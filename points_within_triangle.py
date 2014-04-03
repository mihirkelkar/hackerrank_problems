import math
"""The logic here is a point is inside a triangle if the sum of the angles made by that point with the 3 points of the triangle is 2pi radians"""
def find_slope(x1, x2, y1, y2):
	if x2 - x1 != 0:
		return (y2 - y1 / x2 - x1)
	else:
		return float("inf")

def find_angle(m1, m2):
	if 1 + m1*m2 != 0:
		return math.atan((m1 - m2) / (1 + m1*m2))
	else:
		return math.atan(float("inf"))

def if_inside_triangle(x1, x2, x3, y1, y2, y3):
	max_x = max(x1, x2, x3)
	max_y = max(y1, y2, y3)
	min_x = min(x1, x2, x3)
	min_y = min(y1, y2, y3)
	for i in range(min_x, max_x):
		for j in range(min_y, max_y):
			total_angle = find_angle(find_slope(x1, i, y1, j) , find_slope(x2, i, y2, j))+find_angle(find_slope(x2, i, y2, j) , find_slope(x3, i, y3, j))+find_angle(find_slope(x3, i, y3, j) , find_slope(x1, i, y1, j))
			if total_angle == 2 * math.pi:
				print i, j
def main():
	x1 = input()
	y1 = input()
	x2 = input()
	y2 = input()
	x3 = input()
	y3 = input()
	if_inside_triangle(x1, x2, x3, y1, y2, y3)

if __name__ == "__main__":
	main()

