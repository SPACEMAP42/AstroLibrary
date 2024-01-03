import os
import astrolibrary
from datetime import datetime, timezone

example_access_token = ""

if __name__ == "__main__":
    spacemap = astrolibrary.Client(example_access_token)

    # exmaple data
    primary_id_of_conjunction = 58463
    secondary_id_of_conjunction = 56358
    offset_amount = 200
    number_of_paths = 5
    threshold = 50
    start_time_of_cola = None
    end_time_of_cola = None
    # start_time_of_cola = datetime.strptime("2023-12-28T05:00:00", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    # end_time_of_cola = datetime.strptime("2023-12-28T06:00:00", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)

    # 1. predict link optimization with default parameter
    response = spacemap.collision_avoidance_API.predict_collision_avoidance(
        primary_id_of_conjunction,
        secondary_id_of_conjunction,
        offset_amount,
        number_of_paths,
        threshold,
        start_time_of_cola,
        end_time_of_cola,
    )
    print(response)

    # 2. read link optimization (get all link optimization prediction list)
    request_list = (
        spacemap.collision_avoidance_API.read_collision_avoidance_status_list()
    )
    print(request_list)

    # 3. find link optimization (get very last link optimization result)
    id = request_list[-1]["_id"]
    collision_avoidance_result = (
        spacemap.collision_avoidance_API.find_collision_avoidance_result_by_id(id)
    )
    print(collision_avoidance_result)

    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    path = os.path.abspath(os.path.dirname(__file__))
    with open(f"{path}/collision_avoidance_result_{now}.txt", "w") as file:
        file.write(collision_avoidance_result.__repr__())

    # 4. delete link optimization (delete link optimization object in database)
    response = spacemap.collision_avoidance_API.delete_collision_avoidance_result_by_id(
        id
    )
    print(response)

    # implement 1 ~ 3 All at once (except task 4)
    collision_avoidance_result = (
        spacemap.collision_avoidance_API.predict_collision_avoidance_and_get_result(
            primary_id_of_conjunction,
            secondary_id_of_conjunction,
            offset_amount,
            number_of_paths,
            threshold,
            start_time_of_cola,
            end_time_of_cola,
        )
    )
    print(collision_avoidance_result)
