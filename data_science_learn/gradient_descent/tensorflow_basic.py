# -*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np

# 构造计算图

# tf.constant()函数构造 常量
a = tf.constant(1, dtype=tf.float32, shape=[1, 1], name="a")
b = tf.constant(2, dtype=tf.float32, shape=[1, 1], name="b")
c = tf.constant(3, dtype=tf.float32, shape=[1, 1], name="c")

s = tf.add(a, b, name="sum")
re = tf.multiply(c, s, name="multiply")


# tf.Variable()函数构造 可变变量
x = tf.Variable(0, name="counter")
one = tf.constant(1)

# 对可变变量赋值
update = tf.assign(x, tf.add(x, one))

# 可变变量初始化
init = tf.global_variables_initializer()


# tf.placeholder()函数  构造占位符变量， 类似函数定义时的参数

# 定义占位符mat1, mat2
mat1 = tf.placeholder(tf.float32, shape=[1, 3], name="mat1")
mat2 = tf.placeholder(tf.float32, shape=[3, 1], name="mat2")

output = tf.matmul(mat1, mat2)

# 创建session 对象，执行计算图
sess = tf.Session()
print(sess.run(s))
print(sess.run(re))
print(sess.run(a))

# 调用可变变量时，首先进行 变量初始化
sess.run(init)
print(sess.run(x))

sess.run(update)
print(sess.run(x))

sess.run(update)
print(sess.run(x))

print(sess.run(
    [output], feed_dict={
        mat1: np.array([1, 2, 3]).reshape(1, 3),
        mat2: np.array([4, 5, 6]).reshape(3, 1)
    }
))