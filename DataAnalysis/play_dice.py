# -*- coding:utf-8 -*-
from random import randint
import numpy as np
import matplotlib.pyplot as plt


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

    def get_num(self, row_numbers):
        results = []
        for i in range(row_numbers):
            result = self.roll()
            results.append(result)

        frequencies = []
        for value in range(1, self.num_sides + 1):
            frequency = results.count(value)
            frequencies.append(frequency)

        return results, frequencies


def play_die_one(num_sides, row_numbers):
    """play one die"""
    while True:
        die = Die(num_sides)
        results, frequencies = die.get_num(row_numbers)

        print(frequencies)

        x = np.arange(1, num_sides + 1)
        plt.bar(x, frequencies)
        plt.xlabel('Results', fontsize=20)
        plt.ylabel('Frequencies', fontsize=20)
        plt.title('Results of rolling one D%s %s times' % (num_sides, row_numbers), fontsize=20)

        plt.show()

        keep_running = input("Make another play? Y/N: ")
        if keep_running in ('N', 'n'):
            print("end...")
            break
        elif keep_running in ('Y', 'y'):
            continue
        else:
            print("输入错误，结束测试")
            break


def play_die_two(num_side1, num_side2, row_numbers):
    """play two die"""

    die1 = Die(num_side1)
    die2 = Die(num_side2)
    results = []
    for i in range(row_numbers):
        result = die1.roll() + die2.roll()
        results.append(result)

    frequencies = []
    for value in range(2, num_side1 + num_side2 + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    num_sides = num_side1 + num_side2
    x = np.arange(2, num_sides + 1)
    plt.bar(x, frequencies)
    plt.xlabel('Results', fontsize=20)
    plt.ylabel('Frequencies', fontsize=20)
    plt.title('Results of rolling one D%s %s times' % (num_sides, row_numbers), fontsize=20)

    plt.show()

    while True:
        keep_running = input("Make another play? Y/N: ")
        if keep_running in ('N', 'n'):
            print("end...")
            break
        elif keep_running in ('Y', 'y'):
            play_die_two(num_side1, num_side2, row_numbers)
        else:
            print("输入错误，结束测试")
            break


if __name__ == '__main__':

    play_die_one(6, 1000)
    play_die_one(8, 1000)
    play_die_two(6, 8, 1000)
