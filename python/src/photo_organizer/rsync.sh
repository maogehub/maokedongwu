#!/bin/bash
source=$HOME/Pictures
targets=$(ls -d /Volumes/*/Pictures 2>/dev/null)
if [[ ! -d $source ]]
then
    echo "$source not found" 1>&2
    exit 1
fi
if [[ -z $targets ]]
then
    echo "no target found" 1>&2
    exit 1
fi

for target in $targets
do 
    if [[ ! -d $target ]] 
    then 
        echo "$target no longer exist... skip " 1>&2
    else
        echo "rsync from $source to $target start" 
        rsync -av $source/* $target/
    fi
done
