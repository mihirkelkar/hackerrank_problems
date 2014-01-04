#!/usr/bin/py
# Head ends here
import itertools
def findStrings(a,query):
    oldset = set()
    for i in a:
        temp = itertools.permutations(i)
        lister = []
        for p in temp:
            lister.append(''.join(p))
	print lister
        newset = set(lister)
	print newset
        oldset = set(itertools.chain(oldset, newset))
	print oldset
    temp = sorted(list(oldset))    
    print temp	
    for i in query:
        if i > len(temp):
            print "INVALID"
        else:
            print temp[i - 1]


if __name__ == '__main__':
    n = input()
    string=[]
    for i in range(0,n):
        string.append(raw_input())
    q= input()
    query=[]
    for i in range(0,q):
        query.append(input())
    findStrings(string,query)
