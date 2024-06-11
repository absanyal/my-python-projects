import numpy as np
import matplotlib.pyplot as plt
from modules.conversions import base_to_decimal, decimal_to_base
from numpy import pi, cos, sin, sqrt, exp
from modules.conversions import decomp

max_val = 10
base = 3.4

target_vals = [i for i in
               np.linspace(0.1, max_val, 1000)]

with open('data.txt', 'w') as f:
    f.write('#b_10\t\t\tb_({:.8f})\n'.format(base))
    for target_val in target_vals:
        rep = decomp(target_val, base)
        f.write('{}\t\t\t{}\n'.format(
            target_val, ''.join([str(r) for r in rep])))
