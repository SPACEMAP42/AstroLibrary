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
        apex_latitude: latitude of the apex to observe the space objects
            default value: 37.5326 (deg)

        apex_longitude: longitude of the apex to observe the space objects
            default value: 127.024612 (deg)

        cone_range: range to observe space objects from the ground
            default value: 2000 (km)

        cone_field_of_view: the extent of the observable world that is seen at any given moment, indicating the visual range
            default value: 40 (deg)

        start_time_of_timeline: time to start exploring the space objects
            default value: current timexw

        end_time_of_timeline: time to end object search
            default value: 1 hour from current time

            
    Example result (show only 2 watching_time_interval examples)
    ------------------------------------------
    {
        "id": "643d0a524623d86432a04ce4",
        "apex_latitude": 37.5326,
        "apex_longitude": 127.024612,
        "cone_range": 2000,
        "cone_field_of_view": 40,
        "start_time_of_timeline": "2023-04-17T08:58:58.170Z",
        "end_time_of_timeline": "2023-04-17T09:58:58.170Z",
        "downloaded_time_of_used_TLE": "2023-04-16T09:00:00.000Z",
        "watching_time_interval": [
            {
                "primary_id": 0,
                "primary_name": "Apex",
                "secondary_id": 55999,
                "secondary_name": "STARLINK-5901",
                "start_time_of_time_interval": "2023-04-19T08:10:59.000Z",
                "end_time_of_time_interval": "2023-04-19T08:11:09.000Z"
            },
            {
                "primary_id": 0,
                "primary_name": "Apex",
                "secondary_id": 87235,
                "secondary_name": "TBA - TO BE ASSIGNED",
                "start_time_of_time_interval": "2023-04-19T08:10:49.000Z",
                "end_time_of_time_interval": "2023-04-19T08:11:09.000Z"
            }
        ]
    }
    """

    # 1. call api with default parameters
    # send request to watcher catcher server
    response = ROK_airforce.watcher_catcher_API.predict_watcher_catcher()

    # # 2. list of statuses of requests sent to the watcher catcher server
    request_list = ROK_airforce.watcher_catcher_API.get_requests_status_list()["data"]
    print(request_list)

    # 3. Select a very last request from the list and read data
    # Save the database id, then read the value from that database
    # If you want to get the previous result rather than the last one, you can query the database.
    id = ROK_airforce.watcher_catcher_API.get_requests_status_list()["data"][-1]["_id"]
    print(ROK_airforce.watcher_catcher_API.get_predicted_result(id))

    # API to clear the id of a specific database from the list
    ROK_airforce.watcher_catcher_API.delete_predicted_result(id)

    # # A function that performs steps 1-3 above at once
    print(ROK_airforce.watcher_catcher_API.predict_watcher_catcher_and_get_result())
