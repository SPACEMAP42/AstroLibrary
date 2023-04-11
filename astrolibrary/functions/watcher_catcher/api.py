import datetime

class watcher_catcher:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def __get_current_time(self):
        return datetime.datetime.now()

    def post_watcher_catcher(
        self,
        latitude: float = 37.5326,
        longitude: float = 127.024612,
        altitude: float = 45,
        field_of_view: float = 40,
        wc_epoch_time: str = None,
        wc_end_time: str = None,
    ):
        if wc_epoch_time == None:
            wc_epoch_time = self.__get_current_time()
        if wc_end_time == None:
            wc_end_time = self.__get_current_time() + datetime.timedelta(hours=1)

        endpoint = "/watcher-catcher"
        url = self.__base_url + endpoint
        payload = {
            "latitude": latitude,
            "longitude": longitude,
            "altitude": altitude,
            "fieldOfView": field_of_view,
            "wcEpochTime": wc_epoch_time,
            "wcEndTime": wc_end_time,
        }
        response = self.__session.post(url, data=payload)
        return response.json()