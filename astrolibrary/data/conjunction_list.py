import json


class ConjunctionList:
    def __init__(self, response):
        self.__total_count = response["totalCount"]
        self.__current_count = response["currentCount"]
        self.__conjunctions = response["conjunctions"]

    @property
    def total_count(self):
        return self.__total_count

    @total_count.setter
    def total_count(self, new_total_count) -> None:
        self.__total_count = new_total_count

    @property
    def current_count(self):
        return self.__current_count

    @total_count.setter
    def current_count(self, new_current_count) -> None:
        self.__current_count = new_current_count

    @property
    def conjunctions(self):
        return self.__conjunctions

    @conjunctions.setter
    def conjunctions(self, new_conjunctions) -> None:
        self.__conjunctions = new_conjunctions

    def __repr__(self) -> str:
        data = {
            "total_count": self.__total_count,
            "current_count": self.__current_count,
            "conjunctions": [
                conjunction.__repr__() for conjunction in self.__conjunctions
            ],
        }
        return json.dumps(data, indent=4)
