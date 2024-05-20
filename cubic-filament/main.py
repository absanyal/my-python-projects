from math import cos, sqrt, sin
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
from numpy.linalg import norm
from modules.filament import filament
from modules.makexyz import dump_filament
from modules.positions import get_frame
from modules.bonds import join_frame

num_monomers = 10

monomer_diameter = 1
a = monomer_diameter


filament_list = []

# theta = 45
# theta = np.radians(theta)
# start_pos = np.array([0, 0, 0])
# heading = [0, -cos(theta), -sin(theta)]
# f = filament(num_monomers, monomer_diameter, start_pos, heading)
# filament_list.append(f)

# theta = -20
# theta = np.radians(theta)
# start_pos = np.array([-30, 10, 30])
# heading = [0, -cos(theta), -sin(theta)]
# f = filament(num_monomers, monomer_diameter, start_pos, heading)
# filament_list.append(f)

num_monomers = 3
theta = 0
theta = np.radians(theta)
start_pos = np.array([0, 0, 0])
# heading = [0, -cos(theta), -sin(theta)]
heading = [0, 0, 1]
f1 = filament(num_monomers, monomer_diameter, start_pos, heading)
# filament_list.append(f)

# for i_pos, pos in enumerate(pos_list):
#     print("Atom {} at position {}".format(i_pos, pos))

atom_type_template = [1, 2, 3, 4]

join_frame(f1, 0, 0)

# dump_filament("filament.xyz", filament_list, 1)
