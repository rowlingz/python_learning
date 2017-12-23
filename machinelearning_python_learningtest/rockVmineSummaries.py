# 从网页上读取统计数据
import urllib.request
import sys

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    #split on comma
    row = str(line.strip()).split(',')
    xList.append(row)

print("Number of Rows of Data = " + str(len(xList)) + '\n')
print("Number of Columns of Data = " + str(len(xList[1])))



