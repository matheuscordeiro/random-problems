
#!/usr/local/bin/python3


# Problem: Given a smaller string s and a bigger string b, design an algorithm to find all permutations
# of the shorter string within the longer. Print the location of each permutation.

# credits: https://www.geeksforgeeks.org/anagram-substring-search-search-permutations/ 
# (Rabin Karp algorithm)


MAX = 256 # Letters are mapped from 0 to 255 at UNICODE


def compare(array1, array2): 
	size1 = len(array1)
	size2 = len(array2)
	if size1 == size2:
	    for i in range(MAX): 
	        if array1[i] != array2[i]: 
	            return False
	    return True

	return False


def search_permutation(s, b):
	size_s = len(s)
	size_b = len(b)
	pattern = [0] * MAX
	window = [0] * MAX

	# First window
	for i in range(size_s):
		pattern[ord(s[i])] += 1
		window[ord(b[i])] += 1


	for i in range(size_s, size_b):
		if compare(pattern, window):
			print(f"Found at index: {i-size_s}")

		window[ord(b[i])] += 1 # add current character
		window[ord(b[i-size_s])] -= 1 # remove charcter of previous window


	if compare(pattern, window):
		print(f"Found at index: {size_b-size_s}")


