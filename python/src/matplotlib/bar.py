#!/usr/bin/python
import matplotlib.pyplot as plt

def barChart():
    n_groups = 5
    yujie = (5, 3, 3, 4, 8)
    luoli = (1, 2, 1, 2, 4)
    weekday = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    fig, ax = plt.subplots()
    index = [x for x in range(n_groups)]
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = plt.bar(index, yujie, bar_width,
                     alpha=opacity,
                     color='y',
                     error_kw=error_config,
                     label= u'YuJie')
    rects2 = plt.bar([x+bar_width for x in index] , luoli, bar_width,
                     alpha=opacity,
                     color='r',
                     error_kw=error_config,
                     label=u'LuoLi')
    plt.xlabel('Week Days')
    plt.ylabel('Number of Hugs')
    plt.title('YuJie vs LuoLi daily hugging')
    plt.xticks([x+bar_width-0.2 for x in index], weekday)
    plt.legend()
    plt.tight_layout()
    plt.savefig('bar.png')

if __name__ == '__main__':
    barChart()
