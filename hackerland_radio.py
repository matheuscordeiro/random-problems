
# Hackerland Radio Transmitters
# Difficulty: Medium

def hackerlandRadioTransmitters(x, k):
    x_sorted = sorted(x)
    transmitters = 0
    i = 0
    while i < len(x): 
        transmitters += 1

        loc = x_sorted[i] + k
        while i < len(x) and x_sorted[i] <= loc:
            i += 1
        
        i = i - 1
        loc = x_sorted[i] + k
        while i < len(x) and x_sorted[i] <= loc:
            i += 1
       
    return transmitters


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5] # 1
    print(hackerlandRadioTransmitters(array, 1))