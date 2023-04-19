import time
import datetime
from typing import List
from astrolibrary.data.watcher_catcher import WatcherCatcher
from astrolibrary.data.watching_time_interval import WatchingTimeInterval


class WatcherCatcherAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def __get_current_time(self):
        return datetime.datetime.utcnow()

    def predict_watcher_catcher(
        self,
        apex_latitude: float = 37.5326,
        apex_longitude: float = 127.024612,
        cone_range: float = 2000,
        cone_field_of_view: float = 40,
        start_time_of_timeline: str = None,
        end_time_of_timeline: str = None,
    ):
        if start_time_of_timeline == None:
            start_time_of_timeline = self.__get_current_time()
        if end_time_of_timeline == None:
            end_time_of_timeline = self.__get_current_time() + datetime.timedelta(
                hours=1
            )

        endpoint = "/watcher-catcher"
        url = self.__base_url + endpoint
        payload = {
            "latitude": apex_latitude,
            "longitude": apex_longitude,
            "altitude": cone_range,
            "fieldOfView": cone_field_of_view,
            "wcEpochTime": start_time_of_timeline,
            "wcEndTime": end_time_of_timeline,
        }
        response = self.__session.post(url, data=payload)
        return response.json()

    def get_requests_status_list(self):
        endpoint = "/watcher-catcher"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()

    def get_predicted_result(self, id) -> WatcherCatcher:
        endpoint = f"/watcher-catcher/{id}"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        while response.json()["statusCode"] == 400:
            time.sleep(5)
            response = self.__session.get(url)
        # return response.json()["data"]
        return self.__response_to_watcher_catcher_object(response.json()["data"])

    def delete_predicted_result(self, id):
        endpoint = f"/watcher-catcher/{id}"
        url = self.__base_url + endpoint
        response = self.__session.delete(url)
        return response.json()

    # def delete_entire_predicted_results(self) -> None:
    #     results = self.get_requests_status_list()['data']
    #     for result in results:
    #         id = result['_id']
    #         self.delete_predicted_result(id)

    def __response_to_watcher_catcher_object(self, response) -> WatcherCatcher:
        object_list: List[WatchingTimeInterval] = list()
        for object in response["wcdb"]:
            object = WatchingTimeInterval(object)
            object_list.append(object)
        response["wcdb"] = object_list
        return WatcherCatcher(response)

    def predict_watcher_catcher_and_get_result(
        self,
        apex_latitude: float = 37.5326,
        apex_longitude: float = 127.024612,
        cone_range: float = 2000,
        cone_field_of_view: float = 40,
        start_time_of_timeline: str = None,
        end_time_of_timeline: str = None,
    ):
        self.predict_watcher_catcher(
            apex_latitude,
            apex_longitude,
            cone_range,
            cone_field_of_view,
            start_time_of_timeline,
            end_time_of_timeline,
        )
        id = self.get_requests_status_list()["data"][-1]["_id"]
        return self.get_predicted_result(id)
