# -*- coding: utf-8 -*-
from datetime import datetime, date, time
from functools import reduce


df = datetime(2011, 10, 29, 20, 39, 6)
print(df)
print(df.date())
print(df.replace(minute=0, second=34))
print(df.time())
print(df.strftime("%m/%d/%Y %H:%M"))
print(datetime.strptime('20011019', '%Y%m%d'))
a = [1,2,3,4]
b = a * 4

print(a[::-1])

s = ['foo', 'bar', 'baz']
mapping = dict((i, v) for i, v in enumerate(s))
print(mapping)

print(sorted('hello world'))

print(sorted(set('hello world')))

s2 = ['one', 'two', 'three']

a = zip(s, s2)

mapping = dict((val, index) for val, index in a)
# mapping = {val: index for val, index in a}
print("mapping")
print(mapping)

print("summary")
a = zip(s, s2)
summary = {}
for i, j in a:
    summary[i] = j

print(summary)

b = [('one', 'kity'), ('two', 'sam'), ('three', 'jule')]

first, last = zip(*b)
print(first)
# print(last)




