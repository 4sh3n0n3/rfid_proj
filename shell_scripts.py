#!/usr/bin/env python

KILL_TASK_READER =  "pgrep -f 'python rfid_reader\.py*' | xargs kill"
START_TASK_READER = "python rfid_reader.py &"


