import json


class LinkOptimization:
    def __init__(self, response):
        self.__id = response["_id"]
        self.__source_latitude = response["sourceLatitude"]
        self.__source_longitude = response["sourceLongitude"]
        self.__destination_latitude = response["destinationLatitude"]
        self.__destination_longitude = response["destinationLongitude"]
        self.__start_time_of_timeline = response["loEpochTime"]
        self.__end_time_of_timeline = response["loEndTime"]
        self.__downloaded_time_of_used_TLE = response["predictionEpochTime"]
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
    def start_time_of_timeline(self):
        return self.__start_time_of_timeline

    @property
    def end_time_of_timeline(self):
        return self.__end_time_of_timeline

    @property
    def downloaded_time_of_used_TLE(self):
        return self.__downloaded_time_of_used_TLE

    @property
    def link_optimization_db(self):
        return self.__link_optimization_db

    def __repr__(self):
        data = {
            "id": self.__id,
            "source_latitude": self.__source_latitude,
            "source_longitude": self.__source_longitude,
            "destination_latitude": self.__destination_latitude,
            "destination_longitude": self.__destination_longitude,
            "start_time_of_timeline": self.__start_time_of_timeline,
            "end_time_of_timeline": self.__end_time_of_timeline,
            "downloaded_time_of_used_TLE,": self.__downloaded_time_of_used_TLE,
            "link_optimization_db": [
                lodb.__repr__() for lodb in self.__link_optimization_db
            ],
        }
        return json.dumps(data, indent=4)
