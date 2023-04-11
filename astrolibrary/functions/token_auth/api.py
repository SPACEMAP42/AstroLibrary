class token_auth:
    def __init__(self, base_url, session, token):
        self.__base_url = base_url
        self.__session = session
        self.__token = token

    def create_session(self):
        endpoint = "/token-auth/token"
        url = self.__base_url + endpoint
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {"authToken": self.__token}
        self.__session.post(url, headers=headers, data=payload)
