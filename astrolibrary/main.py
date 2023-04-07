import requests
import configparser
from functions.ppdb.api import ppdb
from functions.token_auth.api import token_auth

class AstroLib:
    def __init__(self, token):
        config = configparser.ConfigParser()
        config.read('./config.ini')
        self.base_url = config.get('SPACEMAP', 'BASE_URL')
        self.token = token
        self.session = requests.Session()
        self.token_auth = token_auth(self.base_url,  self.session, self.token)


if __name__ == "__main__":
    astroLib = AstroLib("Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi")
    astroLib.token_auth.create_session_cookie()