def fib(num):
	if num == 1:
		return 1
	second, first = 2, 1
	for i in range(num - 3):
		second, first = (second + first) % 10, second
	return second


def main():
	while True:
		n = input("Insert number or q for exit: ")
		if n.isdigit():
			res = fib(int(n))
			print("fib: ", res)
		elif n == 'q':
			print("exit")
			break


if __name__ == "__main__":
	main()
