# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     understand-iterator
   Description：
   Author :       stephen
   date：          2019/6/3
-------------------------------------------------
   Change Activity:
                   2019/6/3:
-------------------------------------------------
"""
# 懒执行 (lazy evalution)
import time

id = 0
def get_img_by_id(id):
    # time-consuming
    time.sleep(id)
    return id

def generate_id():
    global id
    id += 1
    return get_img_by_id(id)

# print(generate_id())
# print(generate_id())
# print(generate_id())

# 类实现

class ImageGeneretor:
    def __init__(self):
        self.id = 0

    def get_img_by_id(self):
        self.generate_id()
        time.sleep(self.id)
        print(self.id)
        return self.id

    def generate_id(self):
        self.id += 1
#
# iG = ImageGeneretor()
# iG.get_img_by_id()
# iG.get_img_by_id()

# iterator
# use __iter__ and __next__
class ImageGeneretor1:
    def __init__(self):
        self.id = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.id += 1
        return self.get_img_by_id()

    def get_img_by_id(self):
        time.sleep(self.id)
        print(self.id)
        return self.id

# for im in ImageGeneretor1():
#     pass

# genrator

def image_generator2():
    id = 0
    while id < 3:
        id+=1
        yield get_img_by_id(id)

# for img in image_generator2():
#     print(img)

# fibonacci generator 写法
def fibonacci():
    a, b = (0, 1)
    while True:
        yield a
        time.sleep(1)
        a, b = b, a+b
# for f in fibonacci():
#     print(f)
#
# fibos = fibonacci()
# next(fibos) #=> 0
# next(fibos) #=> 1
# next(fibos) #=> 1
# next(fibos) #=> 2

# Fibonacci iterator 写法
class Fibonacci:
    def __init__(self):
        self.a, self.b = (0,1)

    def __iter__(self):
        return self

    def __next__(self):
        res = self.a
        self.a, self.b = self.b, self.b+self.a
        time.sleep(1)
        return res

# for fi in Fibonacci():
#     print(fi)
#     pass
# Fi = Fibonacci()
# print(Fi)
#
# print(next(Fi))
# print(next(Fi))
# print(next(Fi))
# print(next(Fi))

# 理解Generator
def generator():
    print('before')
    yield  'test'         # break 1
    print('middle')
    yield            # break 2
    print('after')

# x = generator()
# print(next(x))
# next(x)
# next(x)

# yield 传值

def get_average():
    score_sum = 0
    num = 0
    while True:
        score_sum += yield score_sum/num if num != 0 else 0
        num += 1

# ave = get_average()
#
# print(ave.send(None))
# print(ave.send(99))
# print(ave.send(20))

# yield from
def odds(n):
    for i in range(n):
        if i % 2 == 1:
            yield i

def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# def odd_even(n):
#     for x in odds(n):
#         yield x
#     for x in evens(n):
#         yield x
# =>
def odd_even(n):
    yield from odds(n)
    yield from evens(n)

for x in odd_even(6):
    print(x)


