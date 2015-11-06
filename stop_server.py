#!/usr/bin/python
#
# stop artillery
#
#
import subprocess
import os
import signal
from src.core import *

proc = subprocess.Popen("ps -A x | grep artiller[y]", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# kill running instance of artillery
kill_artillery()
