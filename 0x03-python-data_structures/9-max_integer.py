#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        max = None
    else:
        max = my_list[0]
        for int in my_list:
            if int > max:
                max = int
    return max
