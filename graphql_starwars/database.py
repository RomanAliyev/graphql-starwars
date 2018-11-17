import json
from os import path


class DataBaseClient(object):
    def __init__(self):
        with open(path.join(path.dirname(__file__), "database.json")) as f:
            self._db = json.load(f)

    def _filter(self, data, options):
        for key, value in options.items():
            if type(value) is list:
                if data.get(key) not in value:
                    return False
            elif data.get(key) != value:
                return False
        return True

    def find(self, type_name, options):
        return list(
            filter(
                lambda data: self._filter(data, options),
                self._db[type_name]
            )
        )


db_client = DataBaseClient()
