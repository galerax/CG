import pygame
import loger
import os
from extra import view_converter

os.system('cd desktop/cg/projeto1/')


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()



w_width, w_height = 600, 400
vp_width, vp_height = 600, 400



engine_running = True

# VERIFYING EVENTS
def verify_quit(events):
	engine_running = True
	for event in events:
		if pygame.QUIT == event.type:
			engine_running = False

	return engine_running

def get_instruction(surface):
	flag, pos1, pos2 = loger.read_line()

	if flag == True:
		draw_line(pos1, pos2, surface)
		loger.remove_line()

def draw_line_direct(cord1, cord2, surface):
	x1, y1 = cord1
	x2,y2 = cord2

	pygame.draw.line(surface, 'green', (x1,y1), (x2,y2), 1)

def draw_line(cord1, cord2, surface):
	x1, y1 = cord1
	x2,y2 = cord2

	x1, y1 = view_converter.window_to_viewPort(x1, y1, w_width, w_height, vp_width, vp_height)
	x2, y2 = view_converter.window_to_viewPort(x2, y2, w_width, w_height, vp_width, vp_height)

	pygame.draw.line(surface, 'green', (x1,y1), (x2,y2), 1)

#OtherFuncs
def update_screen(screen, clock):
	clock.tick(60)
	pygame.display.update()



# GLOBAL LOOP
while engine_running:
	update_screen(screen, clock)
	pygame.display.update()
	global_events = pygame.event.get()
	engine_running = verify_quit(global_events)

	get_instruction(screen)

		
