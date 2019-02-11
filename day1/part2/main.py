#!/usr/bin/env python3

import re
import sys


def main():
    frequency = 0
    frequency_store = []
    frequency_changes = read_file('input.txt')

    loop = True
    while loop:
        for frequency_change in frequency_changes:
            frequency += int(frequency_change)

            if frequency not in frequency_store:
                frequency_store.append(frequency)
            else:
                print(frequency)
                loop = False
                break


def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.readlines()

if __name__ == '__main__':
    main()
