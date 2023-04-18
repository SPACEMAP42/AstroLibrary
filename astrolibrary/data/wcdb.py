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
    def p_id(self):
        return self.__p_id

    def __repr__(self):
        return f"\nplace_id: {self.__place_id}\np_id: {self.__p_id}\np_name: {self.__p_name}\ns_id: {self.__s_id}\ns_name: {self.__s_name}\ndca: {self.__dca}\ntca_time: {self.__tca_time}\ntca_start_time: {self.__tca_start_time}\ntca_end_time: {self.__tca_end_time}\n"
