# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


titles = ['received', 'used', 'rate']
columns = ['100-10', '200-20', '300-30', '400-40']
plt.figure(1)
for j in range(1, 4):

    cols = [i for i in range(j, 13, 3)]
    data = pd.read_excel('data1.xlsx', usecols=cols)
    local = '31' + str(j)

    plt.subplot(int(local))

    for i in range(4):
        plt.plot(data.iloc[:, i], 'o-', label=columns[i])
    plt.title(titles[j - 1])
    plt.legend(loc='upper left')
plt.savefig('data1.png')
plt.show()



