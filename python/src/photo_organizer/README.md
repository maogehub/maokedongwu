# Photo Mangement 

## rsync.sh - back up photos to external drive

works on mac or linux where you have $HOME/Pictures

if there's disk mount on /Volumes, and there's folder called "Pictures" script will try to rsync everything to /Volumnes/*/Pictures. works on multi-target

## delete\_raw\_from_jpg.py

giving 2 directory: if base namename in second directory (without .jpg or .xxx) do not exist in the first directory. file will "delete" (moved to .delete directory) 

use case: camera doing both jpg and raw. use jpg for quick reviews, delete anything I don't like. then turn the script, script will delete matching raw files. (file not exist in jpg, will delete from raw)

## exif.py

give filename and return exif info for a file in python dict

## relocate.py (aka default view)
this relocate will move images to target locatioin.
will work on both jpg and raw images 

arrange files in following layout 

```
├── 2015  #年
│   ├── 01 #月
│   │   ├── 01 #日
└── 2016
    ├── 01
    │   ├── 01
    │   ├── 02
    ├── 02
    │   ├── 01
    │   ├── 02
    │   └── 03
    └── 03
        ├── 01
        ├── 02
        └── 03

```

## md5_check.py
return md5 value of the file. will use it to avoid duplicate 

## views 
views are saved metadata. each time can gnerate new view on-fly for "view"

### camera view 
group by camera mode then date time format

### camera len view
group by camera and len

### camera aperture view
group by camera and aperture

### camera iso view
group by camera and iso

### camera shutter speed view 
group by camera and speed

### mixed len view
mixed by len

### mixed aperture view
mixed by aperture

### mixed iso view
mixed by iso

### mixed shutter speed 
mixed by speed 

### black and white 
for black and white  

### flash photo
photo with flash on


## work flow

* all jpgs can exist in single location, for example Pictures/jpg
* all raw can exist in single location, for example Pictures/raw
* review all jpg images by using any image viewer, delete unwanted jpg images
* run delete_raw_from_jpg.py Pictures/jpg Pictures/raw
* rum md5 to de-deplicate 
* run relocate to move pics to correct location
* run all different views 