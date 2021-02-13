# This program applies Sieve of Eratosthenes to find all prime numbers from 2 to an input number

import time

def sieve_era(n):
	nums = {}
	for i in range(2,n+1):
		nums[i] = False

	for k, v in nums.items():
		if v == False:
			for i in range(k, n):
				multiply = i*k

				if multiply > n:
					break

				nums[multiply] = True

	print(f"Total of prime numbers is {sum(v == False for v in nums.values())}")

n = input("Enter a number: ")
n = int(n)

start_time = time.time()

sieve_era(n)

print("--- %s seconds ---" % (time.time() - start_time))


# Less efficient method
# def sieve_era(n):
# 	marked = []
# 	for i in range(2,n):
# 		flag = True
# 		if i in marked:
# 			continue
# 		for j in range(i,n):

# 			multiple_num = j*i

# 			if multiple_num > n:
# 				break

# 			if multiple_num not in marked:
# 				print(i, j, multiple_num, flag)
# 				marked.append(multiple_num)
# 				flag = False
		
# 			# marked.sort()
# 			# print(marked, len(marked))
# 			# time.sleep(0.01)
# 			# break

# 		if flag:
# 			break

# 	count = 4
# 	prime_count = 0
# 	for i in marked:
# 		count += 1
# 		if count != i:
# 			prime_count += 1
# 	print(f"The total numbers of prime is {prime_count}")