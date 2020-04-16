#!/usr/bin/env python

import sqlite3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from sql_requests import *
from private_scripts import *


def add_allowed(text):
    conn, cursor = _get_connection()
    response = "Попытка добавления нового ID в базу. Результат:"
    try:
        _stop_reader()
        id, txt = reader.write(text)
        if not cursor.execute(SELECT_FROM_ALLOWED_IDS_BY_ID, [(str(id))]).fetchone():
            cursor.execute(INSERT_ALLOWED_IDS, (str(id), str(text)))
            conn.commit()
            response += " Добавление успешно: id - {}, text - {}".format(str(id), str(txt))
        else:
            response += " Добавление не произошло, id {} обнаружен в базе. text {} перезаписан".format(str(id), str(txt))
        _start_reader()
    except:
        response = "Произошла неизвестная ошибка"
    finally:
        GPIO.cleanup()
        return response

