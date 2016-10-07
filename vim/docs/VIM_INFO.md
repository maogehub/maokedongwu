# VIM 
首先，猫哥不想引起任何 VIM VS EMACS 的口水战。各自有个各自的好处。我第一天在电信注册unix账号的时候，当时登陆后，有个选择编辑器的地方，一个是VI，一个是EMACA，当时emac注明是（高级用户）我当然就选择了VI，这个也就是我用VIM的起点。

VIM是我用过最强大的本文编辑软件，而且习惯了vim之后，觉得其他本文编辑软件都不顺手。虽然用vim很多年了，但是大概也就用到vim一半不到的功能。vim自带文档其实很齐全，这里算是一个翻译加注释吧。基本就是把vim的主指令翻译下

写这个的时候，是vim7刚出来的时候写的，新版本中，也许有更多的功能出现。可以看vim的文档，有非常非常详细的介绍

vim中很多东西可以用简称来写，就不用打字那么麻烦了，例如 :edit=:e, :next=:n 这个简称，就大家自己看看吧

## 键盘移动 (Move)
一切都是从键盘移动开始，不是吗

|快捷键|功能|English
|---|---|---|
|k|上| up
j |下| down
h |左| left
l |右| right
z |重画屏幕,当前光标变成屏幕第一行| redraw current line at top of window
CTRL-f || page down
CTRL-b || page up

## 跳跃指令 (Jumps)
跳跃指令类似于游览器中的 <前进> 跟 <后退>

|快捷键|功能|English
|---|---|---|
CTRL-]| 跟着link/tag转入|follow link/tag
CTRL-o |回到上一次jump的地方|go back
CTRL-i|跳去下一个地方|go forward
:ju|显示所有的可以跳跃的地方|print jump list

## 重做/恢复 (Undo & Redo)

|快捷键|功能|English
|---|---|---|
u|撤销|undo
CTRL-r|取消撤销|redo
:undo 2|撤掉到结构的2层|undeo to tree 2
:undolist|显示所有undo列表|show undo list


vim的undo是树结构，你可以回到这个结构中的任意地方

```
          one
           |
        change 1
           |
       c1_change
      /        \
 change 2    change 3
     |          |
 c2_change   c3_change
     |
 change 4
     |
 c4_change
```

## 视觉模式 (visual)

|快捷键|功能|English
|---|---|---|
v|进入视觉模式|enter visual mode
CTRL-v|视觉block编辑|virtual block 

## 打印 (print)

混合视觉模式下（visual）可以选择打印区域。例如用virtual模式选择一定的区域，然后打印这些区域


|快捷键|功能|English
|---|---|---|
:hardcopy|打印vim中的内容|print test
:1,15hardcopy|打印第一行到15行|print lien 1 to 15
:source  $VIMRUNTIME/syntax/2html.vim|文件保存成html格式|save to html $



## 格式 (format)

|快捷键|功能|English
|---|---|---|
:set ff=unix|转换文件为unix格式|set file in unix format
:set ff=dos|转换文件为dos格式|set file in dos format
:set ff?|检查当前文件的格式|check the format of current file

## 加密 (Encryption)

vim 可以给文件直接做简单的加密

vim -x 文件名 输入两次密码后，以后每次打开这个文件，都会要求输入密码才可以

注意的是，vim 处理加密文件的时候，并不会做密码验证。每次打开文件的时候，vim 会直接以你给的密码对本文进行解密。所以如果密码错误，你一样可以“打开”文件，只不过看到的都是乱码（加密后的内容，因为解密失败）

## 语法显示 (Syntax)
|快捷键|功能|English
|---|---|---|
:syntax enable|打开语法的颜色显示|turn on syntax color 
:syntax clear|去掉语法颜色显示|remove off syntax color
:syntax off|关闭语显示功能|turn off syntax
:syntax on|打开语法显示|turn on syntax
:syntax manual|手动设定语法|set the syntax manually

