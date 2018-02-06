# 温习数据结构


def sequential_search(lis, key):
    """顺次查找"""
    length = len(lis)
    for i in range(length):
        if lis[i] == key:
            return i
    return False


def binary_search(lis, key):
    """二分查找：取中间元素与目标值比较"""
    low = 0
    high = len(lis) - 1
    time = 0
    while low <= high:
        time += 1
        mid = (high + low) // 2
        if lis[mid] == key:
            print("time: " + str(time))
            print("index: " + str(mid))
            return True
        elif lis[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


def insert_search(lis, key):
    """插值查找：二分查找的进化，将mid 修改目标值在数组中的相对位置"""
    low = 0
    high = len(lis) - 1
    time = 0
    while low <= high:
        time += 1
        mid = low + (high - low) * (key - lis[low]) // (lis[high] - lis[low])
        if lis[mid] == key:
            print("time: " + str(time))
            print("index: " + str(mid))
            return True
        elif lis[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_search(lis, key):
    low, high = 0, (len(lis) - 1)
    k = 0
    # 确定K值
    while len(lis) > fibonacci(k) - 1:
        k += 1

    while len(lis) < fibonacci(k) - 1:
        lis.append(lis[high])
    print(k)

    time = 0
    while low <= high:
        time += 1
        mid = low + fibonacci(k - 1) - 1
        if key == lis[mid]:
            print("time: " + str(time))
            print("index: " + str(mid))
            return True
        elif key < lis[mid]:
            high = mid - 1
            k = k - 1
        else:
            low = mid + 1
            k = k - 2
    return False


if __name__ == '__main__':
    args = [1, 5]
    print(range(*args))

    foo = lambda x: x + 1
    print(foo(2))

    a = [1, 4, 6, 8]
    b = [i for i in a if i > 2]
    c = map(lambda i: i + 3, a)

    print(b)
    print(c)

    for index, item in enumerate(c):
        print(index, item)

    a = [1, 4, 6, 8]
    print(insert_search(a, 8))
    print(binary_search(a, 8))
    print(fibonacci_search(a, 1))