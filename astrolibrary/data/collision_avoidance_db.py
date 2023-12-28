import json

class CollisionAvoidanceDB:
    def __init__(self, object):
        self.__primary_id = object["pId"]
        self.__primary_name = object["pName"]
        self.__secondary_id = object["sId"]
        self.__secondary_name = object["sName"]
        self.__distance_of_closest_apporoach = object["dca"]
        self.__start_time_of_closest_approach = object["tcaStartTime"]
        self.__time_of_closest_approach = object["tcaTime"]
        self.__end_time_of_closest_appoach = object["tcaEndTime"]

    @property
    def primary_id(self):
        return self.__primary_id

    @property
    def primary_name(self):
        return self.__primary_name

    @property
    def secondary_id(self):
        return self.__secondary_id

    @property
    def secondary_name(self):
        return self.__secondary_name

    @property
    def distance_of_closest_approach(self):
        return self.__distance_of_closest_apporoach

    @property
    def start_time_of_closest_approach(self):
        return self.__start_time_of_closest_approach

    @property
    def time_of_closest_approach(self):
        return self.__time_of_closest_approach

    @property
    def end_time_of_closest_approach(self):
        return self.__end_time_of_closest_appoach

    def __repr__(self):
        data = {
            "primary_id": self.__primary_id,
            "primary_name": self.__primary_name,
            "secondary_id": self.__secondary_id,
            "secondary_name": self.__secondary_name,
            "distance_of_closest_approach": self.__distance_of_closest_apporoach,
            "start_time_of_closest_approach": self.__start_time_of_closest_approach,
            "time_of_closest_approach": self.__time_of_closest_approach,
            "end_time_of_closest_approach": self.__end_time_of_closest_appoach
        }
        return json.dumps(data, indent=4)
