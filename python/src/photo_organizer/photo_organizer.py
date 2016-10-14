#!/usr/bin/env python
"""
photo organizer
"""
import optparse
import os
import json

from lib import checksum
from lib import exif
from lib import storage
from lib import delete_files
from lib import relocate


def handle_options():
    parser = optparse.OptionParser(version='%prog 1.0')
    parser.add_option('-s', '--source', action = 'store', type = 'string',
                      dest = 'source', help = 'source directory.')
    parser.add_option('-d', '--destination', action = 'store', type = 'string',
                      dest = 'destination', help = 'destination directory.')
    
    parser.add_option('-u', '--unique', action = 'store_true', help = 'delete duplicate from source directory. (use with -s)')
    parser.add_option('-e', '--exif', action = 'store_true', help = 'add exif info to storage.(use with -s)')
    
    parser.add_option('-j', '--jpg', action = 'store', type = 'string',
                       dest = 'jpg', help = 'remove raw in RAW dir if pic not in jpg, works with -r')
    parser.add_option('-r', '--raw', action = 'store', type = 'string',
                       dest = 'raw', help = 'remove raw in RAW dir if pic not in jpg, works with -j')
    
    (options, args) = parser.parse_args()
    help = False
    if options.source:
        #when -s is used. it should work with -d, -u or -e
        if not (options.destination or options.unique or options.exif):
            help = True
    if options.destination:
        #when -d is used. it only work with -s
        if not options.source:
            help = True
    if not (options.source or options.destination):
        #we need at least source or destination in option
        if not (options.jpg and options.raw):
            help = True
    if (options.source and options.destination):
        #if we have both source and destination, unique and exif will not do anything
        if (options.unique or options.exif):
            help = True
    if help:
        parser.print_help()
        raise SystemExit()
    return options
    

def delete_duplication(source):
    """ delete duplicate from source directory
    """
    s = storage.Storage()
    if not os.path.isdir(source):
        raise SystemExit("source must be directory")
    for f in os.listdir(source):
        fname = os.path.abspath(os.path.join(source, f))
        md5 = checksum.md5(fname)
        if s.has_key(fname, md5):
            result = s.fetch_key(data = md5)[0][0]
            if result == fname:
                #same file 
                continue
            else:
                print 'delete duplicate [%s] ::: original [%s]' % (f, result )
                delete_files.move_file(fname)
                
def move_source_to_destination(source, destination):
    """move source files to destination
    """
    s = storage.Storage()
    for f in os.listdir(source):
        fname = os.path.abspath(os.path.join(source, f))
        md5 = checksum.md5(fname)
        if s.has_key(fname, md5):
            print 'delete duplicate [%s]' %f
            delete_files.move_file(fname)
            continue
        tags = exif.get(fname)
        if not tags:
            continue
        s.add_metadata(fname, json.dumps(tags, ensure_ascii= False))
        relocate.move((fname, tags['DateTimeOriginal']), destination)

def main():
    options = handle_options()
    
    #remove raw file if not exist on jpg (-j -r)
    if (options.raw and options.jpg):
        if not (os.path.isdir(options.raw) and os.path.isdir(options.jpg)):
            raise SystemExit("both raw and jpg needs to be directory")
        delete_files.delete_raw_from_jpg(options.jpg, options.raw)
        return
    
    #delete duplicate from source directory (-s -u)
    if (options.source and options.unique):
        delete_duplication(options.source)
        
        
    s = storage.Storage()
    
    #add files to exif storage (-s -e)
    if (options.source and options.exif):
        if not os.path.isdir(options.source):
            raise SystemExit("source must be directory")
        #deduplicate first
        delete_duplication(options.source)
        for f in os.listdir(options.source):
            fname = os.path.abspath(os.path.join(options.source, f))
            s.add_metadata(fname, json.dumps(exif.get(fname)))
            
    #move files from current location to destination location based on exif info
    if (options.source and options.destination):
        if not (os.path.isdir(options.source) and os.path.isdir(options.destination)):
            raise SystemExit("source and destination must both be directory")
        move_source_to_destination(options.source, options.destination)
        
if __name__ == '__main__':
    main()