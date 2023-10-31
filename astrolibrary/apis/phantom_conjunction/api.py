import time
import datetime
from typing import List
from astrolibrary.data.phantom_conjunction import PhantomConjunction
from astrolibrary.data.watching_time_interval import WatchingTimeInterval


class PhantomConjunctionAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def predict_phantom_conjunction(
        self,
        trajectory_path,
        threshold,
    ):
        endpoint = "/launch-conjunction"
        url = self.__base_url + endpoint
        payload = {
            "threshold": threshold,
        }
        with open(trajectory_path, "r") as file:
            payload["trajectory"] = file.read()
        response = self.__session.post(url, data=payload)
        return response.json()

    def get_requests_status_list(self):
        endpoint = "/launch-conjunction"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()

    def get_predicted_result(self, id) -> PhantomConjunction:
        endpoint = f"/launch-conjunction/{id}"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        while response.json()["statusCode"] == 400:
            time.sleep(5)
            response = self.__session.get(url)
        # return response.json()["data"]
        return self.__response_to_launch_conjunction_object(response.json()["data"])

    def delete_predicted_result(self, id):
        endpoint = f"/launch-conjunction/{id}"
        url = self.__base_url + endpoint
        response = self.__session.delete(url)
        return response.json()

    def __response_to_phantom_conjunction_object(self, response) -> PhantomConjunction:
        object_list: List[WatchingTimeInterval] = list()
        for object in response["lpdb"]:
            object = WatchingTimeInterval(object)
            object_list.append(object)
        response["lpdb"] = object_list
        return PhantomConjunction(response)
