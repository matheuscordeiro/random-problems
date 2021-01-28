#!/usr/local/bin/python3

# String compression


def string_compression(s):
	before = ''
	final = ''
	count = 0
	for key, character in enumerate(s):
		if character != before:
			if key != 0:
				final = f'{final}{count}{before}'
			
			count = 1
			before = character

		else:
			count += 1

	final = f'{final}{count}{before}'
	if len(final) >= len(s):
		return s
	else:
		return final


print(string_compression('aabbbcc'))
