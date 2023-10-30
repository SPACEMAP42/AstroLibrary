import os
import astrolibrary
from datetime import datetime

example_access_token = "FLKHTmD7kQvowF+FYvIYtegO834kVdzgbAQxA2+YIe1ngSLkDNY6kWQnAog2z6s8"

if __name__ == "__main__":
    spacemap = astrolibrary.Client(example_access_token)

    # 1. call launch conjunction api
    response = spacemap.launch_conjunction_API.predict_launch_conjunction(
        "./example/common/bocachica_J2000_converted.txt", 150)
    print(response)

    # # 2. list of statuses of requests sent to the launch conjunction server
    # request_list = spacemap.launch_conjunction_API.get_requests_status_list()["data"]
    # print(request_list)

    # # 3. Select a very last request from the list and read data
    # # #  Save database id, then read the value from the database.
    # id = spacemap.launch_conjunction_API.get_requests_status_list()["data"][-1]['placeId']
    # launch_conjunction_data = spacemap.launch_conjunction_API.get_predicted_result(id)
    # print(launch_conjunction_data)

    # # write into txt file
    # now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    # path = os.path.abspath(os.path.dirname(__file__))
    # with open(f'{path}/launch_conjunction_result_{now}.txt', 'w') as file:
    #     file.write(launch_conjunction_data.__repr__())

    # # 4. API to delete data corresponding to id from database
    # # spacemap.launch_conjunction_API.delete_predicted_result(id)

