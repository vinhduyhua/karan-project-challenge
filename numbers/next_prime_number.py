# Program keep giving the next prime number

def isprime(n):
	if n < 2:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

num = 1

while(True):
	answer = input("Do you want to get the next prime number? (y/n) ")
	if answer == "y":
		while not isprime(num):
			num += 1
		print(num)
		num += 1
	elif answer == "n":
		break
	else:
		print("Please enter 'y' or 'n'")