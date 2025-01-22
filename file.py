from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_data = train_datagen.flow_from_directory(
    '/content/drive/MyDrive/CANCER DETECTION',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training'
)
val_data = train_datagen.flow_from_directory(
    '/content/drive/MyDrive/CANCER DETECTION',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Paso 2: Definición de la arquitectura del modelo CNN
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_data,
    epochs=20,
    validation_data=val_data
)

test_loss, test_accuracy = model.evaluate(val_data)
print(f"Precisión en validación: {test_accuracy * 100:.2f}%")

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Precisión en entrenamiento')
plt.plot(history.history['val_accuracy'], label='Precisión en validación')
plt.xlabel('Epocas')
plt.ylabel('Precisión')
plt.legend()
plt.show()

model.save('modelo_clasificador.h5')

from tensorflow.keras.models import load_model

model = load_model('modelo_clasificador.h5')
