from world_map.camp_types import CampType
from world_map.bioma_types import BiomaType

class Camp():
    __type = None
    __bioma = None

    def __init__(self, bioma):
        self.__bioma = bioma
