from enum import Enum
from typing import List
from astrolibrary.data.conjunction import Conjunction
from astrolibrary.data.conjunction_list import ConjunctionList
from astrolibrary.data.constellation import Constellation


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
        target_satellite: str = None,
        constellation: Constellation = None,
    ):
        endpoint = "/ppdb/conjunctions"
        url = self.__base_url + endpoint
        if constellation != None:
            limit = 300000
        params = {
            "limit": limit,
            "page": page,
            "sort": self.sort_type(sort).name,
            "satellite": target_satellite,
        }
        response = self.__session.get(url, params=params)

        result = self.__dict_to_conjunction_object(response.json()["data"])
        if target_satellite != None and constellation != None:
            conjunctions: List[Conjunction] = list()
            for conjunction in result.conjunctions:
                # print(constellation, conjunction.s_id, conjunction.s_name)
                if Constellation(constellation).name in conjunction.s_name:
                    conjunctions.append(conjunction)
            result.conjunctions = conjunctions
            result.total_count = len(conjunctions)
            result.current_count = len(conjunctions)
        return result
        

    def __dict_to_conjunction_object(self, response) -> ConjunctionList:
        conjunction_list: List[Conjunction] = list()
        for conjunction in response["conjunctions"]:
            conjunction = Conjunction(conjunction)
            conjunction_list.append(conjunction)
        response["conjunctions"] = conjunction_list
        return ConjunctionList(response)
