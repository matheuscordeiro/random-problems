def smallest_substring(p, s):
    values = {character: True for character in p}
    start = -1
    end = len(s)
    limit = len(s) - len(p) + 2
    for i in range(limit):
        frequency = {}
        count = 0
        j = i
        while j < len(s):
            if values.get(s[j]) and not frequency.get(s[j]):
                count += 1
                frequency[s[j]] = True

            if count == len(p):
                if (end - start) > (j - i):
                    start = i
                    end = j
                break

            j += 1
    
    if start == -1:
        return "-1"
    else:
        return s[start:end+1]


if __name__ == "__main__":
    p = "xyz"
    s = "xyyzyzyx"
    # p = ["o", "z", "a"]
    # s = "zoomlazapzo"
    # p = ["t", "o", "c"]
    # s = "timetopractice"
    print(smallest_substring(p, s))            
                    
