#!/usr/local/bin/python3

# Triangle display problem

# Input: 
# 6

# Output:

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

import sys

def display_triangle(rows: int):
	cols = rows
	for i in range(rows):
		j_init = rows - i - 1
		show_ast = True
		for j in range(cols):
			if j >= j_init and show_ast:
				print("*", end="")
				show_ast = False
			else:
				print(" ", end="")
				show_ast = True

		cols += 1
		print("")


if __name__ == "__main__":
	rows = sys.argv[1]
	display_triangle(int(rows))
