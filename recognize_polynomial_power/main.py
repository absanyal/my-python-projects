from os import error
from matplotlib import tight_layout
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import layers, models, optimizers
from sklearn.model_selection import train_test_split
import math

def f(x, n):
    sum = 0.0
    for i in range(0, n+1):
        if (i == n):
            ci = 1
        else:
            ci = np.random.normal(1, 3)
        sum += ci * x**i
    return sum

data_set_size = 100000

n_labels = []
f_list = []

x_domain = np.linspace(-1, 1, 1000)

n_max = 10

for i in range(data_set_size):
    n = np.random.randint(1, n_max+1)
    n_labels.append(n)
    f_list.append(f(x_domain, n))

n_labels = np.array(n_labels)
f_list = np.array(f_list)

x_train, x_test, y_train, y_test = train_test_split(f_list, n_labels, test_size=0.2)

model = models.Sequential()
model.add(layers.Dense(128, activation='relu', input_shape=(1000,)))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=500, batch_size=512, validation_data=(x_test, y_test), verbose=0)

plt.figure(tight_layout=True)

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.savefig("plots/loss.png")

model.evaluate(x_test, y_test)

y_predict = model.predict(x_test)

correct=0
total=0
incorrect=0

tolerate = 0.45

isCorrect = 0

mean_error = 0

with open("data/results.txt", "w") as f:
    f.write("#Prediction\tActual\tError\tValidity\n")
    for i in enumerate(y_predict):
        prediction = i[1][0]
        actual = y_test[i[0]]
        if abs((prediction - actual)) < tolerate:
            correct += 1
            isCorrect = 1
        else:
            incorrect += 1
            isCorrect = 0
        total += 1
        
        error = abs((prediction - actual))
        
        # prediction = round(prediction, 0)
        
        f.write("{:.2f}\t{:2.0f}\t{:.2f}\t{}\n".format(prediction, actual, error, isCorrect))
        
        mean_error += ((prediction - actual)/actual)**2

mean_error = mean_error**0.5

print("Total: {}".format(total))
print("Correct: {}\t\t{:.2f} %".format(correct, correct/total*100))
print("Incorrect: {}\t\t{:.2f} %".format(incorrect, incorrect/total*100))
print("Mean Error: {:.2f} %".format(mean_error/total*100))

predicted_val, actual_val = np.loadtxt("data/results.txt", unpack=True, delimiter="\t", skiprows=1, usecols=(0, 1))

axislabels = np.arange(1, n_max+1, 1)

plt.figure(tight_layout=True, figsize=(10, 10))

plt.clf()
plt.cla()
plt.scatter(actual_val, predicted_val, s=2.0, c='blue', alpha=0.1)
plt.xlabel("Actual Value")
plt.ylabel("Predicted Value")
plt.yticks(axislabels)
plt.xticks(axislabels)
plt.grid(axis='both', linestyle='--')

y_truth = np.linspace(1, n_max, n_max)

plt.plot(y_truth, y_truth, color='red', linestyle='--', linewidth=1.0)

plt.savefig("plots/predictions.png")
    
