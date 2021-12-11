input = open('input.txt', 'r').read().splitlines()
print(input)

zero_count, one_count = 0, 0 # zero_count, one_count, idx

test_input = input

zeroes_removed, ones_removed = 0,0

for idx in range(len(input[0])):
    for i in test_input:
        if i[idx] == '0':
            zero_count += 1
        elif i[idx] == '1':
            one_count += 1
    for i in test_input:
        if zero_count > one_count:
            print("remove 0")
            zeroes_removed += 1
            for line in test_input:
                if line[idx] == "0":
                    test_input.remove(line)
                    
            
        elif zero_count <= one_count: 
            print("remove 1")
            ones_removed += 1
            for line in test_input:
                if line[idx] == "1":
                    test_input.remove(line)
                    

    zero_count, one_count = 0, 0
    input = test_input

        
            


print (input)
print(zeroes_removed, ones_removed)
