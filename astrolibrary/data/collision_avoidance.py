import json


class CollisionAvoidance:
    def __init__(self, response):
        self.__id = response["_id"]
        self.__primary_id_of_conjunction = response["pIdOfConjunction"]
        self.__secondary_id_of_conjunction = response["sIdOfConjunction"]
        self.__threshold = response["threshold"]
        self.__offset_amount = response["offsetAmount"]
        self.__number_of_paths = response["numberOfPaths"]
        self.__candidate_paths = response["candidatePaths"]
        self.__download_time_of_TLE = response["predictionEpochTime"]
        self.__start_time_of_cola = response["colaEpochTime"]
        self.__end_time_of_cola = response["colaEndTime"]
        self.__collision_avoidance_db = response["coladb"]

    @property
    def id(self):
        return self.__id

    @property
    def primary_id_of_conjunction(self):
        return self.__primary_id_of_conjunction

    @property
    def secondary_id_of_conjunction(self):
        return self.__secondary_id_of_conjunction

    @property
    def threshold(self):
        return self.__threshold

    @property
    def offset_amount(self):
        return self.__offset_amount

    @property
    def number_of_paths(self):
        return self.__number_of_paths

    @property
    def candidate_paths(self):
        return self.__candidate_paths

    @property
    def download_time_of_TLE(self):
        return self.__download_time_of_TLE

    @property
    def start_time_of_cola(self):
        return self.__start_time_of_cola

    @property
    def end_time_of_cola(self):
        return self.__end_time_of_cola

    @property
    def collision_avoidance_db(self):
        return self.__collision_avoidance_db

    def __repr__(self):
        data = {
            "id": self.__id,
            "primary_id_of_conjunction": self.__primary_id_of_conjunction,
            "secondary_id_of_conjunction": self.__secondary_id_of_conjunction,
            "threshold": self.__threshold,
            "offset_amount": self.__offset_amount,
            "number_of_paths": self.__number_of_paths,
            "candidate_paths": self.__candidate_paths,
            "download_time_of_TLE": self.__download_time_of_TLE,
            "start_time_of_cola": self.__start_time_of_cola,
            "end_time_of_cola": self.__end_time_of_cola,
            "collision_avoidance_db": [
                {
                    "primary_id": coladb.primary_id,
                    "primary_name": coladb.primary_name,
                    "secondary_id": coladb.secondary_id,
                    "secondary_name": coladb.secondary_name,
                    "distance_of_closest_approach": coladb.distance_of_closest_approach,
                    "entering_time": coladb.entering_time,
                    "time_of_closest_approach": coladb.time_of_closest_approach,
                    "leaving_time": coladb.leaving_time,
                }
                for coladb in self.__collision_avoidance_db
            ],
        }
        return json.dumps(data, indent=4)
