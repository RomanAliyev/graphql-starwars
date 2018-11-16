from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLNonNull,
    GraphQLString,
    GraphQLArgument,
    GraphQLList,
    GraphQLID,
    GraphQLInterfaceType,
)
from .model import (
    Human,
    Droid
)

queryType = GraphQLObjectType(
    "Query",
    fields=lambda: {
        "human": GraphQLField(
            humanType,
            args={
                "id": GraphQLArgument(GraphQLNonNull(GraphQLID))
            },
            resolver=lambda obj, info, id: Human.find_one({"id": id}),
        ),
        "droid": GraphQLField(
            droidType,
            args={
                "id": GraphQLArgument(GraphQLNonNull(GraphQLID))
            },
            resolver=lambda obj, info, id: Droid.find_one({"id": id}),
        ),
    },
)

characterInterface = GraphQLInterfaceType(
    "Character",
    fields=lambda: {
        "id": GraphQLField(GraphQLNonNull(GraphQLID)),
        "name": GraphQLField(GraphQLString),
        "friends": GraphQLField(GraphQLList(characterInterface)),
    },
    resolve_type=lambda root, info:
        humanType if type(root) is Human else droidType,
)

humanType = GraphQLObjectType(
    "Human",
    fields=lambda: {
        "id": GraphQLField(GraphQLNonNull(GraphQLID)),
        "name": GraphQLField(GraphQLString),
        "friends": GraphQLField(
            GraphQLList(characterInterface),
            resolver=lambda obj, info:
                Human.find_many({"id": obj.friends}) + Droid.find_many({"id": obj.friends}),
        ),
    },
    interfaces=[characterInterface],
)

droidType = GraphQLObjectType(
    "Droid",
    fields=lambda: {
        "id": GraphQLField(GraphQLNonNull(GraphQLID)),
        "name": GraphQLField(GraphQLString),
        "friends": GraphQLField(
            GraphQLList(characterInterface),
            resolver=lambda obj, info:
                Human.find_many({"id": obj.friends}) + Droid.find_many({"id": obj.friends}),
        ),
    },
    interfaces=[characterInterface],
)

schema = GraphQLSchema(query=queryType)
