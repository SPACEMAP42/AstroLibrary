# import os
# import astrolibrary

# from datetime import datetime

# example_access_token = ""

# if __name__ == "__main__":
#     spacemap = astrolibrary.Client(example_access_token)

#     # 1. generate a phantom
#     phantom = astrolibrary.PhantomGenerator.generate_phantom(
#         inclination=30,
#         ascending_node=0,
#         eccentricity=0.1,
#         argument_of_perigee=0,
#         mean_anomaly=0,
#         epoch_date_time="2023-10-25T00:00:00Z",
#         semi_major_axis=7000,
#         mean_motion=15.00,
#         bstar=0.0001,
#         name="test_phantom",
#     )
#     # 1. call phantom conjunction api
#     response = spacemap.phantom_conjunction_API.predict_phantom_conjunction(
#         phantom, threshold=150
#     )
#     print(response)

#     # 2. list of statuses of requests sent to the phantom conjunction server
#     request_list = spacemap.phantom_conjunction_API.get_requests_status_list()["data"]
#     print(request_list)

#     # 3. Select a very last request from the list and read data
#     id = spacemap.phantom_conjunction_API.get_requests_status_list()["data"][-1][
#         "placeId"
#     ]
#     phantom_conjunction_data = spacemap.phantom_conjunction_API.get_predicted_result(id)
#     print(phantom_conjunction_data)

#     # 4. Write into txt file
#     now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
#     path = os.path.abspath(os.path.dirname(__file__))
#     with open(f"{path}/phantom_conjunction_result_{now}.txt", "w") as file:
#         file.write(phantom_conjunction_data.__repr__())
