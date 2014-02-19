import sys
#go through the entire grid finding a path to the sink
#make another two by two grid to store sink maps, for all co-ordinates in original map, mark grid with new label. 
#Use a recursive function.
#before embarking on checking sink in original em, always check whether a sink has already been associated with it in the sink map.
def find_nbrs(i, j, row, col):
	x_cords = [i + incr for incr in (-1, 0, 0, 1)]
	y_cords = [j + jncr for jncr in (0, -1, 1, 0)]
	temp = zip(x_cords, y_cords)
	return [i for i in temp if ((0<=i[0]<row) and (0<=i[1]<col))]


def sink_map(em):
	sink_dict = {}
	sinkmap = []
	for i in range(len(em)):
		sinkmap.append([0] * len(em[0]))	
	count = 97
	for i in range(len(em)):
		for j in range(len(em[0])):
			if sinkmap[i][j] != 0:
				continue
			else:
				sinked_maps = find_and_label(em, i, j)
				#print sinked_maps
				for elem in sinked_maps:
					sinkmap[elem[0]][elem[1]] = sinked_maps[0]
				try:
					char = sink_dict[sinked_maps[0]]
				except:
					sink_dict[sinked_maps[0]] = chr(count)
					count += 1
				
	for i in range(len(sinkmap)):
		for j in range(len(sinkmap[0])):
			sinkmap[i][j] = sink_dict[sinkmap[i][j]]
	return sinkmap 
def find_and_label(em, i, j):
	#print i, j
	nbrs = find_nbrs(i, j, len(em), len(em[0]))
	map_nbrs = [em[k[0]][k[1]] for k in nbrs]
	mi = map_nbrs.index(min(map_nbrs))
	if map_nbrs[mi] > em[i][j]:
		#print "last element reached", i, j
		return [(i, j)]
	else:
		path = find_and_label(em, nbrs[mi][0], nbrs[mi][1])
		path.append((i,j))
		return path



def main():
#take mad inputs from the user and construct the goddam grid
	answers = []
	fp = open(sys.argv[1], r'U')
	cp = open('output', 'w')
	num_test_cases = int(fp.readline().strip())
	for i in range(num_test_cases):
		row_info = [int(x) for x in fp.readline().strip().split()]
		em = []
		for i in range(row_info[0]):
			em.append([int(x) for x in fp.readline().strip().split()])
		answers.append(sink_map(em))	
	
	for i in range(len(answers)):
		cp.write('Case #' + str(i + 1) + ":\n")
		for j in answers[i]:
			cp.write(' '.join(j) + "\n")
	cp.close()
if __name__ == "__main__":
	main()
