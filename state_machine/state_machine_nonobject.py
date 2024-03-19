import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

current_state = "B"

state_A_num = 0
state_B_num = 1
state_C_num = 0

t_steps = 1000000

for t in tqdm(range(t_steps)):
    if (current_state == "A"):
        r = np.random.uniform(0, 1)
        if (r < 0.9):
            current_state = "A"
        elif (r >= 0.9 and r < (0.9 + 0.05)):
            current_state = "B"
        else:
            current_state = "C"
    elif (current_state == "B"):
        r = np.random.uniform(0, 1)
        if (r < 0.9):
            current_state = "B"
        elif (r >= 0.9 and r < (0.9 + 0.05)):
            current_state = "C"
        else:
            current_state = "A"
    elif (current_state == "C"):
        r = np.random.uniform(0, 1)
        if (r < 0.9):
            current_state = "C"
        elif (r >= 0.9 and r < (0.9 + 0.01)):
            current_state = "A"
        else:
            current_state = "B"

    if (current_state == "A"):
        state_A_num += 1
    if (current_state == "B"):
        state_B_num += 1
    if (current_state == "C"):
        state_C_num += 1

total = state_A_num + state_B_num + state_C_num
print("Total =", total)
print("A =", state_A_num, ", fraction =", round(state_A_num/total, 5))
print("B =", state_B_num, ", fraction =", round(state_B_num/total, 5))
print("C =", state_C_num, ", fraction =", round(state_C_num/total, 5))
