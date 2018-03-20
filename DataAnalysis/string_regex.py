# -*- coding:utf-8 -*-
# 正则表达式regex
import re

pattern = re.compile('hello')

match = pattern.match('hello world')


regex = re.compile(r'\d+')
text = "one1two2three3four4"

text_split = regex.split(text)

text_findall = regex.findall(text)


# . 匹配任意字符，+ 匹配1—多次
key = r"<h1>hello world<h1>"
p = r"<h1>.+<h1>"
pattern1 = re.compile(p)
result = pattern1.findall(key)

# \转义符
key = r"afiouwehrfuichuxiuhong@hit.edu.cnaskdjhfiosueh"
p = r".+@hit\.edu\..+"


# * 匹配前一个字符0——多次
key = r"http://www.nsfbuhwe.com and https://www.auhfisna.com"
p = r"https*://"


# []匹配内部任一个字符
key = r"lalala<hTml>hello</Html>heiheihei"
p = r"<[hH][tT][mM][lL]>.+</[hH][tT][mM][lL]>"


# [^p] 除p以外的匹配
key = r"mat cat hat pat"
p = r"[^p]at"


# 懒惰性匹配
key = r"chuxiuhong@hit.edu.cn"
p = r"@.+\."
p1 = r"@.+?\."

# 匹配前一个字符的次数
key = r"saas and sas and saaas"
p = "sa{1,2}s"


# 子表达， 将几个字符的组合形式看作一个大的z字符

p = "(\d+{1,3}\.){3}\d"

# 向前向后查找 ?<=    ?=
key = r"<html><body><h1>hello world</h1></body></html>"
p = r"(?<=<h1>).+?(?=</h1>)"


# 回溯引用 \1, \2代表第一个/第二个子表达式
key = r"<h1>hello world</h3>"
p = r"<h([1-6])>.*?</h\1>"


if __name__ == "__main__":
    # if match:
    #     print(match.group())
    # else:
    #     print('None')

    # pattern1 = re.compile(p)
    # result = pattern1.findall(key)
    # print(result)

    pattern = re.compile(p)
    matcher = re.search(pattern, key)
    if matcher:
        print(matcher.group(0))
    else:
        print('None')





