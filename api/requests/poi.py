import requests
from constants.paths import *


def get_poi_by_id(poi_id):
    if requests.get(WWG_API + '/poi/' + str(poi_id)).status_code == 200:
        return requests.get(WWG_API + '/poi/' + str(poi_id))
    else:
        return "Oopsie! POI doesn't exist or not approved yet. Try different POI."
