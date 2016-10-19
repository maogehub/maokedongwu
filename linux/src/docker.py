#!/usr/bin/python
"""
run docker container for my daily work

files needs to map:
    .vimrc
    .screenrc
    .ssh/id_rsa

directory needs to map:
    /tmp
    $(pwd)

extra help files:
    ~/.docker/config/$image.sh

type of container :
    adhoc: -ti --rm image bash
    saved: -ti --name=image
        if image.local exist?
            yes: docker run -ti --name=image.local image.local bash
            no:  docker run -ti --name=image.local image bash
        docker commit name name
        docker rm name
"""

import sys
import os
import subprocess
import shlex
import optparse

MAPPINGS = [
        (os.path.expanduser('~/.vimrc'), '/root/.vimrc'),
        (os.path.expanduser('~/.screenrc'), '/root/.screenrc'),
        (os.path.expanduser('~/.ssh/id_rsa'), '/root/.ssh/id_rsa'),
        (os.getcwd(), '/workspace'),
        ('/tmp', '/tmp'),
        ]

def build_commands(image, adhoc=True):
    """build docker command(s) for adhoc and saved container
    """
    parameters = {
            'name': '%s.local' %image,
            'mapping': '',
            'image': image,
            'command': 'bash',
            }
    #build mappings
    for target in MAPPINGS:
        if not os.path.exists(target[0]):
            continue
        parameters['mapping'] += '-v %s:%s ' %target

    #some extra file that I use for help. based on image name
    helper_file = os.path.join(os.path.expanduser('~/.docker/config'), '%s.sh' %parameters['image'])
    if os.path.isfile(helper_file):
        parameters['mapping'] += '-v %s:/%s' %(helper_file, os.path.basename(helper_file))

    #ADHOC (--rm) command
    if adhoc:
        return ['docker run -ti --rm %(mapping)s %(image)s %(command)s' %parameters]

    #SAVED (--name) commands
    #check if we have local saved image
    image = subprocess.check_output(shlex.split("docker images -q %(image)s.local" %parameters))
    if image:
        parameters['image'] = '%s.local' %parameters['image']
    saved =  []
    saved.append('docker run -ti --name=%(name)s %(mapping)s %(image)s %(command)s' %parameters)
    saved.append("docker commit %(name)s %(name)s" %parameters)
    saved.append("docker rm %(name)s" %parameters)
    return saved

def parse_args():
    """parse args and reutrn commands from build_commands()
    """
    parser = optparse.OptionParser(usage='usage: %prog docker_image [options]', version='%prog 1.0')
    parser.add_option('-k', '--keep', action = 'store_true', help='keep the container (save after exit)')
    (options, args) = parser.parse_args()

    if not args:
        parser.print_help()
        raise SystemExit()

    adhoc = True
    image = args[0]
    if options.keep:
        adhoc = False
    return build_commands(image, adhoc)

def exec_commands(commands):
    """ run commands
    if the exit code of any command is not zero. stop
    """
    for command in commands:
        rt = subprocess.call(shlex.split(command))
        if rt !=0: return

def main():
    commands = parse_args()
    exec_commands(commands)

if __name__ == '__main__':
    main()
