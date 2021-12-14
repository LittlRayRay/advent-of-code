pinput = open("input.txt", "r").read().splitlines()


def oxy_gen():
    test_input = []
    zero_count, one_count = 0, 0
    oxyGen=pinput[:]
    for idx in range(12):
        for line in oxyGen: 
            if line[idx] == '0':
                zero_count += 1
            elif line[idx] == '1':
                one_count += 1
        
        
        if zero_count > one_count: 
            for z in oxyGen: 
                if z[idx] == '0':
                    test_input.append(z)    
        else: 
            for z in oxyGen:
                if z[idx] == '1':
                    test_input.append(z)

        oxyGen = list(test_input)
        test_input = []

        zero_count, one_count = 0, 0
    return(oxyGen)

def co2_gen():
    test_input = []
    zero_count, one_count = 0, 0
    co2 = pinput[:]
    for idx in range(12):
        for line in co2: 
            if line[idx] == '0':
                zero_count += 1
            elif line[idx] == '1':
                one_count += 1
        
        
        if zero_count > one_count: 
            for z in co2: 
                if z[idx] == '1':
                    test_input.append(z)    
        else: 
            for z in co2:
                if z[idx] == '0':
                    test_input.append(z)

        co2 = list(test_input)
        test_input = []

        zero_count, one_count = 0, 0
    return(co2)

oxyGenInt = oxy_gen()
co2Int = co2_gen()
oxyGenInt = int(oxyGenInt[0], 2)
co2Int = int(co2Int[0], 2)
answer = co2Int * oxyGenInt