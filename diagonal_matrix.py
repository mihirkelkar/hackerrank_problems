def matrix_diagonal_mirroring(matrix):
	for i in range(0, len(matrix)):
		for j in range(i, len(matrix[i])):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	return matrix		

def main():
	grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	print matrix_diagonal_mirroring(grid)			

main()
