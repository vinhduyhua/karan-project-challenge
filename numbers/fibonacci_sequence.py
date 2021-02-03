# Enter a n number to get a n the fibonacci sequence of that number

def fibonacci(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

try:
	num = input("Please enter a number: ")
	num = int(num)

	if num < 1:
		print("Please enter number greater than 0")
	else:
		for n in range(1, num+1):
			print(fibonacci(n))
except ValueError:
	print("Invalid input")
except OverflowError:
	print("Number reach this program limit")