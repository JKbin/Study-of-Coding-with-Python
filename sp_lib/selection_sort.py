array = [8,4,6,2,9,1,3,7,5]

def selection_sort(array):
	n = len(array)
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if array[j] < array[min_index]:
				min_index = j
		array[i], array[min_index] =  array[min_index], array[i]
		#print(array[:i+1])

print("before: ",array)
selection_sort(array)
print("after:", array)