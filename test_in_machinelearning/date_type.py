import pandas as pd

sensor_data = pd.read_csv('merged-sensor-files.csv',
                          names=['MTU', 'Time', 'Power', 'Cost', 'Voltage'], header=0)

# 获取数据列表中指定列（usecols）,指定行(nrows)
data = pd.read_csv('merged-sensor-files.csv', usecols=[1, 2], names=['date', 'power'], header=0, nrows=10)

print(data)
print(data.axes)

# 1 to_datetime, set_index
# 把 "date" 列的字符类型数据解析成 datetime 对象。
data['date'] = pd.to_datetime(data['date'])

# 将“date"列设为索引
data.set_index("date", inplace=True)

print("将字符类型转换为datetime对象=================\n")
print(data.axes)
print(data.info())
print(data.index)


# 2 DatetimeIndex
data.index = pd.DatetimeIndex(data['date'])
print("===================")
print(data.axes)
print(data)
# 删除重复列
del data['date']
print("删除重复列\n")
print(data)



