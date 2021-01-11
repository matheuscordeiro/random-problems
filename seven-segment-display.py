#!/usr/local/bin/python3

# Seven-segment display problem

import sys


rows = {
	"0": ("###", "# #", "# #", "# #", "###"),
	"1": ("  #", "  #", "  #", "  #", "  #"),
	"2": ("###", "  #", "###", "#  ", "###"),
	"3": ("###", "  #", "###", "  #", "###"),
   	"4": ("# #", "# #", "###", "  #", "  #"),
   	"5": ("###", "#  ", "###", "  #", "###"),
   	"6": ("###", "# #", "###", "#  #", "###"),
   	"7": ("###", "  #", "  #", "  #", "  #"),
   	"8": ("###", "# #", "###", "# #", "###"),
   	"9": ("###", "# #", "###", "  #", "###"),
}

def display_segment(number):
	for i in range(5):
		for char in number:
			for j in range(3):
				print(rows[char][i][j], end="")
			print(" ", end="")
		
		print("")

if __name__ == "__main__":
	number = sys.argv[1]
	display_segment(number)
