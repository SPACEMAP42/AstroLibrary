import requests

class token_auth:
    def __init__(self, base_url, session, token):
        self.base_url = base_url
        self.session = session
        self.token = token

    def create_session_cookie(self):
        endpoint = '/token-auth/token'
        url = self.base_url + endpoint
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        payload = {
            'authToken': self.token,
        }
        response = self.session.post(url, headers=headers,data=payload)


        print(self.session.cookies.get_dict())