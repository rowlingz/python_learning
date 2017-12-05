import json

# 读取用户喜欢的数字：
# 先查询喜欢的数字（get_favorite_number()）
# 如果存在，直接输出；如果不存在，提示用户输入新的数字（get_new_number()）


def show_favorite_number():
    number = get_favorite_number()
    if number:
        print("I know your favorite number! It's " + str(number) + ".")
    else:
        number = get_new_number()
        print("I had save your favorite number!" )


def get_favorite_number():
    # 加载用户存储内容
    file_name = 'favorite_number.json'
    try:
        with open(file_name) as fi_obj:
            content = json.load(fi_obj)
    except FileNotFoundError:
        return None
    else:
        return content


def get_new_number():
    # 提示用户输入内容并存储
    number = input("please input your favorite number: ")
    file_name = 'favorite_number.json'
    with open(file_name, 'w') as fi_obj:
        json.dump(number, fi_obj)
    return number


show_favorite_number()