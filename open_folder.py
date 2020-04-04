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

location = input('Side or Freelance :')  # freelance, side
names = []
for f in os.scandir(paths[location]):
    if f.is_dir():
        names.append(f.name)
        print(f"         {f.name}")

project_name = input('Project Name (Folder Name): ')  # folder name

path = paths[location] + project_name

if path not in names :
    for x in names:
        if x.lower().strip() == project_name:
            os.system(f'code "{path}"')
            exit(0)
    print("PROJECT NOT FOUND")
else:
    os.system(f'code "{path}"')
