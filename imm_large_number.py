def work(array):
	max_num = array[-1]
	prev_max_array = []
	array[-1] = -1
	for i in range(len(array) - 2, -1, -1):
		if max_num > array[i]:
			prev_max_array.append(max_num)
			max_num, array[i] = array[i], max_num
		if max_num < array[i]:
			for elem in reversed(prev_max_array):
				if elem > array[i]:
					prev_max_array.append(max_num)
					max_num = array[i]
					array[i] = elem
					break
			else:
				prev_max_array.append(max_num)
				max_num = array[i]
				array[i] = -1
	print array
def main():
	work([3,1,2,5,9,4,8])

main()
						
		
		

