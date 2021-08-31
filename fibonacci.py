def fib(num):
	if num == 1:
		return 1
	num -= 1
	first, second = 1, 0
	while num >= 2:
		second = first - second
		first = first + second
		num -= 1
	return second

def	main():
	while True:
		n = input("Insert number or q for exit: ")
		if n.isdigit():
			res = fib(int(n))
			print(res)
		elif n == 'q':
			print("exit")
			break

if __name__ == "__main__":
	main()