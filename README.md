# BitBrain

BitBrain es una herramienta avanzada para la clasificación de imágenes de resonancia magnética (MRI) de pacientes, diseñada para identificar casos de cáncer cerebral con una efectividad del 99%. Este proyecto fue desarrollado por el Científico de Datos Alejandro Seminario en septiembre de 2024, utilizando técnicas de aprendizaje profundo y redes neuronales convolucionales (CNNs).


## Descripción del Proyecto

El objetivo principal de BitBrain es asistir a los profesionales médicos en el diagnóstico temprano del cáncer cerebral, utilizando un modelo de Red Neuronal Convolucional (CNN) de nueve capas, diseñado específicamente para analizar imágenes de MRI y clasificarlas en dos categorías principales:
Pacientes con cáncer cerebral.
Pacientes sanos.

### Características Principales

Precisión del Modelo: 99% en datos de prueba.
Arquitectura del Modelo: 9 capas optimizadas para extracción y clasificación de características visuales.
Lenguaje de Programación: Python.
Implementación Modular: Código diseñado para facilitar mejoras futuras y personalización.

## Dataset
El modelo fue entrenado utilizando un conjunto de datos compuesto por 800 imágenes de resonancia magnética (MRI), distribuidas de la siguiente manera:

- 392 imágenes: Pacientes con casos confirmados de cáncer cerebral.
- 408 imágenes: Pacientes sanos.

| MRI - PACIENTES ENFERMOS | MRI - PACIENTES SANOS |
|----------|----------|
| [![pacientesano.gif](https://i.postimg.cc/DzzTQq6P/ezgif-5-ded7e010fc.gif)](https://postimg.cc/RW2y4JjW) | [![cancercerebral.gif](https://i.postimg.cc/RVf8MjYH/ezgif-com-optimize.gif)](https://github.com/seminarioA/TensorBrain/tree/6df1896473fa60c7e2c300e40e99cabc02e2833d/dataSet) |
| 392 imagenes | 408 imagenes |


### Procesamiento del Dataset
1. Escalado: Dimensiones de las imágenes uniformes (150x150 píxeles).
2. Normalización: Valores de píxeles ajustados a un rango de 0-1.
3. División de Datos:
- Entrenamiento: 70%.
- Validación: 20%.
- Pruebas: 10%.


## Arquitectura del Modelo
El clasificador de BitBrain utiliza la siguiente arquitectura:

1. Capas Convolucionales: Tres bloques de capas convolucionales y de pooling para extracción de características.
2. Capas Densas:
- Una capa totalmente conectada con 128 neuronas y activación ReLU.
- Una capa de salida con activación sigmoide para la clasificación binaria.
4. Regularización: Se utilizó Dropout para prevenir el sobreajuste.
