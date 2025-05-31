from flask import Flask, render_template, request
from io import BytesIO
from modelo.predecir import calcularImg

app = Flask(__name__, template_folder='vista')

@app.route("/")
def index():
    """Renderiza la página principal."""
    return render_template("base.html")

@app.route("/convertir", methods=['POST'])
def getImg():
    """
    Procesa una imagen enviada por el cliente sin almacenarla en disco.
    
    Utiliza un flujo de memoria para calcular el resultado.
    """
    archivo = request.files['archivo']
    contenido = archivo.read()
    imagen_memoria = BytesIO(contenido)
    numCal = calcularImg(imagen_memoria)
    return render_template('base.html', num=numCal)

if __name__ == "__main__":
    app.run(debug=True)