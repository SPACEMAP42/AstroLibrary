class LinkOptimizationDB:
    def __init__(self, object):
        self.__lo_current_time = object["loCurrentTime"]
        self.__path = object["path"]
        self.__number_of_hoppings = object["numberOfHoppings"]

    @property
    def lo_current_time(self):
        return self.__lo_current_time

    @property
    def path(self):
        return self.__path

    @property
    def number_of_hoppings(self):
        return self.__number_of_hoppings

    def __repr__(self) -> str:
        data = {
            "lo_current_time": self.__lo_current_time,
            "path": self.__path,
            "number_of_hoppings": self.__number_of_hoppings,
        }
        return str(data)
