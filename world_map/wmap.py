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

	def draw(self, display):
		ii = 0
		while ii < self.__map_y_size:

			ij = 0
			while ij < self.__map_x_size:
				display.blit(bioma_types.img[self.__matrix[ii][ij].get_bioma()], (ij*50, ii*50))

				ij += 1

			ii += 1

	def generate_map(self):
		if(self.__is_generated):
			raise Exception('map is already generated')

		start_time = time.time()

		print('generating world map...', end='')

		bioma_cdf = prob.make_cdf(bioma_types.probtable)
		bioma_list = BiomaType.get_list()

		ii = 0
		heat = 0
		heatmatrix = []
		while ii < self.__map_y_size:
			line = []
			heatline = []

			if(ii > 0):
				heat = heatmatrix[ii-1][0]
				bio2gen = self.__matrix[ii-1][0]
			else:
				bio2gen = BiomaType.ANY

			ij = 0
			while ij < self.__map_x_size:

				if(heat == 0):
					heat = 100
					bio2gen = Camp(BiomaType(prob.rand_pick(bioma_list, bioma_cdf)))
				else:
					coin = random.randint(1, 100)
					if(coin < heat):
						heat -= 3 + (max(bioma_types.probtable) - bioma_types.probtable[bio2gen.get_bioma().value])
					else:
						heat = 0
						bio2gen = Camp(BiomaType(prob.rand_pick(bioma_list, bioma_cdf)))

				line.append(bio2gen)
				heatline.append(heat)
				ij += 1

			self.__matrix.append(line)
			heatmatrix.append(heatline)
			ii += 1

		self.__is_generated = True
		print(' done in %f seconds\n' % (time.time() - start_time), end='\n\n')


world_map = Wmap();

if __name__ == '__main__':
	Wmap.generate_map()
