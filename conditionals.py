def main():
	x, y = 10, 100

	if (x < y):
		st = "x is less than y"
	elif (x == y):
		st = "x is the same as y"
	else:
		st = "x is greater than y"

	print(st)

	st = "x is less than y" if (x<y) else "x is greater than or the same as y"

	print(st)


# if you are running this file from the terminal
# and you have this condition
# the function will run
if __name__ == "__main__":
	main()
