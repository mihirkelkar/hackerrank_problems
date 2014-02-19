"""Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next N days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

Input

The first line contains the number of test cases T. T test cases follow:

The first line of each test case contains a number N. The next line contains N integers, denoting the predicted price of WOT shares for the next N days.

Output

Output T lines, containing the maximum profit which can be obtained for the corresponding test case."""
"""My solution is as follows, look at the array from the end, look for the hihgest bid so far, mark that as sell day. Split the array into two and look for other sell days """


def cacl_max_profit(array):
	"""We decide the convention 1 for sell, 0 for buy"""
	profit = 0
	maxn = 0
	buy = [0] * len(array)
	for i in range(len(array) - 1,-1,-1):
		if array[i] > maxn:
			maxn = array[i]
			buy[i] = 1
	buy_goods = []
	for i in range(0, len(array)):
		if buy[i] == 0:
			buy_goods.append(array[i])
		if buy[i] == 1:
			profit += (array[i]  * len(buy_goods)) - sum(buy_goods)
			buy_goods = []
			
	return profit

def main():
	test_cases = input()
	temp = []
	for i in range(test_cases):
		length = input()
		temp.append([int(x) for x in raw_input().split()])
	
	for i in temp:
		print cacl_max_profit(i)
main()
