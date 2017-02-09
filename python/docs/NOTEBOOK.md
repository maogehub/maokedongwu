#Jupyter Notebook
其实这个就是之前出名的 Ipython Notebook 啦。不过后来分家改名换姓，就叫做 Jupyter Notebook 了。

最近因为工作需要，又要用到 Notebook 来做一些东西（这个画图真的是非常的方便）顺便就说一下如何安装 Jupyter Notebook 吧

## 安装
啥子~~~安装也需要写出来，这个关网不是说的清清楚楚的吗。

安装也有偷懒的方式嘛，鉴于我需要在不同的电脑跑 Notebook，又是不同的环境（python2，python3，linux，苹果）所以当然是用 Docker （容器）最简单了。

[notebook.sh](../src/notebooks/notebook.sh)

~~~bash
#!/bin/bash
notebook_dir=~/notebooks
if [[ ! -d $notebook_dir ]]
then
    mkdir ~/notebook
fi
docker images |grep '^notebooks' >/dev/null 2>&1
notebooks=$?
if [[ $notebooks -eq 0 ]]
then
    docker run --rm -i -t -p 8888:8888 -v $notebook_dir:/opt/notebooks notebooks /bin/bash -c "/opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"
else
    docker pull continuumio/anaconda3
    docker run -i -t -p 8888:8888 -v $notebook_dir:/opt/notebooks continuumio/anaconda3 /bin/bash -c "/opt/conda/bin/conda install -c conda-forge jupyter ipywidgets -y --quiet && pip install jupyter_dashboards && jupyter dashboards quick-setup --sys-prefix && jupyter nbextension enable --py --sys-prefix widgetsnbextension && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"
    docker commit $(docker ps -a|grep "continuumio/anaconda3" | awk '{print $1}') notebooks
    docker rm $(docker ps -a|grep "continuumio/anaconda3" | awk '{print $1}')
fi
~~~

简单的解释一下吧。首先确定我是否有一个叫做 notebooks 说的目录在我的环境下，如果没有，建立这个目录

然后检查一下，我是否有一个叫做notebooks的docker image，如果有的话，那么直接启动这个image，端口映射到8888，属于用完就扔掉的那种（--rm），我会map自己环境目录下的notebooks这个目录到、opt/notebooks，然后运行notebooks

如果我没有notebooks这个images呢，那么就去直接拿anaconda3的官方docker image，然后做一些简单的安装动作，这个可以根据每个人的需要而更改。我目前做的东西，需要 ipywidgets 跟 jupyter_dashboards，另外我需要激活 widgetsnbextension 然后就是跟上面类似的运行notebooks。但是运行结束后，这里会把当前运行的docker container直接commit回去，取名字叫做notebooks（这样下次就不用安装了）然后删除之前的docker（保持用完就扔掉的好习惯）

这样用起来就简单的，直接跑 notebook.sh 就可以给我一个能用的环境了，不管电脑是否有安装过，也不用管是什么系统