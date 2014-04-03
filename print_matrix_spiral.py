def printspiral(horend, horstr, verend, verstr, grid):
	while((horstr < horend) and (verstr < verend)):
		for i in range(horstr, horend):
			print grid[verstr][i],
		horstr += 1
		for i in range(verstr, verend + 1):
			print grid[i][horend],
		horend -= 1
		for i in range(horend, horstr - 2, -1):
			print grid[verend][i],
		verend -= 1
		for i in range(verend , verstr, -1):
			print grid[i][horstr - 1],
		verstr += 1

def main():
	grid = [[1,2,3], [6,7,8]]# [11,12, 13, 14, 15], [16, 17, 18, 19, 20], [21,22, 23, 24, 25]]
	printspiral(len(grid[0]) - 1, 0, len(grid) - 1, 0, grid)

if __name__ == "__main__":
	main()

