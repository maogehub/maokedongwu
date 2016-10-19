#!/usr/bin/python
"""
build new python environment via virtualenv
works on my osx, support osx built-in python
port installed python2.7 and port installed python3.4
"""
import os
import sys
import optparse
import shutil


def main():
    home = os.path.expanduser('~')
    target = os.path.join(home, 'python')
    pythons = { 
            'osx_python2' : '/usr/bin/python',
            'port_python2': '/opt/local/bin/python2.7', 
            'port_python3': '/opt/local/bin/python3.4',
            }
    virtualenv='/usr/local/bin/virtualenv'

    if not os.path.isdir(target):
        try:
            os.mkdir(target)
        except Exception: 
            raise SystemExit("target directory %s do not exist, and I can't make one" %target)
    for python in pythons: 
        if not os.path.isfile(pythons[python]): 
            raise SystemExit("%s not found on: %s" %(python, pythons[python]))
    if not os.path.isfile(virtualenv):
        raise SystemExit("virtualenv not found from: %s" %virtualenv)

    #name do not want people to use in target directory
    #_protected_=['python2', 'python3']
    _protected_=[]

    parser = optparse.OptionParser() 
    parser.add_option('-3', '--python3', action="store_true", dest='python3', default=False, help = "provision python3 instead python2(default)")
    parser.add_option('-o', '--osx', action='store_true', dest='osx', default=False, help = 'use osx python instead of port python. only works for python2')
    parser.add_option('-s', '--system-site-packages', action='store_true', dest='packages', default=False, help = 'Give access to the global site-packages')
    parser.add_option('-p', '--provision', metavar = "Provision", help = "provision new python virtual instance")
    parser.add_option('-l', '--list', action="store_true", dest='list', help = "list provisioned instances")
    parser.add_option('-a', '--active', metavar = 'Active', help="active this virtual python instance")
    parser.add_option('-d', '--delete', metavar = 'Delete', help="delete the virtual python")
    options, args = parser.parse_args()

    if not options.provision and not options.list and not options.active and not options.delete:
        parser.print_help() 
        sys.exit()

    if options.provision: 
        if options.provision in _protected_:
            raise SystemExit("you can not create: %s, this target is protected" %options.provision)
        if os.path.isdir(os.path.join(target, options.provision)):
            raise SystemExit('target %s already exist' %os.path.join(target, options.provision))
        command = ("%s %s" %(virtualenv, os.path.join(target,options.provision)))
        if options.python3: 
            command +=' -p %s' %pythons['port_python3']
        else:
            if options.osx: 
                command +=' -p %s' %pythons['osx_python2']
            else:
                command +=' -p %s' %pythons['port_python2']
        if options.packages: 
            command += ' --system-site-packages'
        os.system(command)
        open(os.path.join(target, options.provision, 'bin/activate'), 'a').write('\n\n[[ -f ~/.python_profile ]] && source ~/.python_profile\n')
        os.system('/bin/bash --init-file %s' %os.path.join(target, options.provision, 'bin/activate'))

    elif options.delete: 
        if options.delete in _protected_:
            raise SystemExit("you can not delete: %s, this target is protected" %options.delete)
        if not os.path.isdir(os.path.join(target, options.delete)): 
            raise SystemExit("%s do not exist" %(os.path.join(target, options.delete)))
        shutil.rmtree(os.path.join(target, options.delete))

    elif options.list:
        dirs=os.listdir(target)
        for d in dirs:
            if d not in _protected_: 
                print '\t', d

    elif options.active:
        if options.active in _protected_:
            raise SystemExit("you can not use: %s, this target is protected" %options.use)
        if not os.path.isdir(os.path.join(target, options.active)):
            raise SystemExit("%s do not exit" %options.use)

        os.system('/bin/bash --init-file %s' %os.path.join(target, options.active, 'bin/activate'))

if __name__=='__main__':
    main()
