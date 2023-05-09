import json
from sgp4.api import Satrec, jday, SatrecArray
from datetime import datetime
from astrolibrary.data.tle import TLE
import numpy as np
from typing import List


class SpaceObjects:
    def __init__(self, tles: List[TLE]):
        self.__tles = tles
        self.satrecs = dict()
        self.coordinates = []
        self.satrecs_array = None
        self.make_satrecs()

    def make_satrecs(self):
        for tle in self.__tles:
            satrec = Satrec.twoline2rv(tle.first_line, tle.second_line)
            self.satrecs[satrec.satnum] = satrec
        self.satrecs_array = SatrecArray(list(self.satrecs.values()))

    def position_vector_of_objects_at_moment(self, moment: datetime):
        self.coordinates = []
        year = moment.year
        month = moment.month
        day = moment.day
        hour = moment.hour
        minute = moment.minute
        second = moment.second
        jd, fr = jday(year, month, day, hour, minute, second)

        jd = np.array([jd])
        fr = np.array([fr])

        e, r, v = self.satrecs_array.sgp4(jd, fr)
        # for satrec in self.satrecs.values():
        #     e, r, v = satrec.sgp4(jd, fr)
        r = np.array(r)
        self.coordinates = r

        return self.coordinates
