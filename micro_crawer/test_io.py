import sys
# file = open(file = sys.path[0] + '/data/boss.txt', mode='w')
# for i in range(0, 11) :
#     file.write(str(i))
# file.close()
# with open(file = sys.path[0] + '/data/boss.txt', mode='w') as file :
#     file.write('kkkkk\n')
#     file.write('aaa')

with open(file = sys.path[0] + '/data/boss.txt', mode='r', encoding='utf-8') as file :
    list = file.readlines()
    for p in list :
        print(p)