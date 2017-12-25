import pandas as pd
import matplotlib.pyplot as plot

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
abalone_data = pd.read_csv(target_url, header=None, prefix="X")
abalone_data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight',
                        'Shucked weight', 'Viscera weight', 'Shell weight',
                        'Rings']

# print(abalone_data.head())
# print(abalone_data.tail())
#
summary = abalone_data.describe()
print(summary)

abalone_array = abalone_data.iloc[:, 1:9].values
labels = abalone_data.columns[1:9]
plot.boxplot(abalone_array, labels=labels)
plot.xlabel("Attrribute Index")
plot.ylabel("Quartile Ranges")
plot.show()
#
#
# abalone_array = abalone_data.iloc[:, 1:8].values
# labels = abalone_data.columns[1:8]
# plot.boxplot(abalone_array, labels=labels)
# plot.xlabel("Attrribute Index")
# plot.ylabel("Quartile Ranges")
# plot.show()

abalone_data_Normalized = abalone_data.iloc[:, 1:9]
for i in range(8):
    mean = summary.iloc[1, i]
    std = summary.iloc[2, i]
    abalone_data_Normalized.iloc[:, i: (i + 1)] = (abalone_data_Normalized.iloc[:, i: (i + 1)]
                                                   - mean) / std

array_Nor = abalone_data_Normalized.values
plot.boxplot(array_Nor, labels=labels)
plot.xlabel("Attrribute Index")
plot.ylabel("Quartile Ranges_Normalized")
plot.show()