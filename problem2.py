counter = 0
def numberofpaths(a):
	global counter
	lx = len(a)
	ly = len(a[0])
	x = 0
	y = 0
	rec_path(x, y, a, lx, ly)
	print counter

def rec_path(x, y, a, lx, ly):
	global counter
	if x == lx - 1 and y == ly - 1:
		counter = counter + 1
	else:
		if (x < lx - 1) and (a[x + 1][y] == 1):
			rec_path(x + 1, y, a, lx, ly) 
		if (y < ly - 1) and (a[x][y + 1] == 1):
			rec_path(x, y + 1, a, lx, ly)
a = [[0,0],[0,0]]
numberofpaths(a)	
