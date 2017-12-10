# formatting string 字符串格式化

# 1. 格式化操作符（%）
# 1.1 python自带的内置格式（%s, %d）
admin = ('liy', 'china', 14)

s = "he's name is %s, and born in %s. the age is %d. " % admin

print(s)

# 1.2 利用字典传递真实值
message = {'name': 'kity', 'place': 'china', 'age': 14}
t = "he's name is %(name)s, and born in %(place)s. the age is %(age)d."
print(t % message)

# 1.3 浮点数格式符（%f）
price1 = "Today's stock price: %f" % 54.789
# %f 十进制输出，保留小数点后6位

price2 = "Today's stock price: %.2f" % 54.789
# %.2f .2 指定小数点输出后2位

price3 = "Today's stock price: %+f" % 54.789
# %+f  + 正数前输出加号（+）
print(price1)
print(price2)
print(price3)

