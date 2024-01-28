import json


class WatcherCatcher:
    def __init__(self, response):
        self.__id = response["_id"]
        self.__apex_latitude = response["latitude"]
        self.__apex_longitude = response["longitude"]
        self.__cone_range = response["altitude"]
        self.__cone_field_of_view = response["fieldOfView"]
        self.__start_time_of_timeline = response["wcEpochTime"]
        self.__end_time_of_timeline = response["wcEndTime"]
        self.__watching_time_interval = response["wcdb"]
        self.__download_time_of_TLE = response["predictionEpochTime"]

    @property
    def id(self):
        return self.__id

    @property
    def apex_latitude(self):
        return self.__apex_latitude

    @property
    def apex_longitude(self):
        return self.__apex_longitude

    @property
    def cone_range(self):
        return self.__cone_range

    @property
    def cone_field_of_view(self):
        return self.__cone_field_of_view

    @property
    def start_time_of_timeline(self):
        return self.__start_time_of_timeline

    @property
    def end_time_of_timeline(self):
        return self.__end_time_of_timeline

    @property
    def download_time_of_TLE(self):
        return self.__download_time_of_TLE

    @property
    def watching_time_interval(self):
        return self.__watching_time_interval

    def __repr__(self):
        data = {
            "id": self.__id,
            "apex_latitude": self.__apex_latitude,
            "apex_longitude": self.__apex_longitude,
            "cone_range": self.__cone_range,
            "cone_field_of_view": self.__cone_field_of_view,
            "start_time_of_timeline": self.__start_time_of_timeline,
            "end_time_of_timeline": self.__end_time_of_timeline,
            "download_time_of_TLE": self.__download_time_of_TLE,
            "watching_time_interval": [
                watching_time_interval.__repr__()
                for watching_time_interval in self.__watching_time_interval
            ],
        }
        return json.dumps(data, indent=4)
