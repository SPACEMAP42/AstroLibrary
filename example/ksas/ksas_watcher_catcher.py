# The Korean Society for Aeronautical & Space sciences
# 2023 Spring Conference April 19 (Wed) ~ April 21 (Fri)
# An example code using the conjunction API of the astrolibrary version 0.1.1.
# This code retrieves conjunction data and prints them out.
# Author: John Kim
# Date: April 18, 2023


import astrolibrary

if __name__ == "__main__":
    # create an astrolibrary client named ROK_airforce
    ROK_airforce = astrolibrary.Client("input access token")

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
