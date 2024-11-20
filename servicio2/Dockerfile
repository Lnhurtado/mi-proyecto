FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia todos los archivos de la carpeta actual al contenedor
COPY . .

# Copia el script wait-for-it.sh y le da permisos de ejecución
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Instala las dependencias desde el archivo requirements.txt
RUN pip install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Ejecuta wait-for-it.sh y luego el script de la app, luego mantiene el contenedor activo
CMD bash -c "/wait-for-it.sh servicio1:5000 -- python app.py && tail -f /dev/null"
