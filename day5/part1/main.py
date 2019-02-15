import re

with open('input.txt') as file:
    line = file.read()
    polymer = list(line)

def main():
    while True:
        start_polymer_length = len(polymer)
        react(polymer)
        end_polymer_length = len(polymer)
        if start_polymer_length == end_polymer_length:
            # print("".join(polymer))
            print(len(polymer))
            exit(0)

# print("".join(polymer))

def react(polymer):
    prev_letter = ""
    index = 0
    for letter in polymer:
        if (prev_letter.lower() == letter.lower() and ((prev_letter.isupper() and letter.islower()) or (prev_letter.islower() and letter.isupper()))):
            del polymer[index - 1]
            del polymer[index - 1]
            # print("".join(polymer))
            break
        else:
            prev_letter = letter
        index += 1

if __name__ == '__main__':
    main()
