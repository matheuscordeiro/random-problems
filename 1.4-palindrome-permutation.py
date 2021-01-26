#!/usr/local/bin/python3

# Palindrome Permutation

# Problem: Given a string, write a function to check if it is a permutation of a palindrome.

def check_palindrome(string):
	size_string = len(string)
	for key, value in enumerate(string):
		if value != string[size_string-key-1] and value != " " and string[size_string-key-1] != " ":
			return False

	return True

check_palindrome("arara")

