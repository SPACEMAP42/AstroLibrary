import json
from datetime import datetime
from typing import List
from astrolibrary.data.tle import TLE


class TLEAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def get_recent_tles(self, limit: int = None, page: int = None) -> List[TLE]:
        endpoint = "/tles"
        url = self.__base_url + endpoint
        params = {"limit": limit, "page": page}
        keys_to_delete = [k for k, v in params.items() if v is None]
        for key in keys_to_delete:
            del params[key]
        response = self.__session.get(url, params=params)
        return self.tles_dict_to_tles_object(response.json()["data"]["tles"])

    def get_tle_by_norad_id_and_date(
        self, norad_id, date: datetime = datetime.now()
    ) -> List[TLE]:
        year = date.year
        month = date.month
        day = date.day
        hour = date.hour
        endpoint = f"/tles/{year}/{month}/{day}/{hour}"
        url = self.__base_url + endpoint
        params = {"id": norad_id}
        response = self.__session.get(url, params=params)
        return self.tles_dict_to_tles_object(response.json()["data"]["tles"])

    def tles_dict_to_tles_object(self, tles_dict) -> List[TLE]:
        tles: List[TLE] = list()
        for tle_dict in tles_dict:
            tle = TLE(tle_dict)
            tles.append(tle)
        return tles
