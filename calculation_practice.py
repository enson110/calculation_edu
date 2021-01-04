# -*- coding: UTF-8 -*-

from random import randint
import sys


def flag_to_str(flag_int):
    if flag_int == 1:
        return "+"
    return "-"


# 两位数加减法
def two_numbers(max_result):
    left = randint(2, max_result - 1)
    right = 0
    flag_int = randint(1, 2)
    if flag_int == 2:
        # 减法不能出现负数
        right = randint(1, left)
    else:
        right = randint(1, max_result - left)

    return str(left) + " " + flag_to_str(flag_int) + " " + str(right) + " = "


def three_numbers(max_result):
    left = randint(2, max_result - 1)
    right = 0
    flag_int = randint(1, 2)
    if flag_int == 2:
        # 减法不能出现负数
        right = randint(1, left)
    else:
        right = randint(1, max_result - left)

    second_flag_int = randint(1, 2)
    last = 0
    two_result = left + right if flag_int == 1 else left - right
    if second_flag_int == 2:
        last = randint(0, two_result)
    else:
        last = randint(0, max_result - two_result)

    return str(left) + " " + flag_to_str(flag_int) + " " + str(right) +\
            " " + flag_to_str(second_flag_int) + " " + str(last) + " " + " = "


def newline_or_table(index):
    if index % 4 == 3:
        sys.stdout.write("\n")
    else:
        sys.stdout.write("\t")


if __name__ == '__main__':
    for i in range(120):
        if i < 40:
            sys.stdout.write(two_numbers(20))
        elif i % 4 == 3:
            sys.stdout.write(three_numbers(20))
        else:
            sys.stdout.write(two_numbers(20))
        newline_or_table(i)