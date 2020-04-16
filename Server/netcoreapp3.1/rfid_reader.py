#!/usr/bin/env python

import sqlite3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import datetime
from sql_requests import *


reader = SimpleMFRC522()
interrupted = False


def read_loop():
    while not interrupted:
        try:
            id, text = reader.read()
            conn = sqlite3.connect("keylogger.db")
            cursor = conn.cursor()
            allowed = True if cursor.execute(SELECT_FROM_ALLOWED_IDS_BY_ID, [(id)]).fetchone() is not None else False
            cursor.execute(INSERT_HISTORY, (id, text, datetime.datetime.now(), allowed))
            conn.commit()
            with open('reader_log.txt', 'a+') as log:
                log.write(str(id) + '\n')
                log.write(str(text) + '\n\n')
            time.sleep(1)
        finally:
            GPIO.cleanup()


read_loop()
