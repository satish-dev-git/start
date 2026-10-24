import tensorflow as tf

print("TensorFlow Version:", tf.__version__)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(5,)),
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1)
])

print("AI Model Created Successfully")