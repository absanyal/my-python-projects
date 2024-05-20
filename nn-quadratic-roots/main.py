import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

b, c, x1, x2 = np.loadtxt('quadratic_data.txt', skiprows=1, unpack=True, usecols=(1, 2, 3, 4))

parameters = np.column_stack((b, c))
solutions = np.column_stack((x1, x2))

X_train, X_test, y_train, y_test = train_test_split(parameters, solutions, test_size=0.05)

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(2,), activation='relu'),
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(2, activation='leaky_relu')
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=100)

loss = model.evaluate(X_test, y_test)

print("Loss: ", loss)

Y_pred = model.predict(X_test)

with open('quadratic_results.txt', 'w') as f:
    f.write("#a\tb\tc\tx1\tx2\tx1_pred\tx2_pred\n")
    for i in range(len(y_test)):
        f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format("1.0", X_test[i][0], X_test[i][1], y_test[i][0], y_test[i][1], Y_pred[i][0], Y_pred[i][1]))
