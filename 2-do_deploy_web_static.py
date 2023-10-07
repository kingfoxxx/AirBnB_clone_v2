#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["54.146.81.220", "52.87.232.38"]
env.user = "ubuntu"


def do_pack():
    """
        return the archive paths if archive has generated correctly.
    """
