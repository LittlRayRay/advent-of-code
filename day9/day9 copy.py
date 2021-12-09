file = open("input.txt", "r").read().split("\n")
input = file

# solve advent of code day 9 part 1

def check_for_low_points(y, x, y1, x1):
    if input_list[y][x]

input_list, low_points, answer = [] ,[], 0


for i in input:
    list_to_append = []
    for j in i:
        list_to_append.append(j)
    input_list.append(list_to_append)

for y in range(len(input_list)):
    for x in range(len(input_list[y])):
        if y == 0 and x == 0:
            if input_list[y+1][x] > input_list[y][x] and input_list[y][x+1] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif y == 0 and x == len(input_list[y])-1:
            if input_list[y+1][x] > input_list[y][x] and input_list[y][x-1] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif y == len(input_list)-1 and x == len(input_list[y])-1:
            if input_list[y-1][x] > input_list[y][x] and input_list[y][x-1] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif y == len(input_list)-1 and x == 0:
            if input_list[y-1][x] > input_list[y][x] and input_list[y][x+1] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif x == 0:
            if input_list[y+1][x] > input_list[y][x] and input_list[y-1][x] > input_list[y][x] and input_list[y][x+1] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif x == len(input_list[y])-1:
            if input_list[y+1][x] > input_list[y][x] and input_list[y-1][x] > input_list[y][x] and input_list[y][x-1] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif y == 0:
            if input_list[y][x + 1] > input_list[y][x] and input_list[y][x - 1] > input_list[y][x] and input_list[y + 1][x] > input_list[y][x]:
                low_points.append(input_list[y][x])
        elif y == len(input_list)-1:
            if input_list[y][x + 1] > input_list[y][x] and input_list[y][x - 1] > input_list[y][x] and input_list[y - 1][x] > input_list[y][x]:
                low_points.append(input_list[y][x])
        else:
            if input_list[y+1][x] > input_list[y][x] and input_list[y-1][x] > input_list[y][x] and input_list[y][x+1] > input_list[y][x] and input_list[y][x-1] > input_list[y][x]:
                low_points.append(input_list[y][x])

print(low_points)

for i in range(len(low_points)):
    answer += (int(low_points[i]) + 1)

print(answer)