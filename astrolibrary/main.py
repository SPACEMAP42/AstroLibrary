import os
import requests
import configparser
from astrolibrary.functions.conjunction.api import conjunction
from astrolibrary.functions.token_auth.api import token_auth
from astrolibrary.functions.watcher_catcher.api import watcher_catcher

class client:
    def __init__(self, token):
        __config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        __config.read(config_path)
        self.__base_url = __config.get("SPACEMAP", "BASE_URL")
        self.__token = token
        self.__session = requests.Session()
        self.token_auth = token_auth(self.__base_url, self.__session, self.__token)
        self.conjunction = conjunction(self.__base_url, self.__session)
        self.watcher_catcher = watcher_catcher(self.__base_url, self.__session)


# for testing astrolib using local environment !!
if __name__ == "__main__":
    spacemap = client(
        "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
    )
    spacemap.token_auth.create_session()
    print(spacemap.watcher_catcher.post_watcher_catcher(37.5326, 127.024612, 45, 40))