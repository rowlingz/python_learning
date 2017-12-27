from math import sqrt
#  回归问题预测模型性能度量


def get_error(target, prediction):
    errors = []
    for i in range(len(target)):
        errors.append(target[i] - prediction[i])

    return errors


# MSE
def get_mean_squared_error(target, prediction):
    errors = get_error(target, prediction)
    square = 0
    for error in errors:
        square += error ** 2

    return square / len(target)


# MAE
def get_mean_absolute_error(target, prediction):
    errors = get_error(target, prediction)
    absolute = 0
    for error in errors:
        absolute += abs(error)
    return absolute / len(target)


# RMSE
def get_squart_mse(target, prediction):
    mse = get_mean_squared_error(target, prediction)
    return sqrt(mse)


# target_variance
def get_variance(target):
    mean = sum(target) / len(target)
    deviation = 0
    for val in target:
        deviation += (val - mean) ** 2

    return deviation / len(target)


# target standard deviation
def get_standard_deviation(target):
    variance = get_variance(target)
    return sqrt(variance)


def get_measures_summary(target, prediction):
    measures = {}
    measures["MSE"] = get_mean_absolute_error(target, prediction)
    measures["RMSE"] = get_squart_mse(target, prediction)
    measures["MAE"] = get_mean_absolute_error(target, prediction)
    measures["target_variance"] = get_variance(target)
    measures["target_standard_deviation"] = get_standard_deviation(target)

    for label, data in measures.items():
        print(label + ": " + str(data))


target = [1.5, 2.1, 3.3, -4.7, -2.3, 0.75]
prediction = [0.5, 1.5, 2.1, -2.2, 0.1, -0.5]

get_measures_summary(target, prediction)
