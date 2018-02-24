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
		print(self.preprint + 'wmap from world_map...', end='')
		print(' done')

	def quit(self):
		print(self.preprint + 'wmap from world_map...', end='')
		print(' done')

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

		start_time = time.time()

		print('generating world map...', end='')

		bioma_cdf = prob.make_cdf(bioma_types.probtable)
		bioma_list = BiomaType.get_list()

		ix = 0
		heat = 0
		while ix < self.__map_x_size:
			line = []
			bio2gen = BiomaType.ANY

			iy = 0
			while iy < self.__map_y_size:

				if(heat == 0):
					heat = 100
					bio2gen = BiomaType(prob.rand_pick(bioma_list, bioma_cdf))
				else:
					coin = random.randint(1, 100)
					if(coin < heat):
						heat -= 3 + (max(bioma_types.probtable) - bioma_types.probtable[bio2gen.value])
					else:
						heat = 0
						bio2gen = BiomaType(prob.rand_pick(bioma_list, bioma_cdf))

				line.append(bio2gen)

				iy += 1

			self.__matrix.append(line)
			ix += 1

		self.__is_generated = True
		print(' done in %f seconds\n' % (time.time() - start_time), end='\n\n')


world_map = Wmap();

if __name__ == '__main__':
	Wmap.generate_map()
