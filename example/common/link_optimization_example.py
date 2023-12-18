import os
import astrolibrary
from datetime import datetime

# john.kim@spacemap42.com
example_access_token = "FLKHTmD7kQvowF+FYvIYtegO834kVdzgbAQxA2+YIe1ngSLkDNY6kWQnAog2z6s8"

# inu.spacemap@gmail.com
# example_access_token = "KxFRFXbU/qbdvPVZ7HkJnlob+zXOVerMWCNv74raMDtiX4LPekZniSSXAR61HVHa"

if __name__ == "__main__":
    spacemap = astrolibrary.Client(example_access_token)

    # 1. predict link optimization with default parameter
    """
    {
        source_latitude: float = 37.4562557,
        source_longitude: float = 126.7051576,
        destination_latitude: float = 34.052235,
        destination_longitude: float = -118.243683,
        lo_epoch_time: str = current time,
        lo_end_time: str = current time + 1 hour
    }
    """

    # response = spacemap.link_optimization_API.predict_link_optimization()
    # print(response)

    
    # # 2. read link optimization (get all link optimization prediction list)
    # request_list = spacemap.link_optimization_API.read_link_optimization()["data"]
    # print(request_list)

    # # 3. find link optimization (get very last link optimization result)
    # id = request_list[-1]["_id"]
    # link_optimization_result = spacemap.link_optimization_API.find_link_optimization(id)
    # print(link_optimization_result)

    # now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    # path = os.path.abspath(os.path.dirname(__file__))
    # with open(f'{path}/link_optimization_result_{now}.txt', 'w') as file:
    #     file.write(link_optimization_result.__repr__())

    # # 4. delete link optimization (delete link optimization object in database)
    # response = spacemap.link_optimization_API.delete_predicted_result(id)
    # print(response)

    
    # implement 1 ~ 3 All at once (except task 4)
    spacemap.link_optimization_API.predict_link_optimization_and_get_result()