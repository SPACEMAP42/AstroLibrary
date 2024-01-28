import time
import datetime
from typing import List
from astrolibrary.data.collision_avoidance import CollisionAvoidance
from astrolibrary.data.collision_avoidance_db import CollisionAvoidanceDB


class CollisionAvoidanceAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def __get_current_time(self):
        return datetime.datetime.utcnow()

    def predict_collision_avoidance(
        self,
        primary_id_of_conjunction: int,
        secondary_id_of_conjunction: int,
        offset_amount: int,
        number_of_paths: int,
        threshold: float,
        start_time_of_cola: str = None,
        end_time_of_cola: str = None,
    ):
        if start_time_of_cola == None:
            start_time_of_cola = self.__get_current_time()
        if end_time_of_cola == None:
            end_time_of_cola = self.__get_current_time() + datetime.timedelta(hours=1)

        endpoint = "/collision-avoidance"
        url = self.__base_url + endpoint
        payload = {
            "pIdOfConjunction": primary_id_of_conjunction,
            "sIdOfConjunction": secondary_id_of_conjunction,
            "offsetAmount": offset_amount,
            "numberOfPaths": number_of_paths,
            "threshold": threshold,
            "colaEpochTime": start_time_of_cola,
            "colaEndTime": end_time_of_cola,
        }
        response = self.__session.post(url, data=payload)
        return response.json()

    def read_collision_avoidance_status_list(self):
        endpoint = "/collision-avoidance"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()["data"]

    def find_collision_avoidance_result_by_id(self, id) -> CollisionAvoidance:
        endpoint = f"/collision-avoidance/{id}"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        number_of_attempts = 0
        while response.json()["statusCode"] == 400:
            number_of_attempts += 1
            time.sleep(30)
            print("Waiting for the result" + " (attempt: " + str(number_of_attempts) + ")." + "\n")
            response = self.__session.get(url)
            # if number_of_attempts >= 20:
            #     return None
        return self.__response_to_collision_avoidance_object(response.json()["data"])

    def delete_collision_avoidance_result_by_id(self, id):
        endpoint = f"/collision-avoidance/{id}"
        url = self.__base_url + endpoint
        response = self.__session.delete(url)
        return response.json()

    def __response_to_collision_avoidance_object(self, response) -> CollisionAvoidance:
        object_list: List[CollisionAvoidanceDB] = list()
        for object in response["coladb"]:
            object = CollisionAvoidanceDB(object)
            object_list.append(object)
        response["coladb"] = object_list
        return CollisionAvoidance(response)

    def predict_collision_avoidance_and_get_result(
        self,
        primary_id_of_conjunction: int,
        secondary_id_of_conjunction: int,
        offset_amount: int,
        number_of_paths: int,
        threshold: float,
        start_time_of_cola: str,
        end_time_of_cola: str,
    ):
        self.predict_collision_avoidance(
            primary_id_of_conjunction,
            secondary_id_of_conjunction,
            offset_amount,
            number_of_paths,
            threshold,
            start_time_of_cola,
            end_time_of_cola,
        )
        id = self.read_collision_avoidance_status_list()[-1]["_id"]
        return self.find_collision_avoidance_result_by_id(id)
