file = open("example.txt", "r").read().splitlines()
input = file

FIRST_ENTER = []

print(input)

# make dictionary with all opening parentheses

opening = {"(": 0, "{": 0, "[": 0, "<": 0}

closing = {")": 0, "}": 0, "]": 0, ">": 0}

clean_closing, clean_opening = closing, opening 

for l in range(len(input)):

    opening = clean_opening.copy()
    closing = clean_closing.copy()

    for i in range(len(input[l])):
        try:
            opening[str(input[l][i])] += 1
        except KeyError:
            closing[str(input[l][i])] += 1
        try:
            if closing[")"] > opening["("] or closing["}"] > opening["{"] or closing["]"] > opening["["] or closing[">"] > opening["<"]:
                if FIRST_ENTER != True:
                    FIRST_ENTER.append(str(input[l][i]))
                    print(FIRST_ENTER)
                elif str(input[l][i]) in FIRST_ENTER:
                    FIRST_ENTER.append(str(input[l][i]))
                    print(FIRST_ENTER)
        except KeyError:
            pass

# print closing and opening

print(opening)
print(closing)