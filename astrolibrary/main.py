import requests
import configparser
from astrolibrary.functions.conjunction.api import conjunction
from astrolibrary.functions.token_auth.api import token_auth
from astrolibrary.functions.tle.api import Tle


class Client:
    def __init__(self, token):
        __config = configparser.ConfigParser()
        __config.read("./astrolibrary/config.ini")
        self.__base_url = __config.get("SPACEMAP", "BASE_URL")
        self.__token = token
        self.__session = requests.Session()
        self.token_auth = token_auth(self.__base_url, self.__session, self.__token)
        self.conjunction = conjunction(self.__base_url, self.__session)
        self.tle = Tle(self.__base_url, self.__session)
