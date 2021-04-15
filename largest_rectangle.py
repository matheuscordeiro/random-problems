def largestRectangle(h):
    largest_area = 0
    for key, value in enumerate(h):
        area = h[key]
        i = key - 1
        j = key + 1
        # search in left side
        while i >= 0 and h[i] >= h[key]:
            area += h[key]
            i -= 1

        # search in right side
        while j < len(h) and h[j] >= h[key]:
            area += h[key]
            j += 1

        largest_area = max(largest_area, area)
        

    return largest_area

if __name__ == "__main__":
    h = [8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]
    print(largestRectangle(h))