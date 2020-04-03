import requests as req
import os
import json
from datetime import datetime
import sys
from bs4 import BeautifulSoup
import threading
import asyncio
import json
from threading import Thread
import time
import shutil
import os
import glob

os.chdir('E:/Projects/generate boilerplate/')
current_dir = os.getcwd() + '/'
# location paths
paths = {
    'freelance': 'E:/Freelance/',
    'side': 'E:/Projects/'
}

# required args
lang_type = input('Language: ')  # node, py
usage_type = input('Project Type: ') # scrape
location = input('Side or Freelance :') # freelance, side
project_name = input('Project Name: ')
file_name = input('Entry File Name (without extension): ')


def copytree(src, path, symlinks=False, ignore=None):
    dst = path+'/node_modules/'
    try:
        os.mkdir(dst)
    except:
        print(f"{path}")
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


if lang_type == 'py':
    if usage_type == 'scrape':
        default_imports = open(
            current_dir + 'templates/imports-py.template.txt', 'r').read()
        scraper_template = open(
            current_dir + 'templates/scraper-py.template.txt', 'r').read()
        print(default_imports)
        path = paths[location] + project_name + '/'
        try:
            os.mkdir(path)
        except:
            print(f"{path} already exist")
        file = open(path + file_name + '.py',  'w+')
        file.write(f'{default_imports} \n\n{scraper_template}')
        print(f'[SUCCESS] GO TO {path}')
else:
    if usage_type == 'scrape':
        default_imports = open(
            current_dir + 'templates/imports-nodejs.template.txt', 'r').read()
        scraper_template = open(
            current_dir + 'templates/scraper-nodejs.template.txt', 'r').read()
        # copy node_modules over to the project folder
        path = paths[location] + project_name
        copytree(current_dir + 'templates/node_modules', path)
        file = open(path + '/' + file_name + '.js',  'w+')
        file.write(f'{default_imports} \n\n{scraper_template}')
        print(f'[SUCCESS] {path}')
        os.system("code "+ path)
