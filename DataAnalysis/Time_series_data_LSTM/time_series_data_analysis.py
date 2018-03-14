# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.metrics import mean_squared_error
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import LSTM
import math


file_name = "international-airline-passengers.csv"
data = pd.read_csv(file_name, usecols=[1])
data.columns = ['number']
dataset = data.values

dataset = dataset.astype('float32')


def creat_dataset(dataset, look_back=1):
    x, y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        x.append(a)
        y.append(dataset[(i + look_back), 0])

    return np.array(x), np.array(y)


def LSTM_model(dataset):
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform(dataset)

    train_size = int(len(dataset) * 0.67)
    test_size = len(dataset) - train_size
    train, test = dataset[0:train_size, :], dataset[train_size:len(dataset), :]
    look_back = 1
    train_x, train_y = creat_dataset(train, look_back)
    test_x, test_y = creat_dataset(test, look_back)

    train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
    test_x = np.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))

    model = Sequential()
    model.add(LSTM(4, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(train_x, train_y, epochs=100, batch_size=1, verbose=2)

    train_predict = model.predict(train_x)
    test_predict = model.predict(test_x)

    train_predict = scaler.inverse_transform(train_predict)
    train_y = scaler.inverse_transform([train_y])
    test_predict = scaler.inverse_transform(test_predict)
    test_y = scaler.inverse_transform([test_y])

    train_score = math.sqrt(mean_squared_error(train_y[0], train_predict[:, 0]))
    print("Train Score: %.2f RMSE" % (train_score))

    test_score = math.sqrt((mean_squared_error(test_y[0], test_predict[:, 0])))
    print("Test Score: %.2f RMSE" % (test_score))

    train_predict_plot = np.empty_like(dataset)
    train_predict_plot[:, :] = np.nan
    train_predict_plot[look_back: (len(train_predict) + look_back), :] = train_predict

    test_predict_plot = np.empty_like(dataset)
    test_predict_plot[:, :] = np.nan
    test_predict_plot[(len(train_predict) + (look_back * 2) + 1): (len(dataset) - 1), :] = test_predict

    plt.plot(scaler.inverse_transform(dataset))
    plt.plot(train_predict_plot)
    plt.plot(test_predict_plot)
    plt.show()


def get_data(filename):
    # 将读取的数据作为时间序列
    date_parse = lambda dates: pd.datetime.strptime(dates, "%b-%y")         # 指定将输入的字符串转换为可变的时间数据
    data = pd.read_csv(filename, index_col='Month', date_parser=date_parse)
    return data


if __name__ == '__main__':
    # plt.plot(dataset)
    # plt.show()
    # x, y = creat_dataset(dataset)
    # print(x.shape)
    # print('+++++++++++')
    # print(y.shape)

    # data = pd.read_csv(file_name)
    # print(data.head())

    data = get_data(file_name)

    print(data.head())
    print(data.index)

    ts = data['number']
    print(ts[:'2052'])
