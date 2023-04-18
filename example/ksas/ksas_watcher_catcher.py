# The Korean Society for Aeronautical & Space sciences
# 2023 Spring Conference April 19 (Wed) ~ April 21 (Fri)
# An example code using the conjunction API of the astrolibrary version 0.1.1.
# This code retrieves conjunction data and prints them out.
# Author: John Kim
# Date: April 18, 2023


import astrolibrary

example_access_token = (
    "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"
)

if __name__ == "__main__":
    # create an astrolibrary client named ROK_airforce
    ROK_airforce = astrolibrary.Client(example_access_token)

    """
    api to predict space objects observable from any location on the ground

    
    Parameters
    ----------
        latitude: latitude of the point to observe the space objects
            default value: 37.5326

        longitude: longitude of the point to observe the space objects
            default value: 127.024612

        altitude: Altitude to observe space objects from the ground
            default value: 2000

        field_of_view: the angle from the vertex to its wall, indicating the visual range
            default value: 40

        wc_epoch_time: time to start exploring the space objects
            default value: current time

        wc_end_time: time to end object search
            default value: 1 hour from current time

            
    Example result (show only 2 wcdb examples)
    ------------------------------------------
    {
        "id": "643d0a524623d86432a04ce4",
        "latitude": 37.5326,
        "longitude": 127.024612,
        "altitude": 2000,
        "field_of_view": 40,
        "wc_epoch_time": "2023-04-17T08:58:58.170Z",
        "wc_end_time": "2023-04-17T09:58:58.170Z",
        "prediction_epoch_time": "2023-04-16T09:00:00.000Z",
        "wcdb": [
            {
                "place_id": "643d0a524623d86432a04ce4",
                "p_id": 0,
                "p_name": "Site",
                "s_id": 7061,
                "s_name": "DELTA 1 DEB",
                "dca": 1591.417,
                "tca_time": "2023-04-17T08:59:03.000Z",
                "tca_start_time": "2023-04-17T08:59:03.000Z",
                "tca_end_time": "2023-04-17T08:59:22.000Z"
            },
            {
                "place_id": "643d0a524623d86432a04ce4",
                "p_id": 0,
                "p_name": "Site",
                "s_id": 8179,
                "s_name": "THORAD DELTA 1 DEB",
                "dca": 1614.78,
                "tca_time": "2023-04-17T08:59:03.000Z",
                "tca_start_time": "2023-04-17T08:59:03.000Z",
                "tca_end_time": "2023-04-17T08:59:57.000Z"
            }
        ]
    }
    """

    # 1. call api with default parameters
    # send request to watcher catcher server
    response = ROK_airforce.watcher_catcher_API.predict_watcher_catcher()

    # 2. list of statuses of requests sent to the watcher catcher server
    request_list = ROK_airforce.watcher_catcher_API.get_requests_status_list()["data"]
    print(request_list)

    # 3. Select a very last request from the list and read data
    # Save the database id, then read the value from that database
    # If you want to get the previous result rather than the last one, you can query the database.
    id = ROK_airforce.watcher_catcher_API.get_requests_status_list()["data"][-1]["_id"]
    print(ROK_airforce.watcher_catcher_API.get_predicted_result(id))

    # API to clear the id of a specific database from the list
    ROK_airforce.watcher_catcher_API.delete_predicted_result(id)

    # A function that performs steps 1-3 above at once
    print(ROK_airforce.watcher_catcher_API.predict_watcher_catcher_and_get_result())
