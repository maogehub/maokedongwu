# 运行 Docker

基本我每天的东西都是在docker下面做。那么当然需要一些简化的东西来然我可以使用docker。例如我经常需要跑centos的环境的话，我不可能每次都跑

~~~bash
docker run -ti --rm -v 我要的_volume centos bash
~~~

这个是很麻烦的事情。首先说说我常用的东西

* 我的每个docker都要带我系统的.vimrc过去，没有这个用不惯
* 我的每个docker也要带我的.screenrc过去，跟上面同理
* 我的每个docker我都会带我自己机器的ssh钥匙进去，方便我ssh其他机器
* 我一般需要做东西，都是在docker做，不是在自己电脑，所以我“当前目录"都是一定要带进去的
* 我一般会除了当前目录，把tmp带进去，这样可以有个交换空间，另外很多东西可以吧pipe，unix socket丢在/tmp
* 我一般常用的vm都会有个小的shell脚本，定义一些我长要做的东西（例如安装软件，设定环境什么的）
* 我跑docker一半分2种情况，一种是用完就丢掉的，一种是用完保存的

这里给一个例子，我需要跑一个centos7的docker，用完之后需要保存，那么我需要输入以下命令（这里假设我的当前目录是在/var/log）

~~~bash
docker run -ti --name=centos.local -v /Users/maoge/.vimrc:/root/.vimrc -v /Users/maoge/.screenrc:/root/.screenrc -v /Users/maoge/.ssh/id_rsa:/root/.ssh/id_rsa -v /private/var/log:/workspace -v /tmp:/tmp -v /Users/maoge/.docker/config/centos.sh:/centos.sh centos bash
docker commit centos.local centos.local
docker rm centos.local
~~~

我这么懒得人，不可能每天打上面的指令几十遍吧

[docker.py](../src/docker.py)

~~~python
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
~~~


