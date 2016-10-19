# Linux 不常用指令

不常用就是说我还是会用到，但是因为并不是常常用，所以容易忘记。这里的东西会看上去很杂乱。

## hyper-thrading
这个不算指令了，不过还是需要用。

每次找cpu很是麻烦，要去看哪些跟哪些是实际在同一个core上，哪些有是在不同的cpu上

同一个core的，两个线程，等于还是两个线程在共用一个core的运算（所以有时候要避免）

不同cpu那么就不能共用L2的cache，就会多出context switch等等不必要的功耗

~~~python
#!/usr/bin/python
import commands
physical=commands.getoutput(“cat /proc/cpuinfo |grep ‘physical id'”).split(‘\n’)
core=commands.getoutput(“cat /proc/cpuinfo |grep ‘core id'”).split(‘\n’)
processor=commands.getoutput(“cat /proc/cpuinfo |grep processor”).split(‘\n’)
CPU={}
for x in range(len(processor)):
if not CPU.has_key(physical[x].split()[-1]):
CPU[physical[x].split()[-1]]={}
if not CPU[physical[x].split()[-1]].has_key(core[x].split()[-1]):
CPU[physical[x].split()[-1]][core[x].split()[-1]]=[]
CPU[physical[x].split()[-1]][core[x].split()[-1]].append(processor[x].split()[-1])
for x in CPU.keys():
for y in CPU[x].keys():
print ‘CPU %s, core %s, id %s’ %(x, y, CPU[x][y])
print ”
~~~

## mutt 发送html邮件

~~~bash
mutt -e set content_type=text/html” -s “subject ” email@address.com < html_file
~~~

html中的image可以用cid的tag，这个tag可以直调用attachments里面的图片

```
<font size=4 color=black><center>%s</center>
</font><p><img src=”cid:file_name”</img><p>
```

例如产生以下html保存为xyz.mutt

```
<font size=6 color=blue><center>test </center></font><p><p>
<font size=4 color=black><center>test 1</center></font><p><img src=”cid:test_1.png”</img><p>
<font size=4 color=black><center>test 2</center></font><p><img src=”cid:test_2.png”</img><p>
<font size=4 color=black><center>test 3 </center></font><p><img src=”cid:test_3.png”</img><p>
<font size=4 color=black><center>test4 </center></font><p><img src=”cid:test_4.png”</img><p>
```

那么用muttl的时候加入如下的那些图片，就可以直接在outlook中显示出来（embedded）而不是以附件的形式出现

~~~bash
mutt -e set content_type=text/html” -s “subject ” email@address.com -a test_1.png -a test_2.png -a test_3.png -a test_4.png < html_file
~~~

outlook 本身不支持 base64直接做embedded （firefox家的就没有问题）

如果直接做base64的嵌入，用法如下

```
<html>
<font size=4 color=red><center>this is a test</font></center>
<p>
<center>
<img src=”data:image/gif;base64,R0lGODlhIAAgAPf+AAAAAFUAAIAAAKoAANUAAP8AAAArAFUrAIArAKorANUrAP8rAABVAFVVAIBV
AKpVANVVAP9VAACAAFWAAICAAKqAANWAAP+AAACqAFWqAICqAKqqANWqAP+qAADVAFXVAIDVAKrV
ANXVAP/VAAD/AFX/AID/AKr/ANX/AP//AAAAVVUAVYAAVaoAVdUAVf8AVQArVVUrVYArVaorVdUr
Vf8rVQBVVVVVVYBVVapVVdVVVf9VVQCAVVWAVYCAVaqAVdWAVf+AVQCqVVWqVYCqVaqqVdWqVf+q
VQDVVVXVVYDVVarVVdXVVf/VVQD/VVX/VYD/Var/VdX/Vf//VQAAgFUAgIAAgKoAgNUAgP8AgAAr
gFUrgIArgKorgNUrgP8rgABVgFVVgIBVgKpVgNVVgP9VgACAgFWAgICAgKqAgNWAgP+AgACqgFWq
gICqgKqqgNWqgP+qgADVgFXVgIDVgKrVgNXVgP/VgAD/gFX/gID/gKr/gNX/gP//gAAAqlUAqoAA
qqoAqtUAqv8AqgArqlUrqoArqqorqtUrqv8rqgBVqlVVqoBVqqpVqtVVqv9VqgCAqlWAqoCAqqqA
qtWAqv+AqgCqqlWqqoCqqqqqqtWqqv+qqgDVqlXVqoDVqqrVqtXVqv/VqgD/qlX/qoD/qqr/qtX/
qv//qgAA1VUA1YAA1aoA1dUA1f8A1QAr1VUr1YAr1aor1dUr1f8r1QBV1VVV1YBV1apV1dVV1f9V
1QCA1VWA1YCA1aqA1dWA1f+A1QCq1VWq1YCq1aqq1dWq1f+q1QDV1VXV1YDV1arV1dXV1f/V1QD/
1VX/1YD/1ar/1dX/1f//1QAA/1UA/4AA/6oA/9UA//8A/wAr/1Ur/4Ar/6or/9Ur//8r/wBV/1VV
/4BV/6pV/9VV//9V/wCA/1WA/4CA/6qA/9WA//+A/wCq/1Wq/4Cq/6qq/9Wq//+q/wDV/1XV/4DV
/6rV/9XV///V/wD//1X//4D//6r//9X//z8/P2tra5WVlcDAwP///yH5BAEAAP4ALAAAAAAgACAA
AAjTAP0JHEhQIICDCA8WXMhwIMIUECNCRNiw4UGJGDEqrOgwo0eNHP0B+EgyIoCKI0uqPLkw5USX
JC+aLAhzpMyPF2sShGmSZ0+PLEXizDkxxUOgBoEC+HfT6EGmSIVmTDj1KEifP5XGxKqya9OuYJ2G
HSuWLNivZoem9erTZsK3VNtKlSgTgIACAAroTYmWZVuTd/PuLTo1KU4BgfX+wxuzI9C7eBUzjmp4
KmTBgylXpntZMtagOx/vzQzSomjSdEN+tpo6pEiuVV3vRPsStOzZcF0HBAA7″ </img>
</center>
</html>
```

## 改变进程的cpu

~~~bash
taskset – retrieve or set a process’s CPU affinity
~~~

## ps 指令 

看到线程

~~~bash
ps H -eo user,pid,ppid,pcpu,ni,pmem,vsize,rss,nlwp,pri,rtprio,stat,psr,comm
~~~

另一个ps指令
~~~bash
ps -eo stat,euid,ruid,tty,tpgid,sess,pgrp,ppid,pid,pcpu,policy,nice,pri,psr,sgi_p,utime,stime,minflt,majflt,wchan:14,args
~~~

## postgresql query

postgresql 里面的一个query. table mytable里面的column: mycolumn 这里假设是varchar的

需要的是用mycolumn里面的值对比自己输入的值，并且返回最match的一个。

~~~sql
select mycolumn from mytable where position(mycolumn in (cast(‘%s’ as varchar)))=1 order by length(mycolumn) desc limit 1″ %my_string
~~~

## curl 带 auth

~~~bash
HTML=$($CURL -d “j_username=$users_login&j_password=$users_password” -L $URL 2>/dev/null)
~~~

## 改变硬盘读写方式

~~~bash
cat /sys/block/cciss\!c0d0/queue/scheduler
noop anticipatory [deadline] cfq
~~~

## process group

~~~bash
getpgid (2)          – set/get process group
getpgrp (2)          – set/get process group
killpg (2)           – send signal to a process group
setpgid (2)          – set/get process group
setpgrp (2)          – set/get process group
setsid (2)           – creates a session and sets the process group ID
tcgetpgrp (3)        – get and set terminal foreground process group
tcsetpgrp (3)        – get and set terminal foreground process group
~~~

## vim 去掉空行 (remove empty line)

```
:%s/^[\ \t]*\n//g

或者
:v/./d
```

## wireshark 

rtp 分析

~~~bash
#capture only udp
#-a duration:10 set to only capture 10 seconds
#-o rtp.heuristic_rtp:TRUE to decode anything as rtp
#-s 65: only capture 65 (header)
#-q quite
#-z : Collect statistics for all RTP streams and calculate max. delta, max. and mean jitter and packet loss percentages

$ tshark udp -a duration:10 -s 65 -o rtp.heuristic_rtp:TRUE -q -z rtp,streams

~~~

抓协议（sip）中的不同的filed （根据callerani）
~~~bash
tshark -i bond0 -d udp.port==5060,sip -T fields -e sip.Contact -e sdp.media.port -e sip.Status-Code -e sdp -R “sip.Status-Code==200 and sdp and sip.from.addr contains 123456789”
~~~

## bash 

语法检查

~~~bash
/bin/bash -n $0 2>&-
~~~

replace 

ls abc 替换成 cd abc

~~~bash
^ls^cd
~~~

~~~bash
test='try to replace it'
echo ${test/replace/xxx}
try to xxx it
~~~

vi 模式下

~~~
fc #fix command
~~~

history ignore

~~~
export HISIGNORE=' '

history will ignore anything start with space
~~~

change real time priority 

~~~bash
chrt -f 90 process
~~~

use python in bash 

~~~bash
for i in $(seq 1 10); do echo $i.txt | python -c "print str(raw_input())[:-3]"; done
~~~

super pipe

~~~bash
file=$(mktmp)
tail -f /var/log/messages > $file &
PID=$(echo $!)
grep xxx $file &
PPID=$(echo $!)
~~~


## 检查 dns

~~~bash
scutil --dns
~~~

## 检查 binary 都有depends哪些rpm

~~~bash
#/bin/bash
[[ -f $1 ]] || exit 1;
for x in $(ldd $1 |grep '='|grep -v 'linux-gate.so.1'|awk -F '>' '{print $2}'|awk -F '(' '{print $1}'); do rpm -qf $x; done|sort -u|awk -F '-' '{print $1}'
~~~

## demsg 开启时间

~~~bash
rhel6
[[ -f /sys/module/printk/parameters/time ]] && echo 1 > /sys/module/printk/parameters/time

rhel5
/sys/module/printk/parameters/printk_time
~~~

## oprofile

~~~bash
opcontrol --init

opcontrol --setup --vmlinux=/usr/lib/debug/lib/modules/$(uname -r)/vmlinux --event=CPU_CLK_UNHALTED:1600000:0:1:1 --separate=library
#or
opcontrol --setup --vmlinux=/usr/lib/debug/lib/modules/`uname -r`/vmlinux --event=GLOBAL_POWER_EVENTS:750000:0x1:1:1 --separate=library

opcontrol --start

opcontrol --shutdown

#Collect the output of

opreport -t 4 --long-filenames
opreport -t 1 -l /usr/lib/debug/lib/modules/`uname -r`/vmlinux
~~~

## ssh

tunnel 
~~~bash
tunnel X for 2 host: (use host.a jump to host.b)

localhost->host.a->host.b

terminal 1:
ssh host.a -L2200:host.b:22

terminal 2:
ssh localhost -XYC -p 2200
~~~

dd 

~~bash
dd if=/dev/sda | gzip -1 - | ssh user@hostname dd of=image.gz

ssh user@hostname dd if=image.gz | gunzip -1 - | dd of=/dev/sda
~~~




