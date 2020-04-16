#!/usr/bin/env python

import sqlite3
from mfrc522 import SimpleMFRC522
from shell_scripts import *
import os
from sql_requests import *


reader = SimpleMFRC522()


def _get_connection():
    conn = sqlite3.connect("keylogger.db")
    return conn, conn.cursor()


def _stop_reader():
    os.system(KILL_TASK_READER)


def _start_reader():
    os.system(START_TASK_READER)

