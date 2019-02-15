# from multiprocessing.dummy import Pool as ThreadPool

def react(polymer):
    while True:
        start_polymer_length = len(polymer)
        i = 0
        while (i < (len(polymer) - 1)):
            if (polymer[i].lower() == (polymer[i + 1]).lower() and ((polymer[i].isupper() and (polymer[i + 1]).islower()) or (polymer[i].islower() and (polymer[i + 1]).isupper()))):
                del polymer[i]
                del polymer[i]
            i += 1
        if len(polymer) == start_polymer_length:
            return(polymer)

with open('input.txt') as file:
    polymer = file.read()

reacted_polymer_lengths = {}

# threading appears to run 10 seconds slower on my mac
# def run(char):
#     print(char)
#     p1 = polymer.replace(char, "")
#     p2 = p1.replace(char.capitalize(), "")
#     reacted_polymer = react(list(p2))
#     reacted_polymer_lengths[char] = len(reacted_polymer)
# pool = ThreadPool(4)
# pool.map(run, list('abcdefghijklmnopqrstuvwxyz'))

for char in 'abcdefghijklmnopqrstuvwxyz':
    print(char)
    p1 = polymer.replace(char, "")
    p2 = p1.replace(char.capitalize(), "")
    reacted_polymer = react(list(p2))
    reacted_polymer_lengths[char] = len(reacted_polymer)

sorted_polymer_lengths = sorted(reacted_polymer_lengths, key=reacted_polymer_lengths.get)
shortest_char = next(iter(sorted_polymer_lengths))
print(reacted_polymer_lengths[shortest_char])
