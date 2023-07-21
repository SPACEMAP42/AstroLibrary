import json


class RfiTimeInterval:
    def __init__(self, rfi_dict):
        self.__target_satellite = rfi_dict["targetSatellite"]
        self.__interferencing_satellite = rfi_dict["interferencingSatellite"]
        self.__site_name = rfi_dict["siteName"]
        self.__site_latitude = rfi_dict["siteLatitude"]
        self.__site_longitude = rfi_dict["siteLongitude"]
        self.__start_time = rfi_dict["startTime"]
        self.__end_time = rfi_dict["endTime"]
        self.__cone_angle = rfi_dict["coneAngle"]
        self.__cone_range = rfi_dict["coneRange"]
        self.__interference_angle = rfi_dict["interferenceAngle"]
        self.__min_angle = rfi_dict["minAngle"]

    @property
    def target_satellite(self):
        return self.__target_satellite

    @target_satellite.setter
    def target_satellite(self, new_target_satellite):
        self.__target_satellite = new_target_satellite

    @property
    def interferencing_satellite(self):
        return self.__interferencing_satellite
    
    @interferencing_satellite.setter
    def interferencing_satellite(self, new_interferencing_satellite):
        self.__interferencing_satellite = new_interferencing_satellite

    @property
    def site_name(self):
        return self.__site_name

    @site_name.setter
    def site_name(self, new_site_name):
        self.__site_name = new_site_name

    @property
    def site_latitude(self):
        return self.__site_latitude

    @site_latitude.setter
    def site_latitude(self, new_site_latitude):
        self.__site_latitude = new_site_latitude

    @property
    def site_longitude(self):
        return self.__site_longitude

    @site_longitude.setter
    def site_longitude(self, new_site_longitude):
        self.__site_longitude = new_site_longitude

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, new_start_time):
        self.__start_time = new_start_time

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, new_end_time):
        self.__end_time = new_end_time

    @property
    def cone_angle(self):
        return self.__cone_angle

    @cone_angle.setter
    def cone_angle(self, new_cone_angle):
        self.__cone_angle = new_cone_angle

    @property
    def cone_range(self):
        return self.__cone_range

    @cone_range.setter
    def cone_range(self, new_cone_range):
        self.__cone_range = new_cone_range

    @property
    def interference_angle(self):
        return self.__interference_angle

    @interference_angle.setter
    def interference_angle(self, new_interference_angle):
        self.__interference_angle = new_interference_angle

    @property
    def min_angle(self):
        return self.__min_angle

    @min_angle.setter
    def min_angle(self, new_min_angle):
        self.__min_angle = new_min_angle

    def __repr__(self) -> str:
        data = {
            "target_satellite": self.__target_satellite,
            "site_name": self.__site_name,
            "site_latitude": self.__site_latitude,
            "site_longitude": self.__site_longitude,
            "start_time": self.__start_time,
            "end_time": self.__end_time,
            "cone_angle": self.__cone_angle,
            "cone_range": self.__cone_range,
            "interference_angle": self.__interference_angle,
            "min_angle": self.__min_angle,
        }
        return json.dumps(data, indent=4)
