from threading import Thread, Condition
import time

# cond = Condition()

# def function(name):
#     print('at function -->', name)

# def thread(name):
#     time.sleep(5)
#     function(name)

# t1 = Thread(target=thread,args=['t1'])
# t2 = Thread(target=thread,args=['t2'])

# t1.start()
# t2.start()

dic = {'a':True, 'b':False}
print(dic)

# dic = {x: 0 for x in dic}
# print(dic)

# if 'p' not in dic:
#     dic['p'] = 0

# print('p' in dic)
# print(dic)

# dic = {}

print(all(dic.values()))
