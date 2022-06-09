array = [8,4,6,2,5,1,3,7,9]

def quick_sort(array):
	if len(array) <= 1:
		return array
	pivot = len(array) // 2
	front_arr, pivot_arr, back_arr = [], [], []
	for value in array:
		if value < array[pivot]:
			front_arr.append(value)
		elif value > array[pivot]:
			back_arr.append(value)
		else:
			pivot_arr.append(value)
	#print(front_arr, pivot_arr, back_arr)
	return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

print("before: ",array)
array = quick_sort(array)
print("after:", array)