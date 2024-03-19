import numpy as np
import matplotlib.pyplot as plt

T = 2
beta = 1/T

E = -5.0


class filament:
    def __init__(self):
        self.pos = 0
        self.connected = 0
        self.steps_performed = 0
        self.num_attempts = 0
        self.num_attached = 0
        self.num_drifted = 0
        self.num_too_long = 0

    def move(self):
        self.pos += np.random.choice([-1, 1])
        self.steps_performed += 1

    def check_collision(self, threshold):
        if self.pos == threshold:
            self.connected = 1
        else:
            self.connected = 0

    def reset(self):
        self.pos = 0
        self.connected = 0
        self.steps_performed = 0


n = 5000

t_list = []
f = filament()

t_max = 200

wall = -3

bins_list = []
bin_val = 0
while bin_val < t_max+1:
    bins_list.append(bin_val)
    bin_val += 1

with open('linker-attachment-out.txt', 'w') as out, open('linker-attachment-time.txt', 'w') as data:
    for i in range(n):
        f.reset()
        f.num_attempts += 1
        while f.connected == 0:
            f.move()
            f.check_collision(wall)
            if f.pos > 5 * abs(wall):
                out.write("F {}/{} drifted away\n".format(i+1, n))
                f.num_drifted += 1
                break
            if f.steps_performed > t_max:
                out.write("F {}/{} took too long\n".format(i+1, n))
                f.num_too_long += 1
                break
            if f.connected == 1:
                t_list.append(f.steps_performed)
                f.num_attached += 1
                out.write("F {}/{} attached at t = {}\n".format(i+1, n, f.steps_performed))
                data.write("{}\n".format(f.steps_performed))
        
        with open('linker-attachment-time-stats.txt', 'w') as stats:
            stats.write(
                "Mean attachment time: {:.4f}\n".format(np.mean(t_list)))
            stats.write(
                "Standard deviation: {:.4f}\n".format(np.std(t_list)))
            stats.write(
                "Number of attempts: {}\n".format(f.num_attempts))
            stats.write(
                "Number of attachments: {}, {:.4f} %\n".format(
                f.num_attached, f.num_attached/f.num_attempts*100))
            stats.write(
                "Number drifted away: {}, {:.4f} %\n".format(
                f.num_drifted, f.num_drifted/f.num_attempts*100))
            stats.write(
                "Number took too long: {}, {:.4f} %\n".format(
                f.num_too_long, f.num_too_long/f.num_attempts*100))
