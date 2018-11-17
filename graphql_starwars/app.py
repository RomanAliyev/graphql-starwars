import json
from .schema import schema
from os import path
import graphql


def application(environ, start_response):
    if environ["PATH_INFO"] == "/graphql":
        if environ["REQUEST_METHOD"] == "POST":
            request_data = json.loads(
                environ["wsgi.input"].read(
                    int(environ.get("CONTENT_LENGTH", 0))
                ).decode("utf8")
            )
            graphql_result = graphql.graphql(
                schema,
                request_string=request_data.get("query"),
                variables=request_data.get("variables"),
                operation_name=request_data.get("operationName"),
                context={
                    "user_id": "2001"
                }
            ).to_dict()
            response_data = json.dumps(graphql_result).encode("utf8")
            start_response("200 OK", [("Content-Type", "application/json")])
            return [response_data]
        elif environ["REQUEST_METHOD"] == "GET":
            with open(path.join(path.dirname(__file__), "graphiql.html")) as f:
                response_data = f.read().encode("utf8")
                start_response("200 OK", [('Content-type', 'text/html')])
                return [response_data]
    start_response("500 Internal Server Error", [('Content-type', 'text/plain')])
    return ["500 Internal Server Error".encode("utf8")]
