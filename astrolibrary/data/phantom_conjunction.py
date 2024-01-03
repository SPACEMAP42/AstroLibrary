import json


class PhantomConjunction:
    def __init__(self, response):
        self.__trajectory_path = response["trajectoryPath"]
        self.__download_time_of_TLE = response["predictionEpochTime"]
        self.__trajectory_length = response["trajectoryLength"]
        self.__phantom_epoch_time = response["launchEpochTime"]
        self.__threshold = response["threshold"]
        self.__watching_time_interval = response["lpdb"]

    @property
    def trajectory_path(self):
        return self.__trajectory_path

    @property
    def download_time_of_TLE(self):
        return self.__download_time_of_TLE

    @property
    def trajectory_length(self):
        return self.__trajectory_length

    @property
    def phantom_epoch_time(self):
        return self.__phantom_epoch_time

    @property
    def threshold(self):
        return self.__threshold

    @property
    def watching_time_interval(self):
        return self.__watching_time_interval

    def __repr__(self) -> str:
        data = {
            "trajectoryPath": self.__trajectory_path,
            "predictionEpochTime": self.__download_time_of_TLE,
            "trajectoryLength": self.__trajectory_length,
            "phantomEpochTime": self.__phantom_epoch_time,
            "threshold": self.__threshold,
            "lpdb": [
                watching_time_interval.__repr__()
                for watching_time_interval in self.__watching_time_interval
            ],
        }
        return json.dumps(data, indent=4)
