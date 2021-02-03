# Enter a number and get all prime factors of that number

def isprime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

num = input("Enter a number: ")
num = int(num)
factors = []

# Find all the factors of the input number
for n in range(2, num):
	if num % n == 0:
		factors.append(n)

# Find all the prime number in the factors pool
for n in factors:
	if isprime(n):
		print(n)
