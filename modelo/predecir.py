from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Carga del modelo Keras
model = load_model('keras\modelo_clasificador.keras')

def calcularImg(image_path):
    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    decToPorcent = (prediction[0][0])*100
    resultadoRedondeado = round(decToPorcent, 4)
    return(resultadoRedondeado)