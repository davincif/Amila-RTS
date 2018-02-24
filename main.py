#python imports
import random
import time

#external libs imports
import pygame

#local imports
from world_map import wmap
from world_map.wmap import world_map

#information about the screen pygame.display.Info()
screen_info = None

#the diplay 'pygame.display.set_mode'
game_display = None

#game clock
clock = None

#game loop status
gl_running = None

#the game name
game_name = 'Amila RTS'

#the game frames per second
game_fps = 30


#initialize the needed libraries and the game modules
def game_init():
	global gl_running
	global screen_info
	global game_display
	global clock
	start_time = time.time()

	print('initializing...')

	#initialize libraries
	print('\tpygame...')
	pygame.init()
	print('\tdone')

	#initialize global variables
	gl_running = True
	screen_info = pygame.display.Info()
	game_display = pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
	pygame.display.set_caption(game_name)
	clock = pygame.time.Clock()
	random.seed()


	#initialize modules
	print('\tAmila modules...')
	world_map.preprint = '\t\t'
	world_map.init()
	print('\tdone')

	print('done in %f seconds\n' % (time.time() - start_time))

#deinitialize the needed libraries and the game modules
def game_quit():
	start_time = time.time()

	print('quiting...')

	#quiting libraries
	print('\tpygame...')
	pygame.quit()
	print('\tdone')

	#quiting modules
	print('\tAmila modules...')
	world_map.preprint = '\t\t'
	world_map.quit()
	print('\tdone')

	#quiting python itself
	print('done in %f\n' % (time.time() - start_time))
	quit()

def main():
	global screen_info
	global game_display
	global clock
	global gl_running
	global game_name
	global game_fps

	game_init()

	world_map.generate_map()

	# main loop
	while gl_running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gl_running = False;

		pygame.display.update()
		clock.tick(game_fps)

	game_quit()


if __name__ == '__main__':
	main()
