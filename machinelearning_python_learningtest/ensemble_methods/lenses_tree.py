# -*- coding:utf-8 -*-
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pydotplus
from IPython.display import Image
import pickle


def creat_tree_model(x_list, y_label, depth):
    """创建决策树模型 训练数据集"""
    model = DecisionTreeClassifier(max_depth=depth)

    model.fit(x_list, y_label)

    return model


def model_visual(tree_model, data_feature_name, data_target, image_name):
    """
    决策树 可视化
    :param tree_model: 训练好的模型
    :param data_feature_name: list, str
    :param data_target: list, str
    :return:
    """
    dot_data = tree.export_graphviz(tree_model, out_file=None, feature_names=data_feature_name, class_names=data_target,
                                    filled=True, rounded=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_png('%s.png' % image_name)  # 保存图像
    Image(graph.create_png())


def store_tree(tree_model, filename):
    with open(filename, 'wb') as fw:
        pickle.dump(tree_model, fw)


def load_model(filename):
    fr = open(filename, 'rb')
    return pickle.load(fr)


if __name__ == '__main__':
    data = pd.read_table('classifierStorage.txt', header=None,
                         names=['age', 'symptom', 'astigmatic', 'tear_production_rate', 'class_'])
    feature = data.columns

    # 替换为数值型变量
    age_dict = {'young': 1, 'pre': 2, 'presbyopic': 3}
    symptom_dict = {'myope': 1, 'hyper': 2}
    astigmatic_dict = {'no': 1, 'yes': 2}
    tear_production_rate_dict = {'reduced': 1, 'normal': 2}
    class_dict = {'hard': 1, 'soft': 2, 'no lenses': 3}
    replace_dict = [age_dict, symptom_dict, astigmatic_dict, tear_production_rate_dict, class_dict]

    for i in range(len(replace_dict)):
        data.iloc[:, i] = data.iloc[:, i].map(replace_dict[i])

    x_list = np.array(data.iloc[:, :-1])
    y_label = np.array(data.iloc[:, -1])

    data_feature_name = feature[:-1]
    # data_target_name = list(data['class_'].unique())
    data_target = list(class_dict.keys())

    model = creat_tree_model(x_list, y_label, 4)
    model_visual(model, data_feature_name, data_target, 'lenses_tree')
    store_tree(model, 'lenses_model.txt')
    mytree = load_model('lenses_model.txt')
    print(mytree)