# The Korean Society for Aeronautical & Space sciences
# 2023 Spring Conference April 19 (Wed) ~ April 21 (Fri)
# An example code using the conjunction API of the astrolibrary version 0.1.1.
# This code retrieves conjunction data and prints them out.
# Author: John Kim
# Date: April 17, 2023


import os
import astrolibrary
from datetime import datetime
from astrolibrary.data.constellation import Constellation

example_access_token = ""

if __name__ == "__main__":
    # create an astrolibrary client named SPACEMAP
    SPACEMAP = astrolibrary.Client(example_access_token)

    """
    get conjunction api basically uses pagination technique.

    
    Parameters
    ----------
        limit (required): limit the number of conjunctions shown on the page
            default value: 2

        page (required): page to load conjunctions
            default value: 0
        
        sort (not required): sort the conjunctions by applying various criteria
            default value: tcaTime
            available values: tcaTime, dca

        satellite (not required): search for conjunctions using NORAD ID or TLE objects names
            example value: 39227 (NORAD ID), KOMSAT 5 (object name)

            
    Example result
    --------------
    {
        "total_count": 239129,
        "current_count": 2,
        "conjunctions": [
            {
                "created_at": "2023-04-19T12:00:00.000Z",
                "primary_id": 53683,
                "primary_name": "STARLINK-4625",
                "secondary_id": 47187,
                "secondary_name": "H-2A DEB",
                "dca": 1.551,
                "tca": "2023-04-18T09:00:20.508Z",
                "probability": "N/A"
            },
            {
                "created_at": "2023-04-19T12:00:00.000Z",
                "primary_id": 55355,
                "primary_name": "STARLINK-5647",
                "secondary_id": 47840,
                "secondary_name": "STARLINK-2432",
                "dca": 6.36,
                "tca": "2023-04-18T09:00:24.576Z",
                "probability": "N/A"
            }
        ]
    }
    """

    # call api with default parameters
    conjunction_assessment_data = SPACEMAP.conjunction_API.search_conjunctions(limit=5, page=0)
    print(conjunction_assessment_data)

    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    path = os.path.abspath(os.path.dirname(__file__))
    with open(f'{path}/conjunction_assessment_result_{now}.txt', 'w') as file:
        file.write(conjunction_assessment_data.__repr__())

    # # <class 'astrolibrary.data.conjunction.Conjunction'>
    # print(type(result.conjunctions[0]))

    # # An error occurs because conjunction result is not a dictionary type
    # # print(result['conjunctions'][0]['p_id'])    # error code
    # print(result.conjunctions[0].primary_id)  # success code

    # # How to call an API with differenet parameters
    # result2 = SPACEMAP.conjunction_API.search_conjunctions(limit=5, page=10, sort="dca")
    # print(result2)

    # # How to search for a specific space object you want
    # result3 = SPACEMAP.conjunction_API.search_conjunctions(
    #     limit=10, sort="tcaTime", norad_id_or_name="starlink"
    # )
    # print(result3)

    # # API to find a conjunction between a specific satellite and satellite constellation
    # result4 = SPACEMAP.conjunction_API.search_conjunctions_by_target_object(
    #     target_norad_id=39227, constellation=Constellation.STARLINK
    # )
    # print(result4)
