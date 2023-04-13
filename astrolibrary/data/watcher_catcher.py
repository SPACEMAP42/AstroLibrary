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

    def get_id(self):
        return self.__id