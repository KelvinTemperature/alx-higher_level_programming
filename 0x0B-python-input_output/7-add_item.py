#!/usr/bin/python3
"""ADDS ARG TO PYTHON LIST"""

import sys
import os


save_to_file = __import__('5-save_to_json_file').save_to_json_file
load_from_file = __import__('6-load_from_json_file').load_from_json_file

load_list = []

if os.path.exists("add_item.json"):
    load_list = load_from_file("add_item.json")

for arg in sys.argv[1:]:
    load_list.append(arg)

save_to_file(load_list, "add_item.json")
