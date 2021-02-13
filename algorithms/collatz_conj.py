# This program replicate Conllatz Conjecture algorithm

def collatz_conj(n):
	if n % 2 == 0:
		return n / 2
	else:
		return n * 3 + 1

count = 0
n = input("Please enter n's value: ")
n = int(n)
while (n > 1):
	n = collatz_conj(n)
	print(n)
	count += 1

print(f"The number of steps is {count}")