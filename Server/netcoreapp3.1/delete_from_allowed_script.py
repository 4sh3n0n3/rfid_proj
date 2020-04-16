#!/usr/bin/env python

import sqlite3
from shell_scripts import *
from sql_requests import *


def delete_from_allowed(id):
    conn, cursor = _get_connection()
    if cursor.execute(SELECT_FROM_ALLOWED_IDS_BY_UD, [(str(id))]).fetchone():
        cursor.execute(DELETE_FROM_ALLOWED_IDS_BY_ID, [(str(id)])
        conn.commit()
        response = "Удаление {} их допустимых успешно произведено".format(str(id))
    else:
        response = "{} не обнаружен в базе".format(str(id))
    return response

