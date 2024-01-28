import json
from collections import UserList


class ConjunctionList(UserList):
    def __init__(self, response):
        self.__conjunctions = response["conjunctions"]

    def write_file(self, file_path: str) -> None:
        with open(f"{file_path}", "w") as file:
            json.dump(self.__conjunctions, file, indent=4)

    @property
    def conjunctions(self):
        return self.__conjunctions

    @conjunctions.setter
    def conjunctions(self, conjunctions) -> None:
        self.__conjunctions = conjunctions

    def __getitem__(self, index):
        return self.__conjunctions.__getitem__(index)

    def __repr__(self):
        return f"{self.__conjunctions}"
