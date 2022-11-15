from ebird.api import get_observations
import os

api_key = os.getenv("EBIRD_API_KEY")

def insert_data_de_novo():
    """
    {
      "type": "and",
      "predicates": [
        {
          "type": "equals",
          "key": "GADM_GID",
          "value": "CYP",
          "matchCase": false
        },
        {
          "type": "equals",
          "key": "TAXON_KEY",
          "value": "212",
          "matchCase": false
        }
      ]
    }
    :return:
    """
    #GBIF.org (13 November 2022) GBIF Occurrence Download  https://doi.org/10.15468/dl.vpa4jk

    #https://www.gbif.org/occurrence/download?has_coordinate=true&has_geospatial_issue=false&taxon_key=212&geometry=POLYGON((31.55554%2034.39248,35.07267%2034.39248,35.07267%2035.79873,31.55554%2035.79873,31.55554%2034.39248))&occurrence_status=present
    #https://api.gbif.org/v1/occurrence/download?has_coordinate=true&has_geospatial_issue=false&taxon_key=212&geometry=POLYGON((31.55554%2034.39248,35.07267%2034.39248,35.07267%2035.79873,31.55554%2035.79873,31.55554%2034.39248))&occurrence_status=present
    pass

#print(retrieve_data("CY"))# will return long and lat which then we can map approximately to the weather data
# {'speciesCode': 'categr', 'comName': 'Cattle Egret', 'sciName': 'Bubulcus ibis', 'locId': 'L21385774', 'locName': 'Vrysoulles and surrounding area', 'obsDt': '2022-11-03 06:30', 'howMany': 10, 'lat': 35.0818734, 'lng': 33.8747264, 'obsValid': True, 'obsReviewed': False, 'locationPrivate': True, 'subId': 'S121771234'}