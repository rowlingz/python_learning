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


def shell_sort(array):
    """shell排序， 将序列分成若干子序列分别进行直接插入排序"""
    count = len(array)
    sep = 2
    group = count // sep
    while group > 0:
        # i 记录分组数
        for i in range(0, group):
            j = i + group
            # j 记录各分组的索引
            while j < count:
                key = array[j]
                # 进行直接插入排序
                for k in range(j - group, -1, - group):
                    if array[k] > key:
                        array[k + group], array[k] = array[k], key
                j += group
        print(array)
        group //= sep

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
    """直接选择排序，类似冒泡，减少交换次数"""
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


def quick_sort(array, left, right):
    """快速排序， 来源冒泡"""
    # 设定左右两边指针，初始left=0, right=n-1,
    if left >= right:
        return array
    key = array[left]
    # 保留边界值
    start, end = left, right
    while left < right:
        # 右指针，比key大，right-1， 比key小, 将right左移
        while left < right and array[right] >= key:
            right -= 1
        array[left] = array[right]
        # 右指针，比key小，left+1， 比key大，将left右移
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    print(array)
    """
        while left < right:
        # 右指针，比key大，right-1， 比key小，替换left, right
        while left < right and array[right] >= key:
            right -= 1
        array[left], array[right] = array[left], array[right]
        # 右指针，比key小，left+1， 比key大，替换left, right
        while left < right and array[left] <= key:
            left += 1
        array[right], array[left] = array[right], array[left]
    """
    # 对排序后的左右分别进行快速排序
    quick_sort(array, start, left - 1)
    quick_sort(array, right + 1, end)
    return array


def merge_sort(array):
    """归并排序， 递归划分子问题"""
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    """合并两个有序序列"""
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    print(result)
    return result


if __name__ == '__main__':
    array = [5, 3, 8, 6, 4]
    # insert_sort(array)
    # bubble_sort(array)
    # select_sort(array)
    # print(quick_sort(array, 0, len(array) - 1))
    # shell_sort(array)
    merge_sort(array)