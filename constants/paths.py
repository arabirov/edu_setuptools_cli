import os
from pathlib import Path

WWG_API = "https://api.wewogo.com/api"
home = Path.home()


def folder_check():
    if not Path(os.path.join(os.path.dirname(os.path.abspath(home))+"/user", 'poi_images/')).exists():
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(home))+"/user", 'poi_images/'))

# IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
#                                   'images/')


IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(home))+"/user", 'poi_images/')