#!/usr/bin/env python

import sqlite3

def init_database():
    conn = sqlite3.connect("keylogger.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE allowed_ids (id text, name text)")
    cursor.execute("CREATE TABLE history (id text, name text, created_date datetime, allowed bool)")
    conn.commit()

init_database()

