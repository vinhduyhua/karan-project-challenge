import math, decimal

decimal_place = input("Enter the decimal place for PI (51 max): ")

try:
	decimal_place = int(decimal_place)
	e_number = str(decimal.Decimal(math.e))

	if decimal_place > 51:
		print("This program can only handle 51 decimal place at max")
	elif decimal_place < 0:
		print("Decimal place can not be negative")
	else:
		if decimal_place == 0:
			print(3)
		else:
			print(e_number[:2+decimal_place])

except:
	print("Invalid input")