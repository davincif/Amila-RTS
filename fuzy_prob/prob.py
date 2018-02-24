from enum import Enum
import random

rand_range = 1000

__prob_correction = rand_range / 100

def flit_a_coin():
    return random.randint(1, rand_range)

def make_cdf(probs):
    if(type(probs) == dict):
        cdf = {}
        probsum = 0

        for key, value in probl.items():
            probsum += value * __prob_correction
            cdf[key] = probsum

        return cdf
    elif(type(probs) == list):
        cdf = []
        probsum = 0

        for prob in probs:
            probsum += prob * __prob_correction
            cdf.append(probsum)

        return cdf
    else:
        raise Exception('argument must be dict or list, but it ' + str(type(probs)))


###
# topick must be a list of value to be picked
# distribution must be list of cdf respecto to the topick list
###
def rand_pick(topick, distribution):
    picked = None
    coin = flit_a_coin()

    for count in range(0, len(distribution)):
        if(coin <= distribution[count]):
            picked = topick[count]
            break

    return picked


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
