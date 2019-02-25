import re


with open('test_input.txt') as file:
    coordinates = file.read().splitlines()

print(coordinates)

# north east walk
coord = coordinates[0]
m = re.match(r'(\d+), (\d+)', coord)
x = int(m.group(1))
y = int(m.group(1))

print(x)
print(y)

walk_x_right(x)
walk_x_left(x)
walk_x_north(x)
walk_x_south(x)

def walk_x_right(x):
    while x != 0 and x < 1000:
        print(x)
        x += 1
        new_coord = ("%s, %s" % (x, y))
        print(new_coord)
        if new_coord in coordinates:
            print('BOOM')

def walk_x_left(x):
    while x != 0 and x < 1000:
        print(x)
        x -= 1
        new_coord = ("%s, %s" % (x, y))
        print(new_coord)
        if new_coord in coordinates:
            print('BOOM')



# x_coords = {}
# y_coords = {}

# alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
# i = 0

# for line in lines:
#     print(line.strip())
#     m = re.match(r'(\d+), (\d+)', line.strip())
#     x_coords[alpha[i]] = m.group(1)
#     y_coords[alpha[i]] = m.group(2)
#     i += 1

# sorted_x_coords = sorted(x_coords, key=x_coords.get)
# print(x_coords)
# print(sorted_x_coords)

# num_coords = len(x_coords)
# if (num_coords % 2) == 0:
#     array_middle1 = num_coords / 2
#     array_middle2 = array_middle1 - 1

# middle_x_coords = [sorted_x_coords[array_middle1], sorted_x_coords[array_middle2]]

# print(middle_x_coords)

    # for char, x_coord in x_coords.items():
    #     if x_coord == (num_coords / 2):
    #         print(char)
    #     if x_coord == ((num_coords / 2) + 1):
    #         print(char)
    # print(x_coords = (num_coords / 2))
    # print(x_coords[(num_coords / 2) + 1])






# num_coords = len(x_coords)
# if (num_coords % 2) == 0:
#     middle1 = int(num_coords / 2)
#     middle2 = int(middle1 + 1)

# sorted_x_coords = sorted(x_coords.iteritems(), key=lambda (k,v): (v,k))

# for char, x_coord in sorted_x_coords:
#     if int(x_coord) == middle1 or int(x_coord) == middle2:
#         print("%s, %s" % (char, x_coord))