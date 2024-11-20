# Usamos una imagen base de Python 3.9
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos todos los archivos del directorio actual (donde está el Dockerfile) al contenedor
COPY . .

# Instalamos las dependencias necesarias (en este caso Flask)
RUN pip install flask

# Exponemos el puerto en el que la aplicación se ejecutará
EXPOSE 5000

# Indicamos que el contenedor debe ejecutar app.py cuando se inicie
CMD ["python", "app.py"]
