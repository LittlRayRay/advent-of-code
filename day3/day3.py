input = open('input.txt', 'r').read().splitlines()
print(input)

zero_count, one_count, idx = 0, 0, 0  # zero_count, one_count, idx

test_input = input

for i in range(12):
    for line in test_input:
        if line[idx] == '0':
            zero_count += 1
        else:
            one_count += 1
    for line in test_input: 
        if zero_count > one_count:
            for line in test_input:
                if line[idx] == '0':
                    test_input.remove(line)
        else:
            for line in test_input:
                if line[idx] == '1':
                    test_input.remove(line)
    idx += 1
    zero_count, one_count = 0, 0
    input = test_input


print (input)
