

# 查找字符中重复出现次数排第n多的字符列表

def find_n_str(list_txt, n):
    dictory_txt = converson_str(list_txt)
    # 将字符串重组成字典，以出现次数为key,对应value为字符列表
    print(dictory_txt)
    count = 0
    for key in sorted(dictory_txt.keys(), reverse=True):
        count += 1
        if count == n:
            print("出现次数第" + str(n) + "多的字符是" +
                  str(dictory_txt[key]) + ", 对应次数为" + str(key))
            return dictory_txt[key]
    return None

## 测试
def converson_str(list_str):
    # 重组字符串为字典
    marked_str = []     # 筛选标记过的字符
    marked_times = []   # 筛选出现过的次数key
    sort_dictory = {}   # 重组后的字典
    for i in range(len(list_str) - 1):
        _str = list_str[i]
        if _str in marked_str:      # 筛选当前字符是否被标记过
            continue
        else:
            marked_str.append(_str)
            time = 1
        for j in range(i,len(list_str) - 1):
            if _str == list_str[j]:
                time += 1
        # 得到当前研究字符出现的次数

        if time not in marked_times:
            marked_times.append(time)
            sort_dictory[time] = [_str]
        else:
            # 更新字典的value
            update_value = sort_dictory[time]
            update_value.append(_str)
            sort_dictory[time] = update_value

    return sort_dictory


with open("test.txt") as file_object:
    contents = file_object.read()
    result = find_n_str(contents, 1)
