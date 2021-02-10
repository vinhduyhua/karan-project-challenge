# This program will calculate the change return based on the cost and the amount give

from decimal import Decimal

dollar, quarter, dime, nickel, penny = 0,0,0,0,0

try:
	cost = input("Enter the cost: ")
	cost = round(float(cost), 2)
	amount_paid = input("Enter the paid amount: ")
	amount_paid = round(float(amount_paid), 2)
except:
	raise

try:
	if amount_paid >= cost:
		change = float(round(amount_paid - cost, 2))

		while(change > 0):
			if change > 1:
				dollar += 1
				change -= 1
				continue
			if change > .25:
				quarter += 1
				change -= .25
				continue
			if change > .1:
				dime += 1
				change -= 1
				continue
			if change > .05:
				nickel += 1
				change -= .05
				continue

			penny += 1
			change = change - .01

		print(f"Your change is {dollar} dollar, {quarter} quarter, {dime} dime, {nickel} nickel, {penny} penny")
	else:
		print("Insufficient pay")
except:
	raise