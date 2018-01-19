#/usr/bin/env python3
# encoding = 'utf-8'
"""
有人问如何画图用中文。也有人问，是否代码可以用中文
这个就当做一个示例吧。不过中文代码（变量）是有点别扭的
这个代码需要 python3 才可以。python2 并不支持中文变量
"""

import matplotlib.font_manager as 字体管理
import matplotlib.pyplot as 绘图

def 御姐萝莉曲线图():
    # 这里使用的是苹果的一个字体的路径。其他系统路径请自行调整
    中文字体 = 字体管理.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
    周几 = ('1','2','3','4','5', '6', '7')
    御姐 = (5, 3, 3, 4, 8, 30, 25)
    萝莉 = (1, 2, 1, 2, 4, 1, 2)

    _ ,御姐萝莉图 = 绘图.subplots()
    御姐萝莉图.plot(周几, 御姐, linewidth=2, label='御姐')
    御姐萝莉图.plot(周几, 萝莉, '--', linewidth=2, label='萝莉')

    御姐萝莉图.legend(loc='upper center', prop=中文字体) #location of line label
    绘图.title('御姐 vs 萝莉 一周中每日拥抱陌生人的次数', fontproperties=中文字体, size='xx-large')
    绘图.xlabel('星期几', fontproperties=中文字体)
    绘图.ylabel('拥抱次数', fontproperties=中文字体)
    绘图.grid(True)
    绘图.savefig("line.png")

if __name__ == '__main__':
    御姐萝莉曲线图()
