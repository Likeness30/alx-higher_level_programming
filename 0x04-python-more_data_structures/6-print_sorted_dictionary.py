#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for m in sorted(my_dict.keys()):
        print("{}: {}".format(m, my_dict[m]))
