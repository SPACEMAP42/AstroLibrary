import json


class Conjunction:
    def __init__(self, conjunction):
        self.__created_at = conjunction["createdAt"]
        self.__p_id = conjunction["pId"]
        self.__p_name = conjunction["pName"]
        self.__s_id = conjunction["sId"]
        self.__s_name = conjunction["sName"]
        self.__dca = conjunction["dca"]
        self.__tca_time = conjunction["tcaTime"]
        self.__tca_start_time = conjunction["tcaStartTime"]
        self.__tca_end_time = conjunction["tcaEndTime"]
        self.__standard_time = conjunction["standardTime"]
        self.__probability = conjunction["probability"]

    @property
    def p_id(self):
        return self.__p_id

    # def __repr__(self):
    #     return f"\n\
    #         created_at: {self.__created_at}\n\
    #         p_id: {self.__p_id}\n\
    #         p_name: {self.__p_name}\n\
    #         s_id: {self.__s_id}\n\
    #         s_name: {self.__s_name}\n\
    #         dca: {self.__dca}\n\
    #         tca_time: {self.__tca_time}\n\
    #         tca_start_time: {self.__tca_start_time}\n\
    #         tca_end_time: {self.__tca_end_time}\n\
    #         standard_time: {self.__standard_time}\n\
    #         probability: {self.__probability}"

    def __repr__(self):
        data = {
            "created_at": self.__created_at,
            "p_id": self.__p_id,
            "p_name": self.__p_name,
            "s_id": self.__s_id,
            "s_name": self.__s_name,
            "dca": self.__dca,
            "tca_time": self.__tca_time,
            "tca_start_time": self.__tca_start_time,
            "tca_end_time": self.__tca_end_time,
            "standard_time": self.__standard_time,
            "probability": self.__probability,
        }
        return json.dumps(data, indent=4)
