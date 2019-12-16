from api.requests.poi import get_poi_by_id
import requests
from constants import paths


def poi_id_message(poi_id):
    if poi_id == 0:
        return "Please use only digit IDs that > 0"
    try:
        result = get_poi_by_id(poi_id).json()
        poi_info = result['data']['poi']
        name = poi_info['name']
        description = poi_info['description']
        category = poi_info['category']['name']
        address = poi_info['formattedAddress']
        email = poi_info['email']
        phone = poi_info['phone']
        web = poi_info['web']
        try:
            image_url = requests.get(poi_info['images'][0]['originalUrl'])
            image = image_url.content
            image_ex = True
        except IndexError:
            image_ex = False
        return f"POI Name: {name}\nPOI Description: {description}\nPOI Category: {category}\nPOI Address: {address}\n" \
               f"Email: {email}\nPhone: {phone}\nWebsite: {web}\nImage: {image_ex}"
    except AttributeError:
        return get_poi_by_id(poi_id)


def poi_id_image(poi_id):
    if poi_id == 0:
        return "Please use only digit IDs that > 0"
    try:
        result = get_poi_by_id(poi_id).json()
        poi_info = result['data']['poi']
        image_url = requests.get(poi_info['images'][0]['originalUrl'])
        image = image_url.content
        paths.folder_check()
        image_file = open(paths.IMAGE_DIR+'image.png', mode='wb+')
        image_file.write(image)
        image_file.close()
        return f"Image saved in {paths.IMAGE_DIR}"
    except IndexError:
        return "Image doesn't exist."
    except AttributeError:
        return get_poi_by_id(poi_id)
