import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = [1,2,3,4]
    y = [3,2,4,5]
    y1=[1,2,4,2]
    plt.figure('click')
    plt.plot(x,y,label='y')
    plt.scatter(x,y,c='r',marker='*')
    plt.plot(x,y1,label='y1')
    plt.scatter(x,y,c='b',marker='*')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('title')
    plt.plot()
    plt.show()
