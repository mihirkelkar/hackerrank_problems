#Code to detect wrong configurations
import sys
#separate each line
temp = raw_input().split(r'\n')
if len(temp) == 1:
	print "Valid Configuration"
else:
	paths = []
	ips = []
	for i in temp:
		paths.append((i.split())[0])
		ips.append((i.split())[1])
	#print paths

	#Look for repeted paths
	for i in range(0,len(paths)):
		#print paths[i]
		if paths.count(paths[i]) > 1:
			#path repeated
			print "Invalid Configuration"
			sys.exit(1)
	#Look for paths with stars at the end and a specific different ip later
	for i in range(0, len(paths) - 1):
		path_finder = paths[i].split('/')
		num = i
		if path_finder[2] == "*":
			for j in range(i + 1, len(paths)):
				path_findertwo = paths[j].split('/')
				if (sorted(path_findertwo[1]) == sorted(path_finder[1])):
					if sorted(ips[i]) == sorted(ips[j]):
						continue	
					else:
						print "Invalid Configuration"
						sys.exit(1)
		
	for i in range(0, len(ips) - 1):
		for j in range(i + 1, len(ips)):
			if sorted(ips[i]) == sorted(ips[j]):
				newone = paths[i].split('/')
				newtwo = paths[j].split('/')
				if (newone[2] == "*") or newtwo[2] == "*":
					continue
				else:
					print "Invalid Configurtion"
					sys.exit(1)
	print "Valid Configuration"		
