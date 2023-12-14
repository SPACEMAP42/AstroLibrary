# An example code using the conjunction API of the astrolibrary version 0.1.5.
# This code retrieves conjunction data and prints them out.
# Author: John Kim, Shawn Choi
# Date: November 1, 2023

# Step 1: Include the system library and AstroLibrary
from datetime import datetime
import os
import astrolibrary
from astrolibrary.data.constellation import Constellation

EXAMPLE_ACCESS_TOKEN = ""

if __name__ == "__main__":
    # Step 2: Create an astrolibrary client named SPACEMAP
    SPACEMAP = astrolibrary.Client(EXAMPLE_ACCESS_TOKEN)

    # Step 3-A: Search Top-10 of all-on-all CA results sorted by DCA
    conjunction_assessment_data_sorted_by_dca = (
        SPACEMAP.conjunction_API.search_conjunctions(limit=10, sort="dca")
    )
    print(conjunction_assessment_data_sorted_by_dca)
    # Step 3-B: Search Top-5 of “KOMPSAT 5” CA results sorted by TCA
    kompsat_5_conjunction_assessment_data = (
        SPACEMAP.conjunction_API.search_conjunctions(
            limit=5, sort="tca", sat_name="KOMPSAT 5"
        )
    )

    # Step 3-C: Search Top-5 of “25544” (ISS) CA results sorted by TCA
    iss_conjunction_assessment_data = SPACEMAP.conjunction_API.search_conjunctions(
        limit=5, sort="tca", norad_id="25544"
    )

    # Step 3-D: Call API with different parameters (Top-10 of "STARLINK" constellation CA results sorted by DCA)
    starlink_conjunction_assessment_data = (
        SPACEMAP.conjunction_API.search_conjunctions_for_constellation(
            limit=10, sort="dca", constellation=Constellation.STARLINK
        )
    )

    # Step 4: Write the CA data of STARLINK  to a file
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    path = os.path.abspath(os.path.dirname(__file__))
    file_path = f"{path}/conjunction_assessment_result_{now}.txt"
    starlink_conjunction_assessment_data.write_file(file_path)

    """
    get conjunction api basically uses pagination technique.

    
    Parameters
    ----------
        limit (required): limit the number of conjunctions shown on the page
            default value: 10

        page (required): page to load conjunctions of pagination
            default value: 0
        
        sort (not required): sort the conjunctions by applying various criteria
            default value: tca
            available values: tca, dca

        sat_name (not required): search for conjunctions using objects names
            example value: 39227 (NORAD ID)

        norad_id (not required): search for conjunctions using NORAD ID
            example value: 39227 (NORAD ID)

            
    Outputs
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
