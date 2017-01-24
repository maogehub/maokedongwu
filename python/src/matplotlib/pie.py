#!/usr/bin/python
import matplotlib.pyplot as plt

def pieChart():
    yujie = (5, 3, 3, 4, 8)
    weekday = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
    fig1, ax1 = plt.subplots()
    ax1.pie(yujie, explode=[0, 0, 0, 0, 0.1], labels=weekday, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig('pie.png')

if __name__ == '__main__':
    pieChart()
