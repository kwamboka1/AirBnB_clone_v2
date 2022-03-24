#!/usr/bin/python3
""" Function that compresses a folder """

from datetime import datetime
from fabric.api import local
from  os.path import isdir 


"""A function that generates a tgz archive"""
def do_pack():
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local('mkdir versions')
        file_name = "versions/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except:
        return None
