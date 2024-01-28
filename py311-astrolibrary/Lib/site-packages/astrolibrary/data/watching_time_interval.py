class WatchingTimeInterval:
    def __init__(self, object):
        # self.__place_id = object['placeId']
        self.__primary_id = object['pId']
        self.__primary_name = object['pName']
        self.__secondary_id = object['sId']
        self.__secondary_name = object['sName']
        self.__dca = object['dca']
        self.__tca = object['tcaTime']
        self.__start_time_of_time_interval = object['tcaStartTime']
        self.__end_time_of_time_interval = object['tcaEndTime']

    # @property
    # def place_id(self):
    #     return self.__place_id

    @property
    def primary_id(self):
        return self.__primary_id

    @property
    def primary_name(self):
        return self.__primary_name

    @property
    def secondary_id(self):
        return self.__secondary_id

    @property
    def secondary_name(self):
        return self.__secondary_name

    @property
    def dca(self):
        return self.__dca

    @property
    def tca(self):
        return self.__tca

    @property
    def start_time_of_time_interval(self):
        return self.__start_time_of_time_interval

    @property
    def end_time_of_time_interval(self):
        return self.__end_time_of_time_interval

    def __repr__(self) -> str:
        data = {
            'primary_id': self.__primary_id,
            'primary_name': self.__primary_name,
            'secondary_id': self.__secondary_id,
            'secondary_name': self.__secondary_name,
            'start_time_of_time_interval': self.__start_time_of_time_interval,
            'end_time_of_time_interval': self.__end_time_of_time_interval,
        }
        return str(data)
