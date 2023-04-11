from datetime import datetime


class Tle:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def get_recent_tles(self):
        endpoint = "/tles"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()["data"]

    def get_tle_by_norad_id_and_date(self, norad_id, date: datetime = datetime.now()):
        year = date.year
        month = date.month
        day = date.day
        hour = date.hour
        endpoint = f"/tles/{year}/{month}/{day}/{hour}"
        url = self.__base_url + endpoint
        params = {"id": norad_id}
        response = self.__session.get(url, params=params)
        return response.json()["data"]
