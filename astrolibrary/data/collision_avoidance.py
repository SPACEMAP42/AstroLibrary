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
        self.__prediction_epoch_time = response["predictionEpochTime"]
        self.__cola_epoch_time = response["colaEpochTime"]
        self.__cola_end_time = response["colaEndTime"]
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
    def prediction_epoch_time(self):
        return self.__prediction_epoch_time

    @property
    def cola_epoch_time(self):
        return self.__cola_epoch_time

    @property
    def cola_end_time(self):
        return self.__cola_end_time

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
            "prediction_epoch_time": self.__prediction_epoch_time,
            "cola_epoch_time": self.__cola_epoch_time,
            "cola_end_time": self.__cola_end_time,
            "collision_avoidance_db": [
                {
                    "primary_id": coladb.primary_id,
                    "primary_name": coladb.primary_name,
                    "secondary_id": coladb.secondary_id,
                    "secondary_name": coladb.secondary_name,
                    "distance_of_closest_approach": coladb.distance_of_closest_approach,
                    "start_time_of_closest_approach": coladb.start_time_of_closest_approach,
                    "time_of_closest_approach": coladb.time_of_closest_approach,
                    "end_time_of_closest_approach": coladb.end_time_of_closest_approach
                } for coladb in self.__collision_avoidance_db
            ]
        }
        return json.dumps(data, indent=4)
