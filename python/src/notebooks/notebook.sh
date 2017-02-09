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
