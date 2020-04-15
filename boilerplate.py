import os
import sys
import shutil

os.chdir('E:/Projects/generate boilerplate/')
current_dir = os.getcwd() + '/'

# location paths
paths = {
    'freelance': 'E:/Freelance/',
    'side': 'E:/Projects/'
}

# required args
print('           nodejs')
print('           py')
print('           random')
lang_type = input('Language: ')  # node, py
if lang_type == 'random':
    print("           You don't have to specify project type")
else:
    print('           scrape')
    print('           mobile automation')
    print('           general')
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

path = paths[location] + project_name

if lang_type == 'py':
    if usage_type == 'scrape':
        default_imports = open(
            current_dir + 'templates/imports-py.template.txt', 'r').read()
        scraper_template = open(
            current_dir + 'templates/scraper-py.template.txt', 'r').read()
        path = path + '/'
        try:
            os.mkdir(path)
        except:
            print(f"{path} already exist")
        file = open(path + file_name + '.py',  'w+')
        file.write(f'{default_imports} \n\n{scraper_template}')
        print(f'[SUCCESS] GO TO {path}')
    
    if usage_type == 'general':
        default_imports = open(current_dir + 'templates/imports-py.template.txt', 'r').read()
        path = path + '/'
        try:
            os.mkdir(path)
        except:
            print(f"{path} already exist")
        file = open(path + file_name + '.py',  'w+')
        file.write(f'{default_imports} \n')
        print(f'[SUCCESS] GO TO {path}')

if lang_type == 'random':
    path = path + '/'
    try:
        os.mkdir(path)
    except:
        print(f"{path} already exist")
    print(f'[SUCCESS] GO TO {path}')

if lang_type == 'nodejs': #nodejs
    if usage_type == 'scrape':
        default_imports = open(
            current_dir + 'templates/imports-nodejs.template.txt', 'r').read()
        scraper_template = open(
            current_dir + 'templates/scraper-nodejs.template.txt', 'r').read()
        # copy node_modules over to the project folder
        copytree(current_dir + 'templates/node_modules', path)
        file = open(path + '/' + file_name + '.js',  'w+')
        file.write(f'{default_imports} \n\n{scraper_template}')
        print(f'[SUCCESS] {path}')
    
    if usage_type == 'general':
        default_imports = open(current_dir + 'templates/imports-nodejs.template.txt', 'r').read()
        path = path + '/'
        try:
            os.mkdir(path)
        except:
            print(f"{path} already exist")
        file = open(path + file_name + '.js',  'w+')
        file.write(f'{default_imports} \n')
        print(f'[SUCCESS] GO TO {path}')

    if usage_type == 'mobile automation':
        template = open(current_dir + 'templates/mobile-automation.template.txt', 'r').read()
        path = path + '/'
        try:
            os.mkdir(path)
        except:
            print(f"{path} already exist")
        # copy node_modules over to the project folder
        copytree(current_dir + 'templates/node_modules - mobile automation', path)
        shutil.copy(current_dir + 'templates/desiredCapabilities.js', path)
        shutil.copy(current_dir + 'templates/keyCodes.json', path)
        file = open(path + file_name + '.js',  'w+')
        file.write(f'{template} \n')
        print(f'[SUCCESS] GO TO {path}')


os.system(f'code "{path}"')

