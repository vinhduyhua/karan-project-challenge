# This program will calculate monthly payment base on the mortgage amount and interest rate for 30 years fixed term

try:
	mortgage = input("Enter mortgage amount: ")
	mortgage = int(mortgage)

	interest_rate = input("Enter interest rate: ")
	interest_rate = int(interest_rate)/100

	monthly_payment = mortgage * (interest_rate/12)
	
	print(f"Your monthly payment for fixed 30 years term is : {monthly_payment}")
except ValueError:
	print("Invalid input. Program stop working.")
except:
	raise