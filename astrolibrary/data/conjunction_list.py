import json


class ConjunctionList:
    def __init__(self, response):
        self.__conjunctions = response["conjunctions"]

    def write_file(self, file_path: str) -> None:
        with open(f"{file_path}", "w") as file:
            file.write(self.__repr__())

    @property
    def conjunctions(self):
        return self.__conjunctions

    @conjunctions.setter
    def conjunctions(self, new_conjunctions) -> None:
        self.__conjunctions = new_conjunctions

    def __repr__(self) -> str:
        data = {
            "conjunctions": [
                conjunction.__repr__() for conjunction in self.__conjunctions
            ],
        }
        return json.dumps(data, indent=4)
