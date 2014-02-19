
def find_neighbour(i, j):
	x_cords = [i + incr for incr in (-1, 0, 0, 1)]
	y_cords = [ j + jncr for jncr in (0, -1, 1, 0)]
	neighbours = zip(x_cords, y_cords)
	neighbours = [i for i in neighbours if((0<=i[0]<=2) and (0<=i[1]<=2))]
	print neighbours
	 
find_neighbour(0, 0)	
