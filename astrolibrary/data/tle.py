import json
from sgp4.api import Satrec, jday
from datetime import datetime
import numpy as np


class TLE:
    def __init__(self, tle_dict):
        self.__title_line = tle_dict["name"]
        self.__first_line = tle_dict["firstLine"]
        self.__second_line = tle_dict["secondLine"]
        self.__position_vector = None

    def position_vector_at_moment(self, moment: datetime):
        year = moment.year
        month = moment.month
        day = moment.day
        hour = moment.hour
        minute = moment.minute
        second = moment.second
        jd, fr = jday(year, month, day, hour, minute, second)
        satrec = Satrec.twoline2rv(self.__first_line, self.__second_line)
        e, r, v = satrec.sgp4(jd, fr)
        r = np.array(r)
        self.__position_vector = r
        return r

    @property
    def position_vetor(self):
        return self.__position_vector

    def __repr__(self):
        return f"title_line: {self.__title_line}\nfirst_line: {self.__first_line}\nsecond_line: {self.__second_line}"

    # @staticmethod
    # def from_json(json_dict):
    #     return TLE(json_dict["name"], json_dict["firstLine"], json_dict["secondLine"])
