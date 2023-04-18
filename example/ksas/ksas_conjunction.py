# The Korean Society for Aeronautical & Space sciences
# 2023 Spring Conference April 19 (Wed) ~ April 21 (Fri)
# An example code using the conjunction API of the astrolibrary version 0.1.1.
# This code retrieves conjunction data and prints them out.
# Author: John Kim
# Date: April 17, 2023


import astrolibrary

example_access_token = "Y8HSpeoKt+10sYVL7pRJum2lBg8XFfWOu+LVyN0Y26+5l7EO3WXTbGipnlkgkmPi"

if __name__ == "__main__":
    # Create an astrolibrary client named ROK_airforce
    ROK_airforce = astrolibrary.Client(example_access_token)

    """
    get conjunction api basically uses pagination technique.

    Parameters
    ----------
        limit (required): limit the number of conjunctions shown on the page
            default value: 2

        page (required): page to load conjunctions
            default value: 0
        
        sort (required): sort the conjunctions by applying various criteria
            default value: tcaTime
            available values: tcaTime, dca

        satellite (not required): search for conjunctions using NORAD ID or TLE objects names
            example value: 39227 (NORAD ID), KOMSAT 5 (object name)

    Example result
    --------------
    {'totalCount': 244653, 'currentCount': 2, 'conjunctions': [{
        "created_at": "2023-04-17T12:00:00.000Z",
        "p_id": 31003,
        "p_name": "FENGYUN 1C DEB",
        "s_id": 31661,
        "s_name": "FENGYUN 1C DEB",
        "dca": 9.373,
        "tca_time": "2023-04-16T09:00:00.000Z",
        "tca_start_time": "2023-04-16T09:00:00.000Z",
        "tca_end_time": "2023-04-16T09:00:28.514Z",
        "standard_time": "2023-04-16T09:00:00.000Z",
        "probability": "0.000e+00"
    }, {
        "created_at": "2023-04-17T12:00:00.000Z",
        "p_id": 49044,
        "p_name": "ISS (NAUKA)",
        "s_id": 55860,
        "s_name": "DRAGON CRS-27",
        "dca": 6.323,
        "tca_time": "2023-04-16T09:00:00.000Z",
        "tca_start_time": "2023-04-16T09:00:00.000Z",
        "tca_end_time": "2023-04-17T08:23:30.000Z",
        "standard_time": "2023-04-16T09:00:00.000Z",
        "probability": "1.091e-12"
    }]}
    """

    # call api with default parameters
    result = ROK_airforce.conjunction_API.get_conjunctions()
    print(result)

    # <class 'astrolibrary.data.conjunction.Conjunction'>
    print(type(result['conjunctions'][0]))
    
    # An error occurs because conjunction result is not a dictionary type
    # print(result['conjunctions'][0]['p_id'])    # error code
    print(result['conjunctions'][0].p_id)       # success code

    # How to call an API with differenet parameters
    result2 = ROK_airforce.conjunction_API.get_conjunctions(limit=5, page=10, sort="dca")
    print(result2)

    # How to search for a specific space object you want
    result3 = ROK_airforce.conjunction_API.get_conjunctions(limit=10, sort="tcaTime", satellite="starlink")
    print(result3)