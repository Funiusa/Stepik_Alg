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
	n = int(input("Insert number: "))
	print(fib(n))

if __name__ == "__main__":
	main()