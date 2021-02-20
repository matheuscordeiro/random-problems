def flip_bip_to_win(number):
    binary = '{0:b}'.format(number)
    size_binary = len(binary)
    max_count = -1
    for i in range(size_binary):
        count_zero = count_one = 0
        for j in range(i,size_binary): 
            if binary[j] == '0':
                if count_zero == 1:
                    break
                
                count_zero += 1
            
            count_one += 1
    
        max_count = max(max_count, count_one)
    
    return max_count


if __name__ == '__main__':
    print(flip_bip_to_win(1775))