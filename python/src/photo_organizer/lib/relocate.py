"""
relocate files to target directory based on exif datetime
"""
import time
import os
import shutil
import uuid

def move((filename, epoch_time), target):
    timestamp = time.gmtime(float(epoch_time))
    target_dir = os.path.join(target,
                          str(timestamp.tm_year),
                          str(timestamp.tm_mon).zfill(2),
                          str(timestamp.tm_mday).zfill(2))
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    target_file = os.path.join(target_dir, os.path.basename(filename))
    if os.path.isfile(target_file):
        target_file = os.path.join(target_dir, 'uuid-%s-%s' % (uuid.uuid4(), os.path.basename(
                                                                                             filename)))
    shutil.move(filename, target_file)