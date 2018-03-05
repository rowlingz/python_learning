# 温习排序算法


def insert_sort(array):
    """插入排序"""
    count = len(array)
    for i in range(1, count):
        key = array[i]
        print("交换" + str(key))
        for j in range(i - 1, -1, -1):
            # 将key插入到前端已排序好的数组中，从后往前比，key值处于j+1的位置，遇大替换，遇小跳出。
            if key < array[j]:
                array[j + 1] = array[j]
                array[j] = key
            else:
                break
        print(array)
    print("end")
    print(array)
    return array


def bubble_sort(array):
    """冒泡排序"""
    count = len(array)
    for i in range(count):
        for j in range(count - 1, i, -1):
            # 从后往前冒泡，将最小的放置在最前方，一次冒泡完成，j的遍历范围为[count -1 , i]
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    print("end", array)
    return array


def select_sort(array):
    """直接选择排序"""
    count = len(array)
    for i in range(count):
        min_index = i
        for j in range(i + 1, count):
            # 从待排序中找出最小的值后，与list[i]交换
            if array[min_index] > array[j]:
                min_index = j
        print("最小值", array[min_index])
        array[i], array[min_index] = array[min_index], array[i]
    print("end", array)
    return array





if __name__ == '__main__':
    array = [5, 3, 8, 6, 4]
    # insert_sort(array)
    # bubble_sort(array)
    select_sort(array)