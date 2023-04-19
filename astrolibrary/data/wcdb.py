class WCDB:
    def __init__(self, object):
        self.__place_id = object["placeId"]
        self.__p_id = object["pId"]
        self.__p_name = object["pName"]
        self.__s_id = object["sId"]
        self.__s_name = object["sName"]
        self.__dca = object["dca"]
        self.__tca_time = object["tcaTime"]
        self.__tca_start_time = object["tcaStartTime"]
        self.__tca_end_time = object["tcaEndTime"]

    @property
    def place_id(self):
        return self.__place_id

    @property
    def p_id(self):
        return self.__p_id

    @property
    def p_name(self):
        return self.__p_name

    @property
    def s_id(self):
        return self.__s_id

    @property
    def s_name(self):
        return self.__s_name

    @property
    def dca(self):
        return self.__dca

    @property
    def tca_time(self):
        return self.__tca_time

    @property
    def tca_start_time(self):
        return self.__tca_start_time

    @property
    def tca_end_time(self):
        return self.__tca_end_time

    def __repr__(self) -> str:
        data = {
            "place_id": self.__place_id,
            "p_id": self.__p_id,
            "p_name": self.__p_name,
            "s_id": self.__s_id,
            "s_name": self.__s_name,
            "dca": self.__dca,
            "tca_time": self.__tca_time,
            "tca_start_time": self.__tca_start_time,
            "tca_end_time": self.__tca_end_time,
        }
        return data
