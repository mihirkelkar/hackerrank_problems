import sys
class level:
	def __init__(self, data, unset):
		self.data = {}
		self.unset = []

levellist = []
data = {}
tempunset = []
levellist.append(level(data, tempunset))
while 1:
	choice = raw_input().split()
	if choice[0] == "SET":
		(levellist[-1]).data[choice[1].lower()] = [int(choice[2]), 1]
	elif choice[0] == "GET":
		flag = 0
		for i in reversed(levellist):
			if (i.data.get(choice[1].lower()) == None):
				continue
			else:
				
				if (i.data.get(choice[1].lower()))[1] == 0:
					print "NULL"
				else:
					print (i.data.get(choice[1].lower()))[0]
				flag = 1
				break
		if flag == 0:
			print "NULL"
	elif choice[0] == "UNSET":
		if levellist[-1].data.get(choice[1].lower()) == None:	
			(levellist[-1]).data[choice[1].lower()] = [0, 0]
			levellist[-1].unset.append(choice[1].lower())
		else:
			((levellist[-1]).data[choice[1].lower()])[1] = 0
			levellist[-1].unset.append(choice[1].lower())
	elif choice[0] == "NUMEQUALTO":
		counter = 0
		totalunset = []
		for i in reversed(levellist):
			totalunset = totalunset + i.unset
			for j in i.data.items():
				if j[0] not in totalunset:
					if j[1][0] == int(choice[1]) and j[1][1] == 1:
						counter = counter + 1
		print counter		
				
	elif choice[0] == "BEGIN":
		tempdata = {}
		templist = []
		levellist.append(level(tempdata, templist))
	elif choice[0] == "ROLLBACK":
		if len(levellist) > 1:
			levellist.pop()
		else:
			print "NO TRANSACTION"
	elif choice[0] == "COMMIT":
		for i in range(1, len(levellist)):
			levellist[0].data.update(levellist[i].data)
		levellist = [levellist[0]]			
	elif choice[0] == "END":
		sys.exit(1)

