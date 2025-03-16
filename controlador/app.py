# Importar librerias necesarias
from flask import Flask, render_template, request, send_from_directory
import os 

#Importar metodo para predecir el cancer
from modelo.predecir import calcularImg

# Definir nueva ruta de template
template_dir = os.path.abspath('vista')
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():
    return render_template("base.html")

# Definir ruta de almacenamiento
UPLOAD_FOLDER = os.getenv("TMPDIR", "/tmp")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/convertir", methods=['POST'])


def getImg():
    archivo = request.files['archivo']
    ruta_guardado = os.path.join(UPLOAD_FOLDER, "temp.png")
    archivo.save(ruta_guardado)
    numCal = calcularImg(ruta_guardado)
    return render_template('base.html', num = numCal)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)