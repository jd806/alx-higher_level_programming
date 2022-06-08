#!/usr/bin/python3
def no_c(my_string):
    string_copy = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            string_copy += c
    return string_copy
