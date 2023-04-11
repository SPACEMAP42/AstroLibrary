from enum import Enum


class conjunction:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    class sort_type(Enum):
        tcaTime = "tcaTime"
        dca = "dca"

    def get_conjunctions(
        self, limit: int = 2, page: int = 0, sort: sort_type = sort_type.tcaTime
    ):
        endpoint = "/ppdb/conjunctions"
        url = self.__base_url + endpoint
        params = {"limit": limit, "page": page, "sort": sort.name}
        response = self.__session.get(url, params=params)
        return response.json()["data"]
