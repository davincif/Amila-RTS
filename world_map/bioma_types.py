from enum import Enum

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


rules = [
    # (A, B, C) -> from A to B must have C
    # (A, B, C) -> from B to A must have C
    (BiomaType.HOT_DISERT, BiomaType.COLD_DISERT, BiomaType.ANY),
    (BiomaType.HOT_DISERT, BiomaType.ANY, BiomaType.PRAIRIE),
    (BiomaType.COLD_DISERT, BiomaType.HILLY, BiomaType.TUNDRA),
    (BiomaType.COLD_DISERT, BiomaType.FLOREST, BiomaType.TUNDRA),
    (BiomaType.COLD_DISERT, BiomaType.SWAMPY, BiomaType.PRAIRIE),
    (BiomaType.HILLY, BiomaType.SWAMPY, BiomaType.FLOREST),
    (BiomaType.PLAINS, BiomaType.HILLY, BiomaType.FLOREST),
]

probtable = [
	#mask
	0,

	#main biomas
	5.6, 5.6, 13, 16, 16, 13,

	#trasition biomas
	8.8, 12, 10,

	#mask
	0
]

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

def init():
	global img
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