## 特殊字符 (Special Character)
**CTRL-v** 编辑就可以。例如打开vim，进入输入模式，然后输入CTRL-v，你就会看到输入了 **ÿ** 这个字母

## 二进制文件 (Binary File)
vim 是可以显示，编辑二进制文件的。

vim -b 文件名 就会打开文件，以二进制进行编辑

|快捷键|功能|English
|---|---|---|
:set display=uhex|以uhex显示。可以显示正常无法显示的内容，例如控制字符|display in uhex, can display non-display char
:!xxd|更改当前文件显示为二进制|change display to binary
:!xxd -r|更改二进制显示为本文格式|chagne display to text

## 自动完成 (Auto-completion)
vim 本身有自动完成功能（这里只是vim内建的，不是ctag这种外部的）

|快捷键|功能|English
|---|---|---|
CTRL-p|向后搜索自动完成|search backward auto-complete
CTRL-n|向前搜索自动完成|search forward auto-complete
CTRL-x+CTRL-o|自动代码补全|code completion 

## 自动备份 (backup)
vim 可以帮助你自动备份文件（储存的时候，之前的文件做备份）

patch模式下，文件最初的原始文件会被保存下来，不会被复写。举例如下

a.txt 被第一次更改保存的时候，我们保存了 a.txt.org (patch) 跟 a.txt.back （备份）

a.txt 再次被更改保存的时候，我们会覆盖之前的 a.txt.back（备份）但是 a.txt.org 是不变的

a.txt 第三次被更改保存后，我们会再次覆盖之前的 a.txt.back（备份）但是 a.txt.org 仍然不变


|快捷键|功能|English
|---|---|---|
:set backup|开启备份。内建文件名是原文件名前面加个**~**|enable backup, default filename is **~**filename
set backupext=.back|设定备份文件名为：文件名**.backup**|set backup filename as filename**.back**
:set patchmode=.org|保持原始文件名为: 文件名**.org**|set original filename as filename**.org** patch mode


## 开启、保存于退出 (Save & Exit)

|快捷键|功能|English
|---|---|---|
:w|保存文件|write file
:w!|强制保存（覆盖已经存在的文件）| force save (overwrite if file exist)
:q|不保存退出文件| exit without save
:q!|强制退出（不保存，直接退出）|force exit without save
:e filename|打开文件 **filename** | open file **filename** for edit
:e! filename|强制打开文件 **filename** 未保存的东西会丢失|force open file **filename** drop dirty buffer
:saveas filename|另存为 **filename** | save file as **filename**

## 编辑指令 (Edit)

