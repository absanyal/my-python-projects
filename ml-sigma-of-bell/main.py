import numpy as np
import matplotlib.pyplot as plt
import modules.disttoplot as dtp
import tensorflow as tf
from tensorflow import keras
from keras import layers, models
from sklearn.model_selection import train_test_split


def N(A, mu, sigma, x):
    return A * np.exp(-((x-mu)**2) / (2 * sigma**2))


x_range = np.linspace(-10, 10, 1000)

data_set_size = 2000

sigma_list = []
data_set = []

A = 1.0
mu = 0.0

plt.figure(tight_layout=True)

for i in range(data_set_size):
    mu = np.random.uniform(-1, 1)
    A = np.random.uniform(0.01, 1)
    sigma = np.random.uniform(0.01, 3)
    curve = N(A, mu, sigma, x_range)
    curve = list(curve)
    data_set.append(curve)
    sigma_list.append(sigma)

    plt.plot(x_range, curve, alpha=0.1, color='k')

plt.savefig('plots/gaussian_curves.png')

x_train, x_test, y_train, y_test = train_test_split(
    data_set, sigma_list, test_size=0.1)

model = keras.Sequential(
    [
        layers.Dense(10, input_shape=(len(x_range),), activation='relu'),
        layers.Dense(8, activation='relu'),
        layers.Dense(5, activation='relu'),
        layers.Dense(5, activation='relu'),
        layers.Dense(5, activation='relu'),
        layers.Dense(3, activation='relu'),
        layers.Dense(1, activation='linear')
    ])

model.compile(loss=keras.losses.MeanSquaredError(),
              optimizer='adam', metrics=['accuracy'])

batch_size = 32
epochs = 100

training_history = {}
training_history['test'] = model.fit(
    x_train, y_train, epochs=epochs, validation_data=(x_test, y_test), verbose=0)

plt.clf()
plt.cla()

plt.plot(training_history['test'].history['loss'], label='loss')
plt.plot(training_history['test'].history['val_loss'], label='val_loss')
plt.legend()
plt.savefig('plots/loss.png')

y_pred = model.predict(x_test)

plt.clf()
plt.cla()

fit_x = np.linspace(min(y_test), max(y_test), 1000)
fit_y = fit_x

plt.plot(fit_x, fit_y, color='r', label='Truth line')
plt.scatter(y_test, y_pred, alpha=0.5, color='b', label='Test')
plt.xlabel('True sigma')
plt.ylabel('Predicted sigma')

# Extra tests
extra_test_set_size = 100
extra_test_set = []
extra_sigma_list = []
for i in range(extra_test_set_size):
    mu = np.random.uniform(-1, 1)
    A = np.random.uniform(0.01, 1)
    sigma = np.random.uniform(0.01, 3)
    curve = N(A, mu, sigma, x_range)
    curve = list(curve)
    extra_test_set.append(curve)
    extra_sigma_list.append(sigma)

extra_y_pred = model.predict(extra_test_set)

plt.scatter(extra_sigma_list, extra_y_pred, alpha=0.5, color='g', label='Extra test')



plt.legend()
plt.savefig('plots/prediction.png')