"""
exif reader
will accpet a filename then try to read exif data from that file
will return dict wih exif info

seems the best library I can find for exif is: https://wiki.gnome.org/Projects/gexiv2
however I can't get it working under osx with virtulenv.
so use http://tilloy.net/dev/pyexiv2/overview.html instead
"""
import pyexiv2
import fractions
import datetime
import time
import os

def get(filename):
    tags = {} 
    if not os.access(filename, os.R_OK):
        return tags
    metadata = pyexiv2.ImageMetadata(filename)
    metadata.read()
    keys = metadata.keys()
    for key in keys:    
        value = None
        tag = metadata[key]
        try:
            if not isinstance(tag.value, (int, str, long, unicode, fractions.Fraction, datetime.datetime)): continue
            
            if isinstance(tag.value, fractions.Fraction):
                value = float(tag.value)
            elif isinstance(tag.value, datetime.datetime):
                value = time.mktime(tag.value.timetuple())
            elif isinstance(tag.value, str):
                value = tag.value.strip()
            else:
                value = tag.value
            if tag.name:
                tags.setdefault(tag.name, value)
        except:
            pass
    
    return tags