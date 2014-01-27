"""Caclculate the total number of paths from the 0,0 to m,n given that you can move only towards the right and downwards"""
count = 0
def create_grid(m, n):
	#we need m rows and n columns
	grid = []
	for i in range(0, m):
		temp = []
		for i in range(0, n):
			temp.append(1)
		grid.append(temp)
	return grid

def find_max_paths(grid, y_cord, x_cord):
	global count
	m = len(grid)
	n = len(grid[0])
	#print y_cord, x_cord
	if x_cord < n - 1:
		find_max_paths(grid, y_cord, x_cord + 1)
	if y_cord < m - 1:	
		find_max_paths(grid, y_cord + 1, x_cord)
	if((x_cord == n - 1) and (y_cord == m - 1)):
		count += 1
def main():
	global count
	m = input("Enter number of rows")
	n = input("Enter numbr of columns")
	find_max_paths(create_grid(m, n), 0, 0)
	print count
		
if __name__ == "__main__":
	main()
	
