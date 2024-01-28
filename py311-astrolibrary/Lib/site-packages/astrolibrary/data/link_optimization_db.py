class LinkOptimizationDB:
    def __init__(self, object):
        self.__lo_current_time = object["loCurrentTime"]
        self.__path = object["path"]
        self.__path_length = object["numberOfHoppings"]

    @property
    def lo_current_time(self):
        return self.__lo_current_time

    @property
    def path(self):
        return self.__path

    @property
    def path_length(self):
        return self.__path_length

    def __repr__(self) -> str:
        data = {
            "lo_current_time": self.__lo_current_time,
            "path": self.__path,
            "path_length": self.__path_length,
        }
        return str(data)
