import requests
from .apis.conjunction.api import ConjunctionAPI
from .apis.token_auth.api import TokenAuthAPI
from .apis.tle.api import TLEAPI
from .apis.watcher_catcher.api import WatcherCatcherAPI
from .apis.phantom_conjunction.api import PhantomConjunctionAPI
from .apis.link_optimization.api import LinkOptimizationAPI


class Client:
    def __init__(self, token):
        # save base url
        # self.__base_url = "https://platformapi.spacemap42.com"
        self.__base_url = "http://localhost:8084"

        # create http session
        self.__token = token
        self.__session = requests.Session()
        self.token_auth_API = TokenAuthAPI(self.__base_url, self.__session, self.__token)
        self.token_auth_API.create_session()

        # create api member variables
        self.conjunction_API = ConjunctionAPI(self.__base_url, self.__session)
        self.tle_API = TLEAPI(self.__base_url, self.__session)
        self.watcher_catcher_API = WatcherCatcherAPI(self.__base_url, self.__session)
        self.phantom_conjunction_API = PhantomConjunctionAPI(self.__base_url, self.__session)
        self.link_optimization_API = LinkOptimizationAPI(self.__base_url, self.__session)
