import os
import requests
import configparser
from astrolibrary.functions.conjunction.api import ConjunctionAPI
from astrolibrary.functions.token_auth.api import TokenAuthAPI
from astrolibrary.functions.tle.api import TLEAPI


class Client:
    def __init__(self, token):
        __config = configparser.ConfigParser()
        config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "config.ini"
        )
        __config.read(config_path)
        self.__base_url = __config.get("SPACEMAP", "BASE_URL")
        self.__token = token
        self.__session = requests.Session()
        self.token_auth_API = TokenAuthAPI(
            self.__base_url, self.__session, self.__token
        )
        self.conjunction_API = ConjunctionAPI(self.__base_url, self.__session)
        self.tle_API = TLEAPI(self.__base_url, self.__session)
