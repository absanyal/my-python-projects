import numpy as np
from modules.layer import layer
import numpy.linalg as la
from numpy.linalg import norm
from numpy import sqrt, pi, cos, sin


class filament:
    def __init__(self, num_monomers, monomer_diameter, start_pos, heading):
        self.__num_monomers = num_monomers
        self.__monomer_diameter = monomer_diameter
        self.__start_pos = np.array(start_pos)
        self.__heading = np.array(heading)

        self.__layers = []

        self.__generate_filament()

        self.__beads = []
        self.__num_beads = 0

        self.__generate_beads()

    def __generate_filament(self):
        l = layer(self.__monomer_diameter, self.__start_pos, self.__heading)
        self.__layers.append(l)

        for i in range(self.__num_monomers):
            l = l.make_next_layer()
            self.__layers.append(l)

    def __generate_beads(self):
        for li in range(1, len(self.__layers)):
            plist = np.zeros(3)
            for p in self.__layers[li].positions:
                p = np.array(p)
                plist += p
            for p in self.__layers[li - 1].positions:
                p = np.array(p)
                plist += p
            plist /= 8

            self.__beads.append(plist)
            self.__num_beads += 1

    @property
    def layers(self):
        return self.__layers

    @property
    def beads(self):
        return self.__beads

    @property
    def num_beads(self):
        return self.__num_beads
    
    @property
    def monomer_diameter(self):
        return self.__monomer_diameter
