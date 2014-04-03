#!/usr/bin/python

"""Assume you are given a linked list where each node has a next pointer and an arbitaty pointer which points to an arbitary node in the list """

"""I am goinf to write a function which can clone this list"""

def clone(origfirstnode):
	#Clone all the next pointers of the list
	newcurnode = origfirstnode
	newhead = newcurnode
	origcur = origfirstnode.next
	while(origcur != None)
		newcurnode.next = origcur
		newcurnode = newcurnode.next
		origcur = origcur.next

	#Make the arbit pointer of new lit point to corresponding nodes in origlist and make the next pointers of old list point to the corresponding nodes in new list
	oldcur = originfirstnode
	newcur = newhead
	while((oldcur != None)and (newcur != None)):
		temp = oldcur.next
		oldcur.next = newcur
		newcur.arb = oldcur
		oldcur = temp
		newcur = newcur.next
	

	#assign arb pointers their right value
	nodecur = nodehead
	while(nodecur != None):
		nodecur.arb = nodecur.arb.arb.next
		nodecur = nodecur.next

	
	return nodehead		

	
		
