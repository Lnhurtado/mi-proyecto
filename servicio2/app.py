from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Solicitar al servicio1
        response = requests.get("http://servicio1:5000")
        return f"Respuesta desde servicio1: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con servicio1: {e}"

if __name__ == '__main__':
    # Ejecutar Flask en el puerto 5001
    app.run(host='0.0.0.0', port=5001)

