import os
import requests
import configparser
from .apis.conjunction.api import ConjunctionAPI
from .apis.token_auth.api import TokenAuthAPI
from .apis.tle.api import TLEAPI
from .apis.watcher_catcher.api import WatcherCatcherAPI


class Client:
    def __init__(self, token):
        # save base url
        __config = configparser.ConfigParser()
        config_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "config.ini"
        )
        __config.read(config_path)
        self.__base_url = __config.get("SPACEMAP", "BASE_URL")

        # create http session
        self.__token = token
        self.__session = requests.Session()
        self.token_auth_API = TokenAuthAPI(
            self.__base_url, self.__session, self.__token
        )
        self.token_auth_API.create_session()

        # create api member variables
        self.conjunction_API = ConjunctionAPI(self.__base_url, self.__session)
        self.tle_API = TLEAPI(self.__base_url, self.__session)
        self.watcher_catcher_API = WatcherCatcherAPI(self.__base_url, self.__session)
