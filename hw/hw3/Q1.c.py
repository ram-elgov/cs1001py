import math


def f1(lst):
    n = len(lst)
    while n > 0:  # floor(log(n))
        n = n // 2
        for i in range(n):  # depends on the firs loop
            if i in lst:  # O(n+i) = O(n)
                lst.append(i)
    return lst


def f2(L):
    n = len(L)
    res = []
    for i in range(500, n):
        m = math.floor(math.log(i))
        for j in range(m):
            k: int = 1
            while k < n:
                k *= 2
                res.append(k)
    return res
