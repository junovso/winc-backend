
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from os.path import abspath, exists, isdir, isfile
from os import mkdir
from shutil import rmtree
from zipfile import ZipFile
from glob import glob
from fileinput import input


def clean_cache():

    CACHE = abspath('./cache')

    if exists(CACHE) and isdir(CACHE):
        try:
            rmtree(CACHE)
        except OSError:
            print(f'Unable to delete directory: {CACHE}')

    try:
        mkdir(CACHE)
        if exists(CACHE) and isdir(CACHE):
            return CACHE 
        return '' 
    except OSError:
        print(f'Unable to make directory: {CACHE}')


def cache_zip(zip_path, cache_path):
    if exists(zip_path) and isfile(zip_path):
        clean_cache()  
        if exists(cache_path) and isdir(cache_path):
            with ZipFile(zip_path, 'r') as obj:
                obj.extractall(cache_path)
            return True
    return False


def cached_files():

    CACHE = abspath('./cache')

    if exists(CACHE) and isdir(CACHE):
        files = glob(CACHE + '/*.txt', recursive=False)  
        files = [f for f in files if isfile(f)]  
        return files  
    return []  


def find_password(cached_files):

    needle = 'password: '

    with input(cached_files) as f:
        for line in f:
            position = line.find(needle)
            if(position >= 0):
                return line[position + len(needle):-1]  
    return ''  


def main():

    cache = clean_cache()
    zipfile = abspath('./data.zip')

    cache_zip(zipfile, cache)
    files = cached_files()

    password = find_password(files)
    print(password)

    cache = clean_cache()


if __name__ == '__main__':

    # calls here
    main()
  
