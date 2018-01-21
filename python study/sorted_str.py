def sorted_word(a, b):
    n = len(a)
    for i in range(n):
        asc_a, asc_b = ord(a[i]), ord(b[i])
        if asc_a == asc_b:
            continue
        elif asc_a > asc_b:
            return True
        else:
            return False


def sorted_list(str_list):
    n = len(str_list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sorted_word(str_list[i], str_list[j]):
                str_list[i], str_list[j] = str_list[j], str_list[i]

    return str_list


str_list = ['abe', 'ccb', 'Aac', 'bca', 'cfb', 'cba']
print(sorted_list(str_list))
