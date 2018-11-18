import json
from .schema import schema
from os import path
import graphql
from werkzeug.wrappers import Request, Response


@Request.application
def application(request):
    if request.path == "/graphql":
        if request.method == "GET":
            # showing GraphiQL page
            with open(path.join(path.dirname(__file__), "graphiql.html")) as f:
                return Response(
                    f.read(),
                    mimetype="text/html"
                )
        elif request.method == "POST":
            # fulfilling GraphQL operations
            request_data = json.loads(request.data)
            graphql_result = graphql.graphql(
                schema,
                request_string=request_data.get("query"),
                variables=request_data.get("variables"),
                operation_name=request_data.get("operationName"),
                context={
                    "user_id": "2001"
                }
            ).to_dict()
            return Response(
                json.dumps(graphql_result),
                mimetype="application/json"
            )
    return Response("Not Found", status=404)
