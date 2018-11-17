from .database import db_client


class ModelObject(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


class Character:
    @staticmethod
    def find_one(options):
        return Human.find_one(options) or Droid.find_one(options)

    @staticmethod
    def find_many(options):
        return Human.find_many(options) + Droid.find_many(options)


class Human(ModelObject):
    @staticmethod
    def find_one(options):
        data = Human.find_many(options)
        return data[0] if len(data) > 0 else None

    @staticmethod
    def find_many(options):
        return list(map(lambda data: Human(
                id=data["_id"],
                name=data.get("name"),
                friends=data.get("friends"),
            ),
            db_client.find("Human", options))
        )


class Droid(ModelObject):
    @staticmethod
    def find_one(options):
        data = Droid.find_many(options)
        return data[0] if len(data) > 0 else None

    @staticmethod
    def find_many(options):
        return list(map(lambda data: Droid(
                id=data["_id"],
                name=data.get("name"),
                friends=data.get("friends"),
            ),
            db_client.find("Droid", options))
        )
