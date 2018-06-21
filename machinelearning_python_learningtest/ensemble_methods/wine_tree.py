# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from IPython.display import Image
import pydotplus

target_url = "http://archive.ics.uci.edu/ml/machine-" \
             "learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(target_url, header=0, sep=";")
x_list = np.array(data.iloc[:, :-1])
y_label = np.array(data.iloc[:, -1])

# 创建决策树模型 训练数据集
wine_tree = DecisionTreeClassifier(max_depth=3)

wine_tree.fit(x_list, y_label)

with open('wine_tree.dot', 'w') as f:
    f = tree.export_graphviz(wine_tree, out_file=f)


# 可视化决策树
data_feature_name = list(data.columns[:-1])
data_target_name = list(data['quality'].unique())
data_target = [str(i) for i in data_target_name]

dot_data = tree.export_graphviz(wine_tree, out_file=None, feature_names=data_feature_name, class_names=data_target,
                                filled=True, rounded=True, special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('wine.png')         # 保存图像
Image(graph.create_png())

