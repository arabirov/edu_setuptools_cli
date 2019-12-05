from api.requests.poi import get_poi_by_id
import requests


def poi_id_message(poi_id):
    if poi_id == 0:
        return "Please use only digit IDs that > 0"
    try:
        result = get_poi_by_id(poi_id).json()
        poi_info = result['data']['poi']
        image_url = requests.get(poi_info['images'][0]['originalUrl'])
        name = poi_info['name']
        description = poi_info['description']
        category = poi_info['category']['name']
        address = poi_info['formattedAddress']
        email = poi_info['email']
        phone = poi_info['phone']
        web = poi_info['web']
        image = image_url.content
        return f"POI Name: {name}\nPOI Description: {description}\nPOI Category: {category}\nPOI Address: {address}\n" \
               f"Email: {email}\nPhone: {phone}\nWebsite: {web}"
    except AttributeError:
        return get_poi_by_id(poi_id)
