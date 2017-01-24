#/usr/bin/python
import matplotlib.pyplot as plt

def lineChart():
    weekday = (1, 2, 3, 4, 5)
    yujie = (5, 3, 3, 4, 8)
    luoli = (1, 2, 1, 2, 4)

    fig, ax = plt.subplots()
    line1, = ax.plot(weekday, yujie, linewidth=2, label='YuJie') #add dash
    line1, = ax.plot(weekday, luoli, '--',  linewidth=2, label='LuoLi') #add dash

    ax.legend(loc='lower right') #location of line label
    plt.title('YuJie vs LuoLi daily hugging')
    plt.xlabel('Week Days')
    plt.ylabel('Number of Hugs')
    plt.grid(True)
    plt.savefig("line.png")

if __name__ == '__main__':
    lineChart()
