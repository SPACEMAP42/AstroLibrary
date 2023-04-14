class WatcherCatcher:
    def __init__(self, object):
        self.__id = object["_id"]
        self.__latitude = object["latitude"]
        self.__longitude = object["longitude"]
        self.__altitude = object["altitude"]
        self.__field_of_view = object["fieldOfView"]
        self.__wc_epoch_time = object["wcEpochTime"]
        self.__wc_end_time = object["wcEndTime"]
        self.__prediction_epoch_time = object["predictionEpochTime"]
        self.__wcdb = object["wcdb"]

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        return f"id: {self.__id}\nlatitude: {self.__latitude}\nlongitude: {self.__longitude}\naltitude: {self.__altitude}\nfield_of_view: {self.__field_of_view}\nwc_epoch_time: {self.__wc_epoch_time}\nwc_end_time: {self.__wc_end_time}\nprediction_epoch_time: {self.__prediction_epoch_time}\nwcdb: {self.__wcdb}\n"