|快捷键|功能|English
|---|---|---|
a |在光表后插入 |append after cursor
A |在一行的结尾插入|append at end of the line
i | 在光标前插入|insert before cursor
I | 在第一个非空白字符前插入|insert before first non-blank
o | 光标下面插入一个新行 |open line below
O | 光标上面插入一个新行 |open line above
x | 删除光标下（或者之后）的东西 |delete under and after cursor
3x | 删除光标下+光标后2位字符 | delete 3 char under and after cursor
X | 删除光标前的字符 |delete before cursor
d | 删除 |delete
dd | 删除一行 | delete line
3dd | 删除3行| delete 3 lines
3dw | 删除3个词 | delete 3 words
J | 将下一行提到这行来 |join line
r | 替换个字符 |replace characters
R | 替换多个字符 |replace mode – continue replace
gr | 不影响格局布置的替换 |replace without affecting layout
c | 跟d键一样，但是删除后进入输入模式 |same as “d” but after delete, in insert mode
S | 删除一行(好像dd一样）但是删除后进入输入模式 |same as “dd” but after delete, in insert mode
s | 删除字符，跟(d)一样，但是删除后进入输入模式 |same as “d” but after delete, in insert mode
s4s | 删除4个字符，进入输入模式 | delete 4 char and put in insert mode
~ | 更改大小写，大变小，小变大 | change case from upper to lower or lower to upper
gu | 变成小写 |change to lower case
guG | 光标当前到文件结尾全部变成小写 |change lower case all the way to the end
gU | 变成大写 |change to upper case
gUG| 光标当前到文件结尾全部变成大写 |change upper case all the way to the end

## 粘贴于复制 (Copy & Paste)

例如我用 **“ayy** 那么在寄存a，就复制了一行，然后我再用 **“byw** 复制一个词在寄存b
粘贴的时候，我可以就可以选择贴a里面的东西还是b里面的，这个就是有很多个复制版

例如 **“ap** 那么就在当前光标下贴出我之前在寄存a中 的内容。**“bP** 就在当前光标上贴出我之前寄存b的内容


|快捷键|功能|English
|---|---|---|
y | 复制 |yank line
yy | 复制当前行 |yank current line
“{a-zA-Z}y | 把信息复制到某个寄存中 |yank the link into register {a-zA-Z}
“*y | 这个是把信息复制进系统的复制版（可以在其他程序中贴出来）|yank to OS buffer
p | 当前光标下粘贴 | paste below
P | 当前光标上粘贴 |paste above
“{a-zA-Z}p | 将某个寄存的内容贴出来 |paste from register
“*p | 从系统的剪贴板中读取信息贴入vim |paste from OS buffer to vim
reg | 显示所有寄存中的内容 |list all registers

## 书签 (Mark)

书签是vim中非常强大的一个功能，书签分为文件书签跟全局书签。文件书签是你标记文件中的不同位置，然后可以在文件内快速跳转到你想要的位置。 而全局书签是标记不同文件中的位置。也就是说你可以在不同的文件中快速跳转

|快捷键|功能|English
|---|---|---|
m{a-zA-Z} | 保存书签，小写的是文件书签，可以用(a-z）中的任何字母标记。大写的是全局 书签，用大写的(A-Z)中任意字母标记。|mark position as bookmark. when lower, only stay in file. when upper, stay in global
‘{a-zA-Z} | 跳转到某个书签。如果是全局书签，则会开启被书签标记的文件跳转至标记的行 |go to mark. in file {a-z} or global {A-Z}. in global, it will open the file
‘0 | 跳转入现在编辑的文件中上次退出的位置 |go to last exit in file
” | 跳转如最后一次跳转的位置 |go to last jump, go back to last jump
‘” | 跳转至最后一次编辑的位置 |go to last edit
g'{mark} | 跳转到书签 |jump to {mark}
:delm{marks} | 删除一个书签 | delete a mark
:delma | 删除了书签 a | delete mark a
:delm! | 删除全部书签 |delete all marks
:marks | 显示系统全部书签 |show all bookmarks


## 标志 (Tag)

|快捷键|功能|English
|---|---|---|
:ta | 跳转入标志 |jump to tag
:ts | 显示匹配标志，并且跳转入某个标志 |list matching tags and select one to jump
:tags | 显示所有标志 | print tag list


## 外部运行命令 (Using External Program)

vim对于常用指令有一些内建，例如wc (算字数）(vim has some buildin functions, such like wc)

|快捷键|功能|English
|---|---|---|
:! | 直接运行shell中的一个外部命令 |call any external program
:!make | 就直接在当前目录下运行make指令了 |run make on current path
:r !ls | 读取外部运行的命令的输入，写入当然vim中。这里读取ls的输出 |read the output of ls and append the result to file
:3r !date -u | 将外部命令date -u的结果输入在vim的第三行中 |read the date -u, and append result to 3rd line of file
:w !wc | 将vim的内容交给外部指令来处理。这里让wc来处理vim的内容 |send vim’s file to external command. this will send the current file to wc command
g CTRL-G | 计算当前编译的文件的字数等信息 |word count on current buffer
!!date | 插入当前时间 |insert current date

## 多个文件编辑 (Edit Multifiles)

vim 可以编辑多个文件，例如
vim a.txt b.txt c.txt 就打开了3个文件

|快捷键|功能|English
|---|---|---|
:next | 编辑下一个文件 |next file in buffer
:next! | 强制编辑下个文件，这里指如果更改了第一个文件 |force to next file in buffer if current buffer changed
:wnext | 保存文件，编辑下一个 |save the file and goto next
:args | 查找目前正在编辑的文件名 | find out which buffer is editing now
:previous | 编辑上个文件 |previous buffer
:previous! | 强制编辑上个文件，同 :next! |force to previous buffer, same as :next!
:last | 编辑最后一个文件 |last buffer
:first | 编辑最前面的文件 |first buffer
:set autowrite | 设定自动保存，当你编辑下一个文件的时候，目前正在编辑的文件如果改动，将会自动保存 |automatic write the buffer when you switch to next buffer
:set noautowrite | 关闭自动保存 |turn autowrite off
:hide e abc.txt | 隐藏当前文件，打开一个新文件 abc.txt进行编辑 |hide the current buffer and edit abc.txt
:buffers | 显示所有vim中的文件 |display all buffers
:buffer2 | 编辑文件中的第二个 |edit buffer 2

## 分屏 (Split)

vim 提供了分屏功能（跟screen里面的split一样）

vim -o file1.txt file2.txt 开启 vim 的时候，就直以分屏编辑两个文件

vim -O file1.txt file2.txt 开启 vim 的时候，竖着分屏编辑两个文件

vimdiff file1.txt file2.txt 或者是 vim -d file1.txt file2.txt

以分屏模式开始两个文件，并且对比显示区别 (diff)


|快捷键|功能|English
|---|---|---|
:split | 将屏幕分成2个 |split screen
:split abc.txt | 将屏幕分成两个，第二个新的屏幕中显示abc.txt的内容 |split the windows, on new window, display abc.txt
:vsplit | 竖着分屏 |split vertically
:{d}split | 设定分屏的行数，例如我要一个屏幕只有20行，就可以下:20split |split the windows with {d} line. 20split: open new windows with 3 lines
:new | 分屏并且在新屏中建立一个空白文件 |split windows with a new blank file
CTRL-w+j/k/h/l | 利用CTRL加w加上j/k/h/l在不同的屏内切换 |switch, move between split screens
CTRL-w+ -/+ | 增减分屏的大小 |change split size
CTRL-w+t | 移动到最顶端的那个屏 |move to the top windows
CTRL-w+b | 移动到最下面的屏 |move to bottom window
:close | 关闭一个分出来的屏 |close splited screen
: only | 只显示光标当前屏 ，其他将会关闭|only display current active screen, close all others
:qall | 退出所有屏 |quite all windows
:wall | 保存所有屏 |write to all windows
:wqall | 保存并退出所有屏 |write and quite all windows
:qall! | 退出所有屏，不保存任何变动 |quite all windows without save

**:diffsplit abc.txt** 如果你现在已经开启了一个文件，想vim帮你区分你的文件跟abc.txt有什么区别，可以在vim中用diffsplit的方式打开第二个文件，这个时 候vim会用split的方式开启第二个文件，并且通过颜色，fold来显示两个文件的区别

这样vim就会用颜色帮你区分开2个文件的区别。如果文件比较大（源码）重复的部分会帮你折叠起来

**:diffpatch filename** 通过 **:diffpatch** 你的patch的文件名，就可以以当前文件加上你的patch来显示。vim会split一个新的屏，显示patch后的信息并且用颜色标明区别。

如果不喜欢上下对比，喜欢左右（比较符合视觉）可以在前面加vert，例如：

**:vert diffsplit abc.txt**

**:vert diffpatch abc.txt**

看完diff，用 **:only** 回到原本编辑的文件，觉 得diff的讨厌颜色还是在哪里，只要用 **:diffoff** 关闭就好了。

还有个常用的diff中的就是 **:diffu** 这个是 **:diffupdate** 的简写，更新用

## TAB

除了split之外， vim 还可以用 tab 

vim -p a.txt b.txt c.txt 就会开启三个tab，分别显示 a.txt b.txt 跟 c.txt

|快捷键|功能|English
|---|---|---|
:tab split filename | 这个就用tab的方式来显示多个文件 |use tab to display buffers
gt | 到下一个tab |go to next tab
gT | 到上一个tab |go to previous tab
0gt |跳到第一个tab |switch to 1st tab
5gt | 跳到第五个tab |switch to 5th tab

当需要更改多个tab中的文件的时候，可以用 **:tabdo** 这个指令 这个就相当于 loop 到你的所有的 tab 中然后运行指令。

例如有5个文件都在tab里面，需要更改一个变量名称：abc 到 def， 就可以用 **:tabdo %s/abc/def/g** 这样所有的5个tab里面的abc就都变成def了


## 折叠 (Folding)

vim的折叠功能。记得应该是6版出来的时候才推出的吧。这个对于写程序的人来说，非常有用。

python 中是以tab作为段落的，所以就可以设定 vim 直接以tab来做折叠(ford by indent)

|快捷键|功能|English
|---|---|---|
zfap | 按照段落折叠 |fold by paragraph
zo | 打开一个折叠 |open fold
zc | 关闭一个折叠 |close fold
zf | 创建折叠 可以用视觉模式，也可以直接给行数等等|create fold. can used in visual mode or giving line number
zr | 打开一定数量的折叠，例如3rz |reduce the folding by number like 3zr
zm | 折叠一定数量（之前你定义好的折叠）| fold by number
zR | 打开所有的折叠 |open all fold
zM | 关闭所有的摺叠 |close all fold
zn | 关闭折叠功能 |disable fold
zN | 开启折叠功能 |enable fold
zO | 将光标下所有折叠打开 |open all folds at the cursor line
zC | 将光标下所有折叠关闭 |close all fold at cursor line
zd | 将光标下的折叠删除，这里不是删除内容，只是删除折叠标记 |delete fold at cursor line
zD | 将光标下所有折叠删除 |delete all folds at the cursor line
:set foldmethod=indent | 设定后用zm 跟 zr 就可以的开关关闭了 |use zm zr


## 保存视果 (Save View)

对于vim来说，如果你设定了折叠，标签，书签等等，但是退出文件，不管是否保持文件，这些东西都会自动消失的。这样来说非常不方便。所以vim给你方法去保存折叠，标签，书签等等记录。最厉害的是，vim对于每个文件可以保存最多10个view，也就是说你可以对同一个文件有10种不同的标记方法，根据你的需 要，这些东西都会保存下来。

|快捷键|功能|English
|---|---|---|
:mkview | 保存记录 |save setting
:loadview | 读取记录 |load setting
:mkview 2 | 保存记录在寄存2 |save view to register 2
:loadview 3 | 从寄存3中读取记录 |load view from register 3

## 常用指令 (Common Commands)

|快捷键|功能|English
|---|---|---|
:set ic |设定为搜索时不区分大小 写 |search case insensitive
:set noic |搜索时区分大小写（内建默认值） |case sensitive (default)
& | 重复上次的”:s” |repeat previous “:s”
. | 重复上次的指令 |repeat last command
K | 在man中搜索当前光标下的词 |search man page under cursor
{0-9}K | 查找当前光标下man中的章节，例如5K就是同等于man 5 |search section of man. 5K search for man 5
:history | 查看命令历史记录 |see command line history
q: | 打开vim指令窗口 |open vim command windows
:e | 打开一个文件，vim可以开启http/ftp/scp的文件 |open file. also works with http/ftp/scp
:e http://www.baidu.com/index.html | 这里就在vim中打开baidu的index.html |open http://www.baidu.com/index.html)
:cd | 更换vim中的目录 |change current directory in vim
:pwd | 显示vim当前目录 |display pwd in vim
gf | 打开文件。例如你在vim中有一行写了#include abc.h 那么在abc.h上面按gf，vim就会把abc.h这个文件打开 |look for file. if you have a file with #include , then the cursor is on abc.h press gf, it will open the file abc.h in vim 

## 记录指令 (Redord)

例子来说明比较容易明白

我现在在一个文件中下**qa**指令,然后输入**itest**然后**ESC**然后**q**
这里**qa**就是说把我的指令记录进**a**寄存，**itest**实际是分2步，**i** 是插入 (insert) 写入的文字是 test 然后用**ESC**退回指令模式**q**结束记录。这样我就把**itest**记录再一个寄存了。
下面我执行**@a**那么就会自动插入test这个词。**@@**就重复前一个动作，等于执行@a

|快捷键|功能|English
|---|---|---|
q{a-z} | 在某个寄存中记录指令 |record typed char into register
q{A-Z} | 将指令插入之前的寄存器 |append typed char into register{a-z}
q | 结束记录 |stop recording
@{a-z} | 执行寄存中的指令 |execute recording
@@ | 重复上次的指令 |repeat previours :@{a-z}


## 搜索 (Search)

vim超级强大的一个功能就是搜索跟替换了。要是熟悉正表达(regular expressions)这个搜索跟后面的替换将会是无敌利器（支持regex的编辑器不多吧）

至于如果用**正表达**就不在这里做介绍了

|快捷键|功能|English
|---|---|---|
\# | 光标下反向搜索关键词 |search the word under cursor backward
* | 光标下正向搜索关键词 |search the word under cursor forward
/ | 向下搜索 |search forward
? | 向上搜索 |search back
% | 查找下一个结束，例如在”(“下查找下一个”)”，可以找”()”, “[]” 还有shell中常用的 if, else这些 |find next brace, bracket, comment or #if/#else/#endif
:help /[] | 特殊的定义的，可以在vim中用用help来看 | everything about special
:help /\s | 普通的也可以直接看一下 | everything about normal


## 替换 (String Substitute)

替换其实跟搜索是一样的。只不过替换是2个值，一个是你搜索的东西，一个是搜索到之后要替换的 string substitute (use regex)

|快捷键|功能|English
|---|---|---|
%s/abc/def/ | 替换abc到def |substitute abc to def
%s/abc/def/c | 替换abc到def，会每次都问你确定|substitute on all text with confirmation (y,n,a,q,l)
1,5s/abc/def/g | 只替换第一行到第15行之间的abc到def |substitute abc to def only between line 1 to 5
54s/abc/def/ | 只替换第54行的abc到def |only substitute abc to def on line 54

## 全局 (Global)

这个不知道怎么翻译，反正 vim 是叫做**global**

这个应该是算做以前ed编辑器的指令吧，如果会会用的话，是个很好用的东西。当然了，别人看到你用可能会觉得“很神奇”

可以对搜索到的东西执行一些vim的命令 (find the match pater and execute a command)

global具体自行方法是 g/pattern/command

|快捷键|功能|English
|---|---|---|
:g/abc/p | 查找并显示出只有abc的行 |only print line with “abc” 
:g/abc/d | 删除所有有abc的行 |delete all line with “abc”
:v/abc/d | 这个会把凡是不是行里没有abc的都删掉 |delete all line without “abc”

## 过滤 (Filter)

vim又一强大功能


|快捷键|功能|English
|---|---|---|
! | 用!就是告诉vim，执行过滤流程 |tell vim to performing a filter operation
!5G | 从光标下向下5行执行过滤程序 |tell vim to start filter under cursor and go down 5 lines
!5Gsort | 从光标下开始执行sort，一共执行5行，就是说我只要sort5行而已 |this will sort the text from cursor line down to 5 lines
!Gsort -k3 | 可以直接代sort的参数，我要sort文字中的第三段 |sort to the end of file by column 3
!! | 值过滤当前的这行 |filter the current line
:.,$!sort | 从当前这行一直执行至文件结束 |sort from current line to end
:.0,$!sort | 从文件的开始第一个行一直执行到文件结束 |sort from start of file to end
:.10,15!sort | 只在文件的第10行到第15行之间执行 |sort between line 10 to 15




