import os
import re
import sys
import zipfile
import datetime
import requests

def timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def fix_file_name(name):
    return re.sub('[\/:*?"<>|]', '', name)

def remove_all_file(path):
    if os.path.exists(path):
        for file in os.scandir(path):
            os.remove(file.path)

def create_directory(name):
    if not os.path.exists(name):
        os.makedirs(name)

def get_lib_path():
    return os.getcwd() + '/lib'

#####################################

def is_pyqt5_exists():
    try:
        from PyQt5 import uic
    except:
        return False
    return True

def get_volatility_path():
    return get_lib_path() + '/volatility3-master/vol.py'

def is_volatility_exists():
    return os.path.exists(get_volatility_path())


def download_volatility():
    link = 'https://github.com/volatilityfoundation/volatility3/archive/master.zip'
    path = get_lib_path() + '/volatility3.zip'
    file_download(link, path)
    print('Download finish!')
    print('Unzipping files...')
    zip_file = zipfile.ZipFile(path)
    zip_file.extractall(get_lib_path())
    zip_file.close()
    print('Finish!')


def file_download(link, path):
    with open(path, 'wb') as f:
        print('Downloading %s' % os.path.basename(link))
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')
        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))    
                sys.stdout.flush()
            print()

