import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import git Adam
from tensorflow.keras.utils import to_categorical
import pandas as pd

# Parameters
learning_rate = 0.001
num_epochs = 10
batch_size = 100

# Load and preprocess MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Build MLP model
model = Sequential([
    Input(shape=(784,)),
    Dense(512, activation='relu'),
    Dense(256, activation='relu'),
    Dense(10)  # logits (no softmax here, since from_logits=True in loss)
])

# Compile model
model.compile(
    optimizer=Adam(learning_rate),
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    metrics=['accuracy']
)

# Train the model
model.fit(x_train, y_train, epochs=num_epochs, batch_size=batch_size, validation_data=(x_test, y_test))

# Evaluate on test data
loss, acc = model.evaluate(x_test, y_test)
print(f"\nFinal Test Accuracy: {acc*100:.2f}%")
print(f"TensorFlow Version: {tf.__version__}")

# 학번 출력 예제
data = {
    '이름': ['김가은'],
    '학번': [2410310],
    '학과': ['소프트웨어학부']
}
df = pd.DataFrame(data)
print("\n학생 정보:")
print(df)
