import os
from pathlib import Path

WWG_API = "https://api.wewogo.com/api"

def folder_check():
    if not Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'images/')).exists():
        os.mkdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'images/'))

IMAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  'images/')