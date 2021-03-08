import loger
import os
os.system('cd desktop/cg/projeto1/')
#TERMINAL BASIC FUNCS

def terminalDrawLine():
	pos1 = input('Insert x1, y1:').split(' ')
	pos2 = input('Insert x2, y2:').split(' ')
	x1, y1 = float(pos1[0]), float(pos1[1])
	x2, y2 = float(pos2[0]), float(pos2[1])
	pos1,pos2 = (x1,y1), (x2, y2)
	loger.write_line(pos1, pos2)





while True:
	print("Welcome to the engine's console")
	command = input("...")

	if command == 'terminalDrawLine':
		terminalDrawLine()

	os.system('cls')



#Terminal Complex Funcs

