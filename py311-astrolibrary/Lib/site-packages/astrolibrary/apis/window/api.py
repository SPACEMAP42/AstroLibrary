class WindowAPI:
    def __init__(self, base_url, session):
        self.__base_url = base_url
        self.__session = session

    def read_prediction_window(self):
        endpoint = "/prediction-window"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()["data"]

    def read_link_optimization_window(self):
        endpoint = "/link-optimization-window"
        url = self.__base_url + endpoint
        response = self.__session.get(url)
        return response.json()["data"]
