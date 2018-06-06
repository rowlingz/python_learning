# -*- coding:utf-8 -*-
import numpy as np
import tensorflow as tf
import math
import timeit
import matplotlib.pyplot as plt
import pandas as pd


def generate_data(dimension, num):
    """
    :param dimension: int, 自变量个数
    :param num: int, 样本数
    :return:
    x 自变量； y 因变量
    """
    np.random.seed(1024)

    beta = np.array(range(dimension)) + 1
    x = np.random.random((num, dimension))
    epsilon = np.random.random((num, 1))

    y = x.dot(beta).reshape((-1, 1)) + epsilon

    return x, y


def create_linear_model(dimension):
    """
    搭建模型： 自变量， 因变量， 损失函数
    :param dimension: 自变量个数
    :return:
    model： dict ,包含模型参数（损失函数， 自变量， 因变量）
    """
    np.random.seed(1024)

    # 利用占位符 定义自变量和因变量， 构造出矩阵形式，加快计算速度
    x = tf.placeholder(tf.float64, shape=[None, dimension], name='x')
    y = tf.placeholder(tf.float64, shape=[None, 1], name="y")

    # 定义参数估计值 和 预测值
    beta_pred = tf.Variable(np.random.random([dimension, 1]))
    y_pred = tf.matmul(x, beta_pred, name="y_pred")

    # 定义损失函数
    loss = tf.reduce_mean(tf.square(y_pred - y))

    model = {"loss_function": loss, "independent_variable": x,
             "dependent_variable": y, "prediction": y_pred, "model_params": beta_pred}

    return model


def creat_summary_writer(log_path):
    """
    存储数据到指定路径
    :param log_path: string , 日志存储路径
    :return:
    FileWriter，日志写入器
    """
    if tf.gfile.Exists(log_path):
        tf.gfile.DeleteRecursively(log_path)
    summary_writer = tf.summary.FileWriter(log_path, graph=tf.get_default_graph())
    return summary_writer


def gradient_descent(x, y, model, learning_rate=0.01, max_iter=10000, tol=1.e-6):
    """
    利用梯度下降法训练模型
    :param x: 自变量
    :param y:  因变量
    :param model:  dict 模型参数
    :param learning_rate: 控制”下降速率“
    :param max_iter:  控制”最大迭代次数“
    :param tol:  控制‘是否收敛’
    """

    # 确定最优化算法
    method = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    optimizer = method.minimize(model["loss_function"])

    # 增加日志 tf.summary.scalar()--->存储单个数值型变量（标量）； tf.summary.histogram()--->存储矩阵型变量
    tf.summary.scalar("loss_function", model["loss_function"])
    tf.summary.histogram("params", model["model_params"])
    tf.summary.scalar("first_param", tf.reduce_mean(model["model_params"][0]))
    tf.summary.scalar("last_param", tf.reduce_mean(model["model_params"][-1]))

    # 合并summary类为一个操作
    summary = tf.summary.merge_all()

    # 写入文件
    summary_writer = creat_summary_writer("./logs/gradient_descent_log")

    # 产生初始化参数
    init = tf.global_variables_initializer()

    # 创建session对象，执行tensorflow
    sess = tf.Session()

    # 初始化变量
    sess.run(init)

    # 迭代 梯度下降算法
    step = 0                # 迭代次数
    prev_loss = np.inf      # 初始 损失值
    diff = np.inf           # 初始损失函数的变动

    # 当损失函数的变动小于阈值 或 达到最大循环次数， 停止迭代
    while (step < max_iter) & (diff > tol):
        _, summary_str, loss = sess.run(
            [optimizer, summary, model['loss_function']],
            feed_dict={model['independent_variable']: x,
                       model['dependent_variable']: y}
        )

        # 写入日志
        summary_writer.add_summary(summary_str, step)

        diff = abs(prev_loss - loss)
        prev_loss = loss
        step += 1
    summary_writer.close()
    # print("模型参数： %s" % sess.run(model['model_params']))
    # print("迭代次数： %s" % step)
    # print("损失函数值： %s" % loss)


def stochastic_gradient_descent(x, y, model, learning_rate=0.01,
                                mini_batch_fraction=0.01, epoch=10000, tol=1.e-6):

    method = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    optimizer = method.minimize(model['loss_function'])

    tf.summary.scalar("loss_function", model["loss_function"])
    tf.summary.histogram("params", model["model_params"])
    tf.summary.scalar("first_param", tf.reduce_mean(model["model_params"][0]))
    tf.summary.scalar("last_param", tf.reduce_mean(model["model_params"][-1]))

    # 合并summary类为一个操作
    summary = tf.summary.merge_all()

    # 写入文件
    summary_writer = creat_summary_writer("./logs/stochastic_gradient_descent_log")

    # 产生初始化参数
    init = tf.global_variables_initializer()

    # 创建session对象，执行tensorflow
    sess = tf.Session()

    # 初始化变量
    sess.run(init)

    step = 0
    batch_size = int(x.shape[0] * mini_batch_fraction)
    batch_num = int(math.ceil(1 / mini_batch_fraction))
    prev_loss = np.inf
    diff = np.inf

    while (step < epoch) & (diff > tol):
        for i in range(batch_num):
            batch_x = x[i * batch_size: (i + 1) * batch_size]
            batch_y = y[i * batch_size: (i + 1) * batch_size]

            sess.run([optimizer], feed_dict={model['independent_variable']: batch_x,
                                             model['dependent_variable']: batch_y})

            summary_str, loss = sess.run([summary, model['loss_function']],
                                         feed_dict={model['independent_variable']: x,
                                                    model['dependent_variable']: y})

            summary_writer.add_summary(summary_str, step * batch_num + i)

            diff = abs(prev_loss - loss)
            prev_loss = loss
            if diff <= tol:
                break
        step += 1
    summary_writer.close()
    # print("模型参数： %s" % sess.run(model['model_params']))
    # print("迭代次数： %s" % step)
    # print("损失函数值： %s" % loss)


def compare_with_diff_size():
    """比较两种模型在不同数据量下的 时间"""
    re = []
    dimension = 20
    model = create_linear_model(dimension)
    for i in range(1, 11):
        num = 10000 * i
        x, y = generate_data(dimension, num)

        start_time = timeit.default_timer()
        gradient_descent(x, y, model)
        end_time = timeit.default_timer()

        gd_time = end_time - start_time

        start_time = timeit.default_timer()
        stochastic_gradient_descent(x, y, model)
        end_time = timeit.default_timer()

        sgd_time = end_time - start_time

        re.append([num, gd_time, sgd_time])

    # 运行时间可视化
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    data = pd.DataFrame(re, columns=['num', 'gd_time', 'sgd_time'])
    data = data.set_index('num')
    data.plot()
    plt.show()
    return re


def run():
    """程序入口"""
    # dimension 自变量个数； num 样本数
    dimension, num = 30, 10000

    # 随机产生模型数据
    x, y = generate_data(dimension, num)

    # 定义模型
    model = create_linear_model(dimension)

    # 采用梯度下降法， 估计模型参数
    gradient_descent(x, y, model)
    # 随机梯度下降
    stochastic_gradient_descent(x, y, model)


if __name__ == "__main__":
    run()
    re = compare_with_diff_size()

