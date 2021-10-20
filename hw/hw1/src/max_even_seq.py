def max_even_seq(n):
    if n == 0:
        return 1
    max_even = 0
    current_even_seq = 0
    while n > 0:
        if n % 2 == 0:
            current_even_seq += 1
            n //= 10
        else:
            if current_even_seq > max_even:
                max_even = current_even_seq
            current_even_seq = 0
            n //= 10
    max_even = current_even_seq if current_even_seq > max_even else max_even
    return max_even


def test():
    if max_even_seq(23300247524689) != 4:
        print("Error in test 1")
    else:
        print(max_even_seq(23300247524689))
    if max_even_seq(0) != 1:
        print("Error in test 2")
    else:
        print(max_even_seq(0))
    if max_even_seq(13579751) != 0:
        print("Error in test 3")
    else:
        print(max_even_seq(13579751))
    if max_even_seq(2468645) != 6:
        print("Error in test 4")
    else:
        print(max_even_seq(2468645))
    if max_even_seq(12121212) != 1:
        print("Error in test 5")
    else:
        print(max_even_seq(12121212))
    if max_even_seq(1089888) != 3:
        print("Error in test 6")
    else:
        print(max_even_seq(1089888))
    if max_even_seq(2) != 1:
        print("Error in test 7")
    else:
        print(max_even_seq(2))
    if max_even_seq(7) != 0:
        print("Error in test 7")
    else:
        print(max_even_seq(7))


test()
