# Yum VS RPM

平时在QQ群里，另一个我常见的问题，就如何安装套件。很多人不清楚yum跟rpm之间的关系以及区别。

## RPM
rpm是Redhat最早做出来的一种东西，全名是 RedHat Package Manager. 文件以 .rpm 作为结尾。在早期，很多程序都是以源码形式发行的，RedHat就做出了rpm这样一个东西，可以把编译好的文件直接包装，然后安装到目标系统中。rpm本身带了metadata，记录了很多信息，例如包裹中文件的位置，每个文件的大小，验证，还包括包裹是否有依赖关系，等等等等。在早期的时候，这个是一个非常方便的神器。节省了很多人自己编译软件的时间，也避免了很多人不会编译软件的麻烦。但是随着时间的发展，随着linux各种套件的增加，rpm的这些管理功能慢慢的就变得不够用了。例如rpm会很清楚的告诉你包裹有什么依赖，或者跟其他的包裹有什么冲突，可是如何（自动）解决这些依赖，还是需要自己手动的。例如我们需要装一个包裹A，包裹A依赖于包裹B，然后包裹B又依赖于包裹C跟D，然后C跟D又各自依赖E,F, G,H，然后H又依赖包裹A，这样的东西，自己手动解决，是很麻烦的一个事情。

## YUM
Yum是个什么？YUM最早是黄狗linux做出来的东西。（Yellowdog）YUM的前身叫做YUP，全名是yellowdog Updater，后来被整个重写（Modified)得到的新的名字：yellowdog updater modified。Yum是一个可以管理多个rpm的程序，在使用yum安装程序的过程中，yum可以根据rpm的依赖要求，寻找合适的套件（在yum的源中）然后自动解决依赖问题。例如同样的上面包裹A的安装，如果所有的依赖包裹都可以在yum的源中找到（yum可以设定使用多个源），那么yum install A的话，所有的依赖包裹(B,C,D,E,F,G,H）都会被自动安装好。

## 什么时候用RPM什么时候用YUM
最简单的一个规则就是：尽力避免使用rpm指令做安装。rpm一般来说，是作为query（rpm -q）作用为主，例如寻找是否安装了套件A: rpm -q A又或者验证套件是否被更改过：rpm -qV A又或者看看这个套件都安装了些什么在哪里：rpm -ql A再或者看看/bin/cat到底在哪个包裹里面：rpm -qf /bin/cat 至于安装，这个应该交给yum来做。yum在安装的时候可以帮你自动解决依赖的问题，避免手动解决依赖的麻烦

yum从源安装套件非常简单：
yum install 套件名

也可以直接安装本地的rpm:
yum --nogpgcheck localinstall 套件名.rpm

这样套件所有需要的依赖yum就会自动帮你解决掉

如果有很多源，可以通过 --enablerepo=源 名称来控制使用哪个源。例如我有两个epel的源，命名为epel1跟epel2，都是设定为disabled的。那么需要使用epel1的时候，就可以：yum --enablerepo=epel1 insall A

可以通过yum-config-manager --enable 源名字

或者yum-config-manager --disable 源名字

来开启/关闭一个源

## 总结
根据猫哥自身的经验（我靠linux吃饭的）安装软件：尽力避免rpm。只很特殊的时候（例如套件冲突，或者强制不安装依赖）我才有用到rpm指令。正常99.9%以上的时候，安装套件，都是用yum做，不会考虑rpm