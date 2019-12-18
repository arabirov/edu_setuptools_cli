from api.requests.poi import get_poi_by_id
import requests
from urllib import parse
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
        poi_image_uri = poi_info['images'][0]['originalUrl']
        image_url = requests.get(poi_image_uri)
        file_format = parse.urlsplit(poi_image_uri)[2].split('.')[1]
        image = image_url.content
        paths.folder_check()
        image_file = open(paths.IMAGE_DIR + f'{poi_id}_image.{file_format}', mode='wb+')
        image_file.write(image)
        image_file.close()
        return f"Image saved in {paths.IMAGE_DIR}{poi_id}_image.{file_format}"
    except IndexError:
        return r"This POI doesn't have any images ¯\_(ツ)_/¯."
    except AttributeError:
        return get_poi_by_id(poi_id)
