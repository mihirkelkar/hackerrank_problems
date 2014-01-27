"""Suppose there were n numbers in an array S1, S2, S3, S4.......SN rearrange them in a such a way that they satisfy bellow property. 
S1<S2>S3<S4>......"""
import random
def swapper(temp):
	for i in range(0, temp):
		
temp = []
for i in range(0, random.randint(1,1000)):
	temp.append(random.randint(1, 1000))
temp = sorted(temp)

	

