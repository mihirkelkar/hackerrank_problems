import sys
def cu(x, y, a):
	while(x >= 0):
		if a[x][y] == 1:
			return 1
		x = x - 1
	return 0
def cd(x,y,a):
	while(x <= len(a) - 1):
		if a[x][y] == 1:
			return 1
		x = x + 1
	return 0
def cl(x,y,a):
	while(y >=  0):
		if a[x][y] == 1:
			return 1
		y = y - 1
	return 0
def cr(x, y, a):
	while(y <= len(a) - 1):
		if a[x][y] == 1:
			return 1
		y = y + 1
	return 0
def cld(x, y, a):
	while((x  >= 0) and (y >= 0)):
		if a[x][y] == 1:
			return 1
		x = x - 1
		y = y - 1
	return 0
def crd(x, y, a):
	while((x  >= 0) and (y <= len(a) - 1)):
		if a[x][y] == 1:
			return 1
		x = x - 1
		y = y + 1
	return 0
def checks(x, y, a):
	temp = cu(x, y, a) or cd(x, y, a) or cl(x, y, a) or cr(x, y, a) or cld(x, y, a) or crd(x, y, a)
	return temp

def nqueens(x, y, a):
	print "checking"
	if checks(x, y, a) == 0:
		a[x][y] = 1
		if x < len(a) - 1:
			nqueens(x + 1, y, a)
		else:
			print a
			sys.exit(1)
		a[x][y] = 0
		if y < len(a) - 1:
			nqueens(x, y + 1, a)
	elif checks(x, y, a) == 1:
		if y < len(a) - 1:
			nqueens(x, y + 1 , a)
def main():
	a = []
	for i in range(0, 5):
		temp = []
		for j in range(0, 5):
			temp.append(0)
		a.append(temp)
	nqueens(0, 0, a)

main()
