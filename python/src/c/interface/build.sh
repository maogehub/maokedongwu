if [[ $(uname) == "Darwin" ]]
then
    #osx build 
    gcc -I /Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/ -c add.c 
    gcc -shared -lpython -o add.so add.o
else 
    #linux (fedora) build 
    gcc -I /usr/include/python2.7 -fPIC -c add.c 
    gcc -shared -o add.so add.o
fi
