#!/usr/bin/env python

import sqlite3


def get_allowed_ids():
    conn, cursor = _get_connection()
    response = cursor.execute("SELECT * FROM allowed_ids").fetchall()
    return response

