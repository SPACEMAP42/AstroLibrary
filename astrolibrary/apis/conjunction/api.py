from enum import Enum
from typing import List
from astrolibrary.data.conjunction import Conjunction


class ConjunctionAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    class sort_type(Enum):
        tcaTime = "tcaTime"
        dca = "dca"

    def get_conjunctions(
        self,
        limit: int = 2,
        page: int = 0,
        sort: sort_type = sort_type.tcaTime,
        satellite: str = None,
    ):
        endpoint = "/ppdb/conjunctions"
        url = self.__base_url + endpoint
        params = {
            "limit": limit,
            "page": page,
            "sort": self.sort_type(sort).name,
            satellite: satellite,
        }
        response = self.__session.get(url, params=params)
        return self.__dict_to_conjunction_object(response.json()["data"])

    def __dict_to_conjunction_object(self, response):
        conjunction_list: List[Conjunction] = list()
        for conjunction in response["conjunctions"]:
            conjunction = Conjunction(conjunction)
            conjunction_list.append(conjunction)
        response["conjunctions"] = conjunction_list
        return response
