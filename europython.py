"""Need to finish this function tomorrow, this is critical"""
		
def main():
	fp = open(sys.argv[1], r'U')
	num_test_cases = int(fp.readline().strip())
	for i in range(num_test_cases):
		temp = []
		for j in range(int(fp.readline().strip())):
			temp.append(fp.readline().strip())
		robot_checker(temp)

