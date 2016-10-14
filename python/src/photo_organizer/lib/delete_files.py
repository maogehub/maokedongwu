#!/usr/bin/env python
"""
delete raw picture based on the not exist of jpg
"""
import sys
import os
import shutil
import uuid

def move_file(filename, target = '.delete'):
    newname = os.path.basename(filename)
    if os.path.isfile(os.path.join(target, os.path.basename(filename))):
        newname = 'uuid-%s-%s' % (uuid.uuid4(), os.path.basename(filename))
    if not os.path.isdir(target):
        os.makedirs(target)
    shutil.move(filename, os.path.join(target, newname))
        
def delete_raw_from_jpg(jpg, raw, delete_dir='.delete'):
    jpg_files = [x.split('.')[0] for x in os.listdir(jpg)]
    raw_files = os.listdir(raw)
    if not os.path.isdir(delete_dir):
        os.mkdir(delete_dir)
    for x in raw_files:
        if x.split('.')[0] not in jpg_files:
            x = os.path.join(raw, x)
            if os.path.isfile(x):
                move_file(x, delete_dir)