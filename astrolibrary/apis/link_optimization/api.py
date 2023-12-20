import time
import datetime
from typing import List
from astrolibrary.data.link_optimization import LinkOptimization
from astrolibrary.data.link_optimization_db import LinkOptimizationDB


class LinkOptimizationAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def __get_current_time(self):
        return datetime.datetime.utcnow()

    def predict_link_optimization(
        self,
        source_latitude: float = 37.4562557,
        source_longitude: float = 126.7051576,
        destination_latitude: float = 34.052235,
        destination_longitude: float = -118.243683,
        lo_epoch_time: str = None,
        lo_end_time: str = None,
    ):
        if lo_epoch_time == None:
            lo_epoch_time = self.__get_current_time()
            lo_epoch_time = (
                lo_epoch_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"
            )
        if lo_end_time == None:
            lo_end_time = self.__get_current_time() + datetime.timedelta(hours=1)
            lo_end_time = lo_end_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"

        endpoint = "/link-optimization"
        url = self.__base_url + endpoint
        payload = {
            "sourceLatitude": source_latitude,
            "sourceLongitude": source_longitude,
            "destinationLatitude": destination_latitude,
            "destinationLongitude": destination_longitude,
            "loEpochTime": lo_epoch_time,
            "loEndTime": lo_end_time,
        }
        # print(payload)
        response = self.__session.post(url, data=payload)
        return response.json()

    def read_link_optimization_status_list(self):
        endpoint = "/link-optimization"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()

    def find_link_optimization_result_by_id(self, placed_id) -> LinkOptimization:
        endpoint = f"/link-optimization/{placed_id}"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        while response.json()["statusCode"] == 400:
            time.sleep(5)
            response = self.__session.get(url)
        return self.__response_to_link_optimization_class(response.json()["data"])

    def delete_link_optimization_result_by_id(self, placed_id):
        endpoint = f"/link-optimization/{placed_id}"
        url = self.__base_url + endpoint
        response = self.__session.delete(url)
        return response.json()

    def __response_to_link_optimization_class(self, response) -> LinkOptimization:
        print(response)
        lodb_list: List[LinkOptimizationDB] = list()
        for lodb in response["lodb"]:
            lodb = LinkOptimizationDB(lodb)
            lodb_list.append(lodb)
        response["lodb"] = lodb_list
        return LinkOptimization(response)

    def predict_link_optimization_and_get_result(
        self,
        source_latitude: float = 37.4562557,
        source_longitude: float = 126.7051576,
        destination_latitude: float = 34.052235,
        destination_longitude: float = -118.243683,
        lo_epoch_time: str = None,
        lo_end_time: str = None,
    ):
        if lo_epoch_time == None:
            lo_epoch_time = self.__get_current_time()
            lo_epoch_time = (
                lo_epoch_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"
            )
        if lo_end_time == None:
            lo_end_time = self.__get_current_time() + datetime.timedelta(hours=1)
            lo_end_time = lo_end_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+00:00"

        self.predict_link_optimization(
            source_latitude,
            source_longitude,
            destination_latitude,
            destination_longitude,
            lo_epoch_time,
            lo_end_time,
        )
        id = self.read_link_optimization()["data"][-1]["_id"]
        return self.find_link_optimization(id)
