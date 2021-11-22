def f1(lst):
    n = len(lst)
    while n > 0:  # floor(log(n))
        n = n // 2
        for i in range(n):  # depends on the firs loop
            if i in lst:  # O(n+i) = O(n)
                lst.append(i)
    return lst




