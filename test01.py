# -----------------------------
# -*- coding: utf-8 -*-
# @Time    : 2022/3/18 11:23
# @Author  : wk！
# @Project : stu_python3.10
# @FileName: test01
# @Software: PyCharm
# -----------------------------

# 学习__call__   装饰器

# class Person:
#     def __init__(self):
#         print("init")
#
#     def __call__(self):
#         print("call")
#
#
# m1 = Person()
# m1()
# m1()
# m1()


# class MyDecorator(object):
#     def __init__(self, f):
#         self.f = f
#         # print(self.f)
#
#     def __call__(self):
#         # print("__call__()...")
#         self.f()
#
#     def wrapped(self):
#         # print(self.f)
#         return self.f()
#
#
# # @MyDecorator
# def hello():
#     print("hello...")
#
#
# new_hello = MyDecorator(hello)
# new_hello()
# new_hello.wrapped()
# hello()


# print(hello)
# hello()
# hello()
# hello()

# def wrapper(base):
#     print("do something")
#     return base
#
#
# @wrapper
# def foo():
#     print("foo")
#
#
# # new_foo = wrapper(foo)
# # new_foo()
# foo()
