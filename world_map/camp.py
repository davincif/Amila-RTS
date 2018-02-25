from world_map import bioma_types
from world_map.bioma_types import BiomaType

class Camp():
    __type = None
    __bioma = None

    def __init__(self, bioma):
        self.__bioma = bioma

    def get_bioma(self):
        return self.__bioma
