"""
return md5 of a file
"""
import os
import hashlib

def md5(filename):
    if not os.access(filename, os.R_OK):
        return
    m = hashlib.md5()
    m.update(open(filename, 'rb').read())
    return m.hexdigest()