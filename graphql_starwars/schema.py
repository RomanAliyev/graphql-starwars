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
    Droid,
    Character
)

queryType = GraphQLObjectType(
    "Query",
    fields=lambda: {
        "me": GraphQLField(
            characterInterface,
            resolver=lambda obj, info:
                Character.find_one({"_id": info.context.get("user_id")}),
        ),
        "human": GraphQLField(
            humanType,
            args={
                "id": GraphQLArgument(GraphQLNonNull(GraphQLID))
            },
            resolver=lambda obj, info, id: Human.find_one({"_id": id}),
        ),
        "droid": GraphQLField(
            droidType,
            args={
                "id": GraphQLArgument(GraphQLNonNull(GraphQLID))
            },
            resolver=lambda obj, info, id: Droid.find_one({"_id": id}),
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
            resolver=lambda obj, info: Character.find_many({"_id": obj.friends})
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
            resolver=lambda obj, info: Character.find_many({"_id": obj.friends}),
        ),
    },
    interfaces=[characterInterface],
)

schema = GraphQLSchema(query=queryType)
