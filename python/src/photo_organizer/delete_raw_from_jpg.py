#!/usr/bin/env python
"""
delete raw picture based on the not exist of jpg
usage: ./script jpg_path raw_path
"""
import sys
import os
import shutil
import uuid


def delete_raw_from_jpg(jpg, raw, delete_dir='.delete', debug=False):
    jpg_files = [x.split('.')[0] for x in os.listdir(jpg)]
    raw_files = os.listdir(raw)
    if not os.path.isdir(delete_dir):
        os.mkdir(delete_dir)
    for x in raw_files:
        if x.split('.')[0] not in jpg_files:
            x = os.path.join(raw, x)
            if os.path.isfile(x):
                if debug:
                    print "remove %s" % x
                basename = os.path.basename(x)
                if not os.path.isfile(os.path.join(delete_dir, basename)):
                    shutil.move(x, delete_dir)
                else:
                    unique = uuid.uuid4()
                    shutil.move(x, os.path.join(delete_dir, '%s-uuid-%s' % (basename, unique)))


if '__main__' == __name__:
    if len(sys.argv) < 3:
        raise SystemExit('%s jpg_path raw_path' % sys.argv[0])
    jpg = sys.argv[1]
    raw = sys.argv[2]
    delete_raw_from_jpg(jpg, raw, debug=True)