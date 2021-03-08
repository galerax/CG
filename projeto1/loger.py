


def write_line(pos1, pos2):
	log = open('log.txt', 'a')
	log.write(str(pos1) +' '+ str(pos2) +'\n')
	log.close()

	cache = open('cache.txt','a')
	cache.write(str(pos1) +' '+ str(pos2) +'\n')
	cache.close()

def read_line():
	cache = open('cache.txt', 'r')
	read_instruction = str(cache.readline(50))
	if read_instruction != '':
		pos1, pos2 = read_instruction.split(') (')
		pos1, pos2 = pos1[1:].split(', '), pos2[:-2].split(', ')
		x1,y1 = float(pos1[0]), float(pos1[1])
		x2,y2 = float(pos2[0]), float(pos2[1])

		pos1, pos2 = (x1,y1), (x2,y2)
		cache.close()
		return True, pos1, pos2
	else:
		cache.close()
		return False, (0,0), (0,0)

def remove_line():
	cache = open('cache.txt', 'w')
	cache.write('')
	cache.close()



# write_line((100,2), (3300,50))

