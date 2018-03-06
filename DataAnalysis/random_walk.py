# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def random_walk():
    position = 0
    walk = [position]
    steps = 1000
    for i in range(steps):
        draws = np.random.randint(2)
        step = np.where(draws > 0, 1, -1)
        position += step
        walk.append(position)

    plt.plot(walk, 'o-')
    plt.show()


class Randomwalk():
    def __init__(self, num_point=5000):
        """初始化随机漫步的类"""
        # num_point漫步次数
        self.num_point = num_point
        # （x_values, y_values）所漫步的坐标，从（0，0）开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """生成随机漫步包含的点"""

        # 不断漫步，直到漫步的点数为num_point
        while len(self.x_values) < self.num_point:

            # 确定下一个点的方向和沿当前方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 获得下一个点的坐标
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """获取随机漫步的距离和方向"""
        direction = np.random.choice([-1, 1])
        distance = np.random.choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step


def randomwalk(rw):
    while True:
        # 设置画布格式
        # plt.figure(figsize=(12, 10), dpi=128)

        # point_numbers 设置漫步的颜色
        point_numbers = list(range(rw.num_point))
        plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=10)

        # 突出起点和终点
        plt.scatter(0, 0, c='red', edgecolors=None, s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors=None, s=100)

        # 隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)
        plt.show()

        keep_running = input("Make another walk? Y/N: ")
        if keep_running == 'N':
            print("end...")
            break


def pollen_movement(rw):
    point_numbers = list(range(rw.num_point))
    plt.plot(rw.x_values, rw.y_values)
    plt.scatter(0, 0, c='red', edgecolors=None, s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='green', edgecolors=None, s=100)
    plt.savefig('pollen_movement.png')
    plt.show()


if __name__ == '__main__':
    rw = Randomwalk(5000)
    rw.fill_walk()
    # randomwalk(rw)
    pollen_movement(rw)