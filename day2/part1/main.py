#!/usr/bin/env python3

import re
import sys


def main():
    input_file = read_file('input.txt')
    two_letter_count = 0
    three_letter_count = 0

    for box_id in input_file:
        two_letter_get = False
        three_letter_get = False

        for letter in set(box_id):
            letter_frequency = 0
            for i in range(len(box_id)):
                if letter == box_id[i]:
                    letter_frequency += 1
            if letter_frequency == 2 and two_letter_get != True:
                two_letter_get = True
            if letter_frequency == 3 and three_letter_get != True:
                three_letter_get = True
        if two_letter_get:
            two_letter_count += 1
        if three_letter_get:
            three_letter_count += 1

    print(two_letter_count * three_letter_count)


def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


if __name__ == '__main__':
    main()
