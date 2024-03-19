import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def test_function(x):
    if (x < 0):
        return -np.sin(10*x)
    elif (x >= 0):
        return 5*x


# Generate some random data points
x = np.random.uniform(-2, 2, 500)
y = np.zeros(len(x))

x_test = np.linspace(-2, 2, 1000)


for i in range(len(x)):
    y[i] = test_function(x[i]) + 0.1 * np.random.uniform(-1, 1)

# Define the polynomial regression model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(20, activation='relu', input_shape=[1]),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError(),
              metrics=['mean_absolute_error'])

# Train the model
model.fit(x, y, epochs=5000, verbose=1)

# Make predictions
y_pred = model.predict(x_test)

# Plot the original points and the fitted polynomial curve
plt.scatter(x, y, alpha=1)
plt.scatter(x_test, y_pred, color='red', alpha=0.5, s=3)
plt.show()
