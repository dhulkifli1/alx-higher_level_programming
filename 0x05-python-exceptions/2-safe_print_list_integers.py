#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for element in range(x):
        try:
            if type(my_list[element]) == int:
                print("{:d}".format(my_list[element]), end = "")
                counter += 1
            else:
                continue
        except Exception:
            break
    print("")
    return counter
