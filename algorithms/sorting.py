# This program illustrates three classic sorting algorithms: direct sort, merge sort, bubble sort

import time

def direct_sort(arr):
	while(True):
		flag = True
		for i in range(0, len(arr)):
			for j in range(i, len(arr)):
				if arr[i] <= arr[j]:
					continue
				else:
					temp = 0
					temp = arr[i]
					arr[i] = arr[j]
					arr[j] = temp
					flag = False
					
					# print(arr)
					# time.sleep(.2)

					continue

		if flag:
			break

def merge_sort(arr):

	print(arr)
	time.sleep(.2)

	mid = int(len(arr) / 2)
	left = arr[:mid]
	right = arr[mid:]

	if len(arr) > 1:
		merge_sort(left)
		merge_sort(right)

	direct_sort(arr)
	print(f"merging {arr}")
	return arr

def bubble_sort(arr):
	while(True):
		flag = True
		for i in range(0, len(arr)-1):
			# print(arr[i], arr[i+1])
			if arr[i] > arr[i + 1]:
				temp = 0
				temp = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = temp
				flag = False

				print(arr)
				time.sleep(.2)
		if flag:
			break



start_time = time.time()

arr=[56,123,3,42,32,12,4,1232142,72,2,0,34,65]

direct_sort(arr)
# merge_sort(arr)
# bubble_sort(arr)

print(arr)

print("--- %s seconds ---" % (time.time() - start_time))