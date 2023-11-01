import json


class ConjunctionList:
    def __init__(self, response):
        self.__conjunctions = response["conjunctions"]

    def write_file(self, file_path: str) -> None:
        with open(f"{file_path}", "w") as file:
            json.dump(self.__repr__(), file, indent=4)

    @property
    def conjunctions(self):
        return self.__conjunctions

    @conjunctions.setter
    def conjunctions(self, conjunctions) -> None:
        self.__conjunctions = conjunctions

    def __repr__(self) -> str:
        data = {
            "conjunctions": [
                conjunction.__repr__() for conjunction in self.__conjunctions
            ],
        }
        return json.dumps(data, indent=4)
