def main():
	x = input("Enter number of rows")
	y = input("Enter number of columns")
	global forest
	forest = []
	for i in range(0, x):
		temp = []
		for i in range(0, y):
			temp.append(input())
		forest.append(temp)
	tree_cut = find_route(0,0,0)

def find_route(i, j, count):
	if(forest[i][j] == 1):
		count = count + 1
	if (i == len(forest) - 1) and (j == len(forest[0]) - 1):
		return count
	else:
		temp1 = temp2 = temp3 = temp4 = float('inf')
		if j < len(forest[0]) - 1:
			temp1 = find_route(i, j + 1, count)
		if j > 0:
			temp2 = find_route(i, j - 1, count)
		if i < len(forest) - 1:
			temp3 = find_route(i + 1, j, count)
		if i > 0:
			temp4 = find_route(i - 1, j, count)
		return min(temp1, temp2, temp3, temp4)

if __name__ =="__main__":
	main()
		
		
	
