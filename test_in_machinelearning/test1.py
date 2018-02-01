import pandas as pd
import matplotlib.pyplot as plt


sensor_data = pd.read_csv('merged-sensor-files.csv',
                          names=['MTU', 'Time', 'Power', 'Cost', 'Voltage'], header=0)

# print(sensor_data.columns)
print(sensor_data.head())
# print(sensor_data.describe())
# print(sensor_data.info())


# 删除有问题的数据
faulty_row_idx = sensor_data[sensor_data['Power'] == ' Power'].index.tolist()
# print(faulty_row_idx)

sensor_data.drop(faulty_row_idx, inplace=True)
print(sensor_data[sensor_data['Power'] == ' Power'].index.tolist())

# 数据类型转换
sensor_data[["Power", "Cost", "Voltage"]] = sensor_data[["Power", "Cost", "Voltage"]].astype(float)
sensor_data[["Time"]] = pd.to_datetime(sensor_data["Time"])
sensor_data["Hour"] = pd.DatetimeIndex(sensor_data["Time"]).hour
print(sensor_data.dtypes)
print(sensor_data.head())

grouped_sensor_data = sensor_data.iloc[:, 2:].groupby(["Hour"], as_index=False).mean()
print(grouped_sensor_data)

fig = plt.figure(figsize=(13,7))
plt.hist(sensor_data.Power, bins=50)
fig.suptitle('Power Histogram', fontsize = 20)
xmin = sensor_data["Power"].min()
xmax = sensor_data["Power"].max()
plt.xlim(xmin, xmax)
plt.xlabel('Power', fontsize = 16)
plt.ylabel('Count', fontsize = 16)

fig = plt.figure(figsize=(13,7))
plt.bar(grouped_sensor_data.Hour, grouped_sensor_data.Power)
fig.suptitle('Power Distribution with Hours', fontsize = 20)
plt.xlabel('Hour', fontsize = 16)
plt.ylabel('Power', fontsize = 16)
plt.xticks(range(0, 24))
plt.show()
