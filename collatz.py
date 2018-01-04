#!/usr/bin/python

import sys

def algo(num):
	print(num)

	while num != 1:
		if num % 2 == 0:
			num = num / 2
			print(num)
		else:
			num = 3 * num + 1
			print(num)

def main():
	argv = int(sys.argv[1])
	algo(argv)


if __name__ == '__main__':
	main()