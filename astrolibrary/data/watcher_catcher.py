import json


class WatcherCatcher:
    def __init__(self, response):
        self.__id = response["_id"]
        self.__latitude = response["latitude"]
        self.__longitude = response["longitude"]
        self.__altitude = response["altitude"]
        self.__field_of_view = response["fieldOfView"]
        self.__wc_epoch_time = response["wcEpochTime"]
        self.__wc_end_time = response["wcEndTime"]
        self.__prediction_epoch_time = response["predictionEpochTime"]
        self.__wcdb = response["wcdb"]

    @property
    def id(self):
        return self.__id

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude

    @property
    def altitude(self):
        return self.__altitude

    @property
    def field_of_view(self):
        return self.__field_of_view

    @property
    def wc_epoch_time(self):
        return self.__wc_epoch_time

    @property
    def wc_end_time(self):
        return self.__wc_end_time

    @property
    def prediction_epoch_time(self):
        return self.__prediction_epoch_time

    @property
    def wcdb(self):
        return self.__wcdb

    def __repr__(self) -> str:
        data = {
            "id": self.__id,
            "latitude": self.__latitude,
            "longitude": self.__longitude,
            "altitude": self.__altitude,
            "field_of_view": self.__field_of_view,
            "wc_epoch_time": self.__wc_epoch_time,
            "wc_end_time": self.__wc_end_time,
            "prediction_epoch_time": self.__prediction_epoch_time,
            "wcdb": [wcdb.__repr__() for wcdb in self.__wcdb],
        }
        return json.dumps(data, indent=4)
