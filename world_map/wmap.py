import pygame

from world_map.camp import Camp
from fuzy_prob.prob import Prob
from fuzy_prob import prob

class Wmap():
	preprint = None

	__map_x_size = 10
	__map_y_size = 10
	__is_generated = False
	__matrix = [] #world mape matriz

	def __init__(self):
		pass

	def init(self):
		print(self.preprint + 'wmap from world_map...')

	def quit(self):
		print(self.preprint + 'wmap from world_map...')

	def def_map_xy(self, mapx, mapy):
        # argument type check
		if(self.__is_generated):
			raise Exception('map already generated')
		elif(type(mapx) != int or type(mapy) != int):
			raise TypeError('arguments just be int, but the are: ' + str(type(mapx)) + str(type(mapy)) )
		elif(mapx <= 0 or mapy <= 0):
			raise Exception('map size should be positive')

		self.__map_x_size = mapx
		self.__map_y_size = mapy

	def generate_map(self):
		if(self.__is_generated):
			raise Exception('map is already generated')

		self.__is_generated = True

		print('generating world map...', end='')
		for ix in range(self.__map_x_size):
			line = []
			for iy in range(self.__map_y_size):
				coin = prob.flit_a_coin()
				line.append(coin)
			self.__matrix.append(line)
		print(' done', end='\n\n')

world_map = Wmap();

if __name__ == '__main__':
	Wmap.generate_map()
