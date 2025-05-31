# Importación de las librerías necesarias
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os

# Carga del modelo Keras (ruta relativa o absoluta según organización del proyecto)
model_path = os.path.join('modelo', 'static', 'keras', 'modelo_clasificador.keras')
model = load_model(model_path)

# Función para calcular el nivel de confianza de una imagen en memoria
def calcularImg(image_stream):
    """
    Calcula el nivel de confianza de una imagen usando un modelo Keras.

    Parámetros:
    ------------
    image_stream : BytesIO
        Flujo de datos de la imagen cargada (no archivo en disco).

    Retorna:
    --------
    float
        Porcentaje de predicción redondeado a 4 decimales.
    """
    img = Image.open(image_stream).convert("RGB").resize((150, 150))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    decToPorcent = prediction[0][0] * 100
    resultadoRedondeado = round(decToPorcent, 4)
    return resultadoRedondeado
