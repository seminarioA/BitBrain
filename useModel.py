from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

model = load_model("""[COLOQUE LA RUTA DEL MODELO PREENTRENADO]""")

image_path = """[COLOQUE LA RUTA DE LA IMAGEN A EVALUAR]"""

img = load_img(image_path, target_size=(150, 150))
img_array = img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

if prediction[0][0] > 0.9:
    print(prediction[0][0])
    print("El paciente tiene cancer")
else:
    print(prediction[0][0])
    print("El paciente NO tiene cancer")
