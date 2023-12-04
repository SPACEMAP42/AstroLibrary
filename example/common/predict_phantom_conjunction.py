# An example code using the phantom conjunction API of the astrolibrary version 0.1.6.
# This code retrieves phantom conjunction data and prints them out.
# Author: John Kim, Shawn Choi
# Date: November 1, 2023

# Step 1: Include the system library and AstroLibrary
import os
import astrolibrary

from datetime import datetime

EXAMPLE_ACCESS_TOKEN = ""

if __name__ == "__main__":
    spacemap = astrolibrary.Client(EXAMPLE_ACCESS_TOKEN)

    # Step 2: Generate a phantom
    phantom = astrolibrary.Phantom.generate_phantom(
        inclination=30,
        ascending_node=0,
        eccentricity=0.1,
        argument_of_perigee=0,
        mean_anomaly=0,
        semi_major_axis=7000,
        mean_motion=15.00,
        bstar=0.0001,
        epoch_date_time="2023-10-25T00:00:00Z",
        trajectory_length_in_seconds=86400,
        name="test_phantom",
    )
    # Step 3: Call phantom conjunction api
    response = spacemap.phantom_conjunction_API.predict_phantom_conjunction(
        phantom, threshold=100
    )

    # Step 4. List of statuses of requests sent to the phantom conjunction server
    status_list = spacemap.phantom_conjunction_API.get_requests_status_list()["data"]

    # Step 5. Select a very last request from the list and read data
    query_id = status_list[-1]["_id"]

    phantom_conjunction_data = spacemap.phantom_conjunction_API.get_predicted_result(
        query_id
    )
    print(phantom_conjunction_data)

    # Step 6. Write the CA of phantom to a file
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    path = os.path.abspath(os.path.dirname(__file__))
    file_path = f"{path}/phantom_conjunction_result_{now}.txt"
    phantom_conjunction_data.write_file(file_path)