#!/usr/bin/python

import sys

def algo(num):
        totalNum = []
	print(num)

	while num != 1:
		if num % 2 == 0:
			num = num / 2
                        totalNum.append(num)
			print(num)
		else:
			num = 3 * num + 1
                        totalNum.append(num)
			print(num)

        print "\nTotal Number :", len(totalNum)

def main():
	argv = int(sys.argv[1])
	algo(argv)


if __name__ == '__main__':
	main()