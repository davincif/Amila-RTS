from enum import Enum
from fuzy_prob import prob

import pygame


class BiomaType(Enum):
	#mark
	NOTHING = 0

	#main biomas
	HOT_DISERT = 1
	COLD_DISERT = 2
	HILLY = 3
	PLAINS = 4
	FLOREST = 5
	SWAMPY = 6

	#trasition biomas
	ARID = 7
	TUNDRA = 8
	PRAIRIE = 9

	#mark
	ANY = 10

	def __str__(self):
		return self.name

	def get_list():
		return [bio.value for bio in BiomaType]

	def get_dict():
		bio2ret = {}
		for bio in BiomaType:
			bio2ret[bio.value] = bio

		return bio2ret


prob_table = {
	BiomaType.ANY: {
		BiomaType.HOT_DISERT: 5.6,
		BiomaType.COLD_DISERT: 5.6,
		BiomaType.HILLY: 13,
		BiomaType.PLAINS: 16,
		BiomaType.FLOREST: 16,
		BiomaType.SWAMPY: 13,
		BiomaType.ARID: 8.8,
		BiomaType.TUNDRA: 12,
		BiomaType.PRAIRIE: 10,
	},

	BiomaType.HOT_DISERT: {
		BiomaType.HOT_DISERT: 60,
		BiomaType.COLD_DISERT: 0,
		BiomaType.HILLY: 0,
		BiomaType.PLAINS: 0,
		BiomaType.FLOREST: 0,
		BiomaType.SWAMPY: 0,
		BiomaType.ARID: 22,
		BiomaType.TUNDRA: 0,
		BiomaType.PRAIRIE: 18,
	},

	BiomaType.COLD_DISERT: {
		BiomaType.HOT_DISERT: 0,
		BiomaType.COLD_DISERT: 60,
		BiomaType.HILLY: 10,
		BiomaType.PLAINS: 0,
		BiomaType.FLOREST: 5,
		BiomaType.SWAMPY: 0,
		BiomaType.ARID: 0,
		BiomaType.TUNDRA: 18,
		BiomaType.PRAIRIE: 7,
	},

	BiomaType.HILLY: {
		BiomaType.HOT_DISERT: 4,
		BiomaType.COLD_DISERT: 2,
		BiomaType.HILLY: 68,
		BiomaType.PLAINS: 3,
		BiomaType.FLOREST: 6,
		BiomaType.SWAMPY: 4,
		BiomaType.ARID: 6,
		BiomaType.TUNDRA: 6,
		BiomaType.PRAIRIE: 1,
	},

	BiomaType.PLAINS: {
		BiomaType.HOT_DISERT: 4,
		BiomaType.COLD_DISERT: 3,
		BiomaType.HILLY: 4,
		BiomaType.PLAINS: 70,
		BiomaType.FLOREST: 6,
		BiomaType.SWAMPY: 5,
		BiomaType.ARID: 4,
		BiomaType.TUNDRA: 1,
		BiomaType.PRAIRIE: 3,
	},

	BiomaType.FLOREST: {
		BiomaType.HOT_DISERT: 0,
		BiomaType.COLD_DISERT: 2,
		BiomaType.HILLY: 5,
		BiomaType.PLAINS: 7,
		BiomaType.FLOREST: 68,
		BiomaType.SWAMPY: 8,
		BiomaType.ARID: 2,
		BiomaType.TUNDRA: 4,
		BiomaType.PRAIRIE: 4,
	},

	BiomaType.SWAMPY: {
		BiomaType.HOT_DISERT: 0,
		BiomaType.COLD_DISERT: 0,
		BiomaType.HILLY: 5,
		BiomaType.PLAINS: 10,
		BiomaType.FLOREST: 7,
		BiomaType.SWAMPY: 68,
		BiomaType.ARID: 2,
		BiomaType.TUNDRA: 2,
		BiomaType.PRAIRIE: 6,
	},

	BiomaType.ARID: {
		BiomaType.HOT_DISERT: 10,
		BiomaType.COLD_DISERT: 0,
		BiomaType.HILLY: 2,
		BiomaType.PLAINS: 4,
		BiomaType.FLOREST: 4,
		BiomaType.SWAMPY: 2,
		BiomaType.ARID: 68,
		BiomaType.TUNDRA: 2,
		BiomaType.PRAIRIE: 8,
	},

	BiomaType.TUNDRA: {
		BiomaType.HOT_DISERT: 0,
		BiomaType.COLD_DISERT: 8,
		BiomaType.HILLY: 11,
		BiomaType.PLAINS: 5,
		BiomaType.FLOREST: 6,
		BiomaType.SWAMPY: 1,
		BiomaType.ARID: 0,
		BiomaType.TUNDRA: 68,
		BiomaType.PRAIRIE: 1,
	},

	BiomaType.PRAIRIE: {
		BiomaType.HOT_DISERT: 6,
		BiomaType.COLD_DISERT: 0,
		BiomaType.HILLY: 4,
		BiomaType.PLAINS: 6,
		BiomaType.FLOREST: 6,
		BiomaType.SWAMPY: 6,
		BiomaType.ARID: 4,
		BiomaType.TUNDRA: 0,
		BiomaType.PRAIRIE: 68,
	},
}

