import os
import requests
import configparser
from .functions.conjunction.api import ConjunctionAPI
from .functions.token_auth.api import TokenAuthAPI
from .functions.tle.api import TLEAPI
from .functions.watcher_catcher.api import WatcherCatcherAPI


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
        self.watcher_catcher_API = WatcherCatcherAPI(self.__base_url, self.__session)
