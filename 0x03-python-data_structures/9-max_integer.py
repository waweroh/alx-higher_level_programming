#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    max_n = my_list[0]
    for m in my_list:
        if m > max_n:
            max_n = m

            return (max_n)
