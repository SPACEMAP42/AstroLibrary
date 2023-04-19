class Conjunction:
    def __init__(self, conjunction):
        self.__created_at = conjunction["createdAt"]
        self.__primary_id = conjunction["pId"]
        self.__primary_name = conjunction["pName"]
        self.__secondary_id = conjunction["sId"]
        self.__secondary_name = conjunction["sName"]
        self.__dca = conjunction["dca"]
        self.__tca = conjunction["tcaTime"]
        self.__probability = conjunction["probability"]

    @property
    def created_at(self):
        return self.__created_at

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
    def probability(self):
        return self.__probability

    def __repr__(self):
        data = {
            "created_at": self.__created_at,
            "primary_id": self.__primary_id,
            "primary_name": self.__primary_name,
            "secondary_id": self.__secondary_id,
            "secondary_name": self.__secondary_name,
            "dca": self.__dca,
            "tca": self.__tca,
            "probability": self.__probability,
        }
        return data
