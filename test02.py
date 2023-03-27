# -----------------------------
# -*- coding: utf-8 -*-
# @Time    : 2022/3/18 11:54
# @Author  : wk！
# @Project : stu_python3.10
# @FileName: test02
# @Software: PyCharm
# -----------------------------
# lambda 函数 fms

from functools import reduce

a_list = filter(lambda x: x % 3 == 0, [1, 2, 3])
for i in a_list:
    print(i)

b_list = map(lambda x: x + 1, [1, 2, 3])
for j in b_list:
    print(j)

sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5 - x))

c = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(c)
