import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def M(x):
    return np.sum(x) / len(x)


n = 100
lattice_size = 5
n_test = 20
epochs = 5000

x = []
for i in range(n):
    lattice = np.random.choice([-1, 1], lattice_size)
    x.append(lattice)

x = np.array(x)
y = np.zeros(len(x))

for i in range(len(x)):
    y[i] = M(x[i])

y = [y]

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(lattice_size)))
model.add(tf.keras.layers.Dense(10, activation='tanh'))
model.add(tf.keras.layers.Dense(10, activation='tanh'))
model.add(tf.keras.layers.Dense(10, activation='tanh'))
model.add(tf.keras.layers.Dense(10, activation='tanh'))
model.add(tf.keras.layers.Dense(10, activation='tanh'))
model.add(tf.keras.layers.Dense(1, activation='tanh'))


model.compile(optimizer='adam', loss='mean_squared_error')

model.summary()

model.fit(x, y, epochs=epochs)

x_test = []
for i in range(n_test):
    lattice = np.random.choice([-1, 1], lattice_size)
    x_test.append(lattice)
x_test = np.array(x_test)

y_predict = model.predict(x_test)

with open("predictions.txt", 'w') as f:
    for i in range(len(x_test)):
        f.write('{}\t{:.4f}\t{:.4f}\n'.format(
            i, M(x_test[i]), y_predict[i][0]))
