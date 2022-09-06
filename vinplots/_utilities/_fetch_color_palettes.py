
__module_name__ = "__init__.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import packages -------------------------------------------------------------
import wget
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
import requests


# supporting functions --------------------------------------------------------
def _list_dir_html(url, ext):

    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    return [
        os.path.join(url, os.path.basename(node.get("href")))
        for node in soup.find_all("a")
        if node.get("href").endswith(ext)
    ]

def _buffered_wget(url, dest):

    if not os.path.exists(dest):
        wget.download(url, dest, bar=False)

def _fetch_color_palettes(url, dest_dir, ext=".pkl"):
    for f_url in tqdm(_list_dir_html(url, ext)):
        f_name = os.path.basename(f_url)
        dest_path = os.path.join(dest_dir, f_name)
        _buffered_wget(f_url, dest_path)
        
