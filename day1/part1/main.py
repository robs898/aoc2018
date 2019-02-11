#!/usr/bin/env python3

import re
import sys


def main():
    frequency = 0
    input_file = read_file('input.txt')
    frequency_changes = iter(input_file)

    for frequency_change in frequency_changes:
        frequency += int(frequency_change)
    print(frequency)


def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()


if __name__ == '__main__':
    main()
