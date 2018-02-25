import time
import random

from world_map.camp import Camp
from world_map.bioma_types import BiomaType
from world_map import bioma_types
from fuzy_prob.prob import Prob
from fuzy_prob import prob

class Wmap():
	preprint = None

	__map_x_size = 100
	__map_y_size = 100
	__is_generated = False
	__matrix = [] #world mape matriz

	def __init__(self):
		pass

	def init(self):
		print(self.preprint + 'wmap from world_map...',)

		print(self.preprint + "\tbioma_types...")
		bioma_types.init()
		print(self.preprint + "\tdone")

		print(self.preprint + ' done')

	def quit(self):
		print(self.preprint + 'wmap from world_map...')

		print(self.preprint + "\tbioma_types...")
		bioma_types.quit()
		print(self.preprint + "\tdone")

		print(self.preprint + ' done')

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

	def draw(self, display, screen_info):
		ii = 0
		while ii < self.__map_y_size:

			iiprint = ii*50
			if(iiprint < screen_info.current_h):
				ij = 0
				while ij < self.__map_x_size:
					ijprint = ij*50
					if(ijprint < screen_info.current_w):
						display.blit(bioma_types.img[self.__matrix[ii][ij].get_bioma()], (ijprint, iiprint))

						ij += 1
					else:
						break

				ii += 1
			else:
				break

	def generate_map(self):
		if(self.__is_generated):
			raise Exception('map is already generated')

		start_time = time.time()

		print('generating world map...', end='')

		biomas = BiomaType.get_dict()

		ii = 0
		while ii < self.__map_y_size:
			line = []

			bio2gen = Camp(BiomaType.ANY)
			ij = 0
			while ij < self.__map_x_size:
				if(ii > 0):
					bio2gen = self.__matrix[ii-1][0]

				bio2gen = Camp(prob.rand_pick(biomas, bioma_types.cdf_table[bio2gen.get_bioma()]))

				line.append(bio2gen)
				ij += 1

			self.__matrix.append(line)
			ii += 1

		self.__is_generated = True
		print(' done in %f seconds\n' % (time.time() - start_time), end='\n\n')


world_map = Wmap();

if __name__ == '__main__':
	Wmap.generate_map()
