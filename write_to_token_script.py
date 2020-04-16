#!/usr/bin/env python

import RPi.GPIO as GPIO
from shell_scripts import *


def write_to_token(text):
    response = "Попытка перезаписи поля text у "
    try:
        _stop_reader()
        id, txt = reader.write(text)
        response += "id - {}. Успешно"
        _start_reader()
    except:
        response = "Попытка перезаписи провалилась"
    finally:
        GPIO.cleanup()
        return response

