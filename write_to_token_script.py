#!/usr/bin/env python

import RPi.GPIO as GPIO
from shell_scripts import *
from sql_requests import  *
from private_scripts import *


def write_to_token(text):
    response = "Попытка перезаписи поля text у "
    try:
        _stop_reader()
        id, txt = reader.write(text)
        conn, cursor = _get_connection()
        if cursor.execute(SELECT_FROM_ALLOWED_IDS_BY_ID, [(str(id))]):
            cursor.execute(UPDATE_ALLOWED_IDS_TEXT_BY_ID, (str(id), str(text)))
            conn.commit()
        response += "id - {}. Успешно"
        _start_reader()
    except:
        response = "Попытка перезаписи провалилась"
    finally:
        GPIO.cleanup()
        return response

