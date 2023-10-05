#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['52.91.117.162', '52.87.232.38']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