cdf_table = {
	BiomaType.ANY: None,
	BiomaType.HOT_DISERT: None,
	BiomaType.COLD_DISERT: None,
	BiomaType.HILLY: None,
	BiomaType.PLAINS: None,
	BiomaType.FLOREST: None,
	BiomaType.SWAMPY: None,
	BiomaType.ARID: None,
	BiomaType.TUNDRA: None,
	BiomaType.PRAIRIE: None,
}

img_dir = {
	BiomaType.HOT_DISERT: 'imgs/' + BiomaType.HOT_DISERT.name.lower() + '.png',
	BiomaType.COLD_DISERT: 'imgs/' + BiomaType.COLD_DISERT.name.lower() + '.png',
	BiomaType.HILLY: 'imgs/' + BiomaType.HILLY.name.lower() + '.png',
	BiomaType.PLAINS: 'imgs/' + BiomaType.PLAINS.name.lower() + '.png',
	BiomaType.FLOREST: 'imgs/' + BiomaType.FLOREST.name.lower() + '.png',
	BiomaType.SWAMPY: 'imgs/' + BiomaType.SWAMPY.name.lower() + '.png',
	BiomaType.ARID: 'imgs/' + BiomaType.ARID.name.lower() + '.png',
	BiomaType.TUNDRA: 'imgs/' + BiomaType.TUNDRA.name.lower() + '.png',
	BiomaType.PRAIRIE: 'imgs/' + BiomaType.PRAIRIE.name.lower() + '.png'
}

img = None

def cdf_table_update():
	for key, value in cdf_table.items():
		cdf_table[key] = prob.make_cdf(prob_table[key])

def init():
	global img

	cdf_table_update()

	img = {
		BiomaType.HOT_DISERT: pygame.image.load(img_dir[BiomaType.HOT_DISERT]),
		BiomaType.COLD_DISERT: pygame.image.load(img_dir[BiomaType.COLD_DISERT]),
		BiomaType.HILLY: pygame.image.load(img_dir[BiomaType.HILLY]),
		BiomaType.PLAINS: pygame.image.load(img_dir[BiomaType.PLAINS]),
		BiomaType.FLOREST: pygame.image.load(img_dir[BiomaType.FLOREST]),
		BiomaType.SWAMPY: pygame.image.load(img_dir[BiomaType.SWAMPY]),
		BiomaType.ARID: pygame.image.load(img_dir[BiomaType.ARID]),
		BiomaType.TUNDRA: pygame.image.load(img_dir[BiomaType.TUNDRA]),
		BiomaType.PRAIRIE: pygame.image.load(img_dir[BiomaType.PRAIRIE])
	}

def quit():
	pass

def nextBioma(currentb):
	bio = BiomaType.NOTHING

	if(currentb == BiomaType.NOTHING):
		bio = BiomaType.ANY
	else:
		for rule in rules:
			if(rule[0] == currentb or rule[1] == currentb):
				bio = rule[2]
				break

	return bio
