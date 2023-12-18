import json

class LinkOptimization:
    def __init__(self, response):
        self.__id = response["_id"]
        self.__source_latitude = response["sourceLatitude"]
        self.__source_longitude = response["sourceLongitude"]
        self.__destination_latitude = response["destinationLatitude"]
        self.__destination_longitude = response["destinationLongitude"]
        self.__lo_epoch_time = response["loEpochTime"]
        self.__lo_end_time = response["loEndTime"]
        self.__prediction_epoch_time = response["predictionEpochTime"]
        self.__link_optimization_db = response["lodb"]

    @property
    def id(self):
        return self.__id
    
    @property
    def source_latitude(self):
        return self.__source_latitude

    @property
    def source_longitude(self):
        return self.__source_longitude

    @property
    def destination_latitude(self):
        return self.__destination_latitude

    @property
    def destination_longitude(self):
        return self.__destination_longitude

    @property
    def lo_epoch_time(self):
        return self.__lo_epoch_time

    @property
    def lo_end_time(self):
        return self.__lo_end_time

    @property
    def prediction_epoch_time(self):
        return self.__prediction_epoch_time

    @property
    def link_optimization_db(self):
        return self.__link_optimization_db
    
    def __repr__(self) -> str:
        data = {
            "id": self.__id,
            "source_latitude": self.__source_latitude,
            "source_longitude": self.__source_longitude,
            "destination_latitude": self.__destination_latitude,
            "destination_longitude": self.__destination_longitude,
            "lo_epoch_time": self.__lo_epoch_time,
            "lo_end_time": self.__lo_end_time,
            "prediction_epoch_time": self.__prediction_epoch_time,
            "link_optimization_db": [
                lodb.__repr__() for lodb in self.__link_optimization_db
            ]
        }
        return json.dumps(data, indent=4)