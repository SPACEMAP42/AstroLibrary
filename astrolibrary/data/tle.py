import json
from sgp4.api import Satrec, jday
from datetime import datetime
import numpy as np


class TLE:
    def __init__(self, tle_dict):
        self.__title_line = tle_dict["name"]
        self.__first_line = tle_dict["firstLine"]
        self.__second_line = tle_dict["secondLine"]

    @property
    def title_line(self):
        return self.__title_line

    @property
    def first_line(self):
        return self.__first_line

    @property
    def second_line(self):
        return self.__second_line

    def __repr__(self):
        return f"title_line: {self.__title_line}\nfirst_line: {self.__first_line}\nsecond_line: {self.__second_line}"

    # @staticmethod
    # def from_json(json_dict):
    #     return TLE(json_dict["name"], json_dict["firstLine"], json_dict["secondLine"])
