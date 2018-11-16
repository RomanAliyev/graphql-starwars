from .database import db_client


class Human(object):
    @staticmethod
    def find_one(options):
        data = db_client.find_one("Human", options)
        if data is not None:
            return Human(
                id=data["id"],
                name=data.get("name"),
                friends=data.get("friends"),
            )

    @staticmethod
    def find_many(options):
        return list(map(lambda data: Human(
                id=data["id"],
                name=data.get("name"),
                friends=data.get("friends"),
            ),
            db_client.find_many("Human", options))
        )

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


class Droid(object):
    @staticmethod
    def find_one(options):
        data = db_client.find_one("Droid", options)
        if data is not None:
            return Droid(
                id=data["id"],
                name=data.get("name"),
                friends=data.get("friends"),
            )

    @staticmethod
    def find_many(options):
        return list(map(lambda data: Droid(
                id=data["id"],
                name=data.get("name"),
                friends=data.get("friends"),
            ),
            db_client.find_many("Droid", options))
        )

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
