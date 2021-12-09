file = open("input8.txt", "r")
input = file.read().splitlines()
input = file.read().split(" | ")

file.close()

# for x in range (len(input)): 
#     del input[x][0]

# answer, idx, idx2, flat_input = 0, 0, 0, []
# input = list(i[0].split() for i in input)
# flat_input = [item for sublist in input for item in sublist]

# for z in flat_input:
#     length = len(z)
#     # print(length)
#     if length == 2 or length == 4 or length == 3 or length == 7:
#         answer+=1
#         print(z)

# print(flat_input)



print(input)

