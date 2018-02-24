from enum import Enum
import random

maxnum = 1000

def flit_a_coin():
    return random.randint(0, maxnum)

class Prob():

    ALWAYS = 1000
    EXTREMELY_COMMOM = 900
    VERY_COMMOM = 700
    COMMOM = 500
    UNCOMMOM = 300
    RARE = 150
    VERY_RARE = 75
    EXTREMELY_RARE = 40
    NEVER = 0

    def fuzify(self, value):
        if(value == self.NEVER):
            return self.NEVER
        elif(value <= self.EXTREMELY_RARE):
            return self.EXTREMELY_RARE
        elif(value <= self.VERY_RARE):
            return self.VERY_RARE
        elif(value <= self.RARE):
            return self.RARE
        elif(value <= self.UNCOMMOM):
            return self.UNCOMMOM
        elif(value <= self.COMMOM):
            return self.COMMOM
        elif(value <= self.VERY_COMMOM):
            return self.VERY_COMMOM
        elif(value <= self.EXTREMELY_COMMOM):
            return self.EXTREMELY_COMMOM
        elif(value > self.EXTREMELY_COMMOM):
            return self.ALWAYS
