# Enter a n number to get a n decimal place of the prime number

import math, decimal

decimal_place = input("Enter the decimal place for PI (48 max): ")

try:
	decimal_place = int(decimal_place)
	pi_number = str(decimal.Decimal(math.pi))

	if decimal_place > 48:
		print("This program can only handle 48 decimal place at max")
	elif decimal_place < 0:
		print("Decimal place can not be negative")
	else:
		if decimal_place == 0:
			print(3)
		else:
			print(pi_number[:2+decimal_place])

except:
	print("Invalid input")
