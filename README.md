📌 Descripción

HashScan es una herramienta para identificar el tipo de cifrado utilizado en bases de datos. Permite conectarse a distintos motores de bases de datos y analizar columnas específicas para determinar el tipo de hash almacenado.

🚀 Instalación y Configuración

1️⃣ Crear archivo .env en el backend

Antes de ejecutar la aplicación, es necesario configurar un archivo .env en la carpeta backend con los parámetros de conexión a la base de datos.

Ejemplo de .env:

DB_HOST=tu_localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=tu_nombre_base_datos

2️⃣ Instalar dependencias

Desde la carpeta backend, instala las dependencias requeridas:

pip install -r requirements.txt

3️⃣ Levantar el servidor

Ejecuta el siguiente comando para iniciar el backend con Flask dentro de la carpeta Backend:

python app.py

🔍 Uso de la API con Postman

Puedes probar las funcionalidades de HashScan utilizando Postman o cualquier cliente REST.

1️⃣ Comprobar conexión a la base de datos

Endpoint: POST /conectar

Los motores de base de datos soportados son: "mysql", "postgresql", "sqlserver", "sqlite"

Ejemplo de solicitud:

{
    "motor_bd": "mysql"
}

Respuesta esperada:

{
    "message": "Conexión exitosa a mysql"
}

2️⃣ Analizar una columna de la base de datos

Endpoint: POST /analizar

Ejemplo de solicitud:

{
  "tabla": "tu_tabla_usuarios",
  "columna": "tu_columna_contraseña",
  "motor_bd": "tu_motor_de_base_de_datos"
}

Respuesta esperada:

{
    "analisis": [
        {
            "password": "482c811da5d5b4bc6d497ffa98491e38",
            "tipo_cifrado": "MD5 (Inseguro)"
        },
        {
            "password": "$2a$12$LJYbfgkjlBk/O3qDNF5QFe8ztgFqzqUkpNhAqj3txYeiv.QalwQJ2",
            "tipo_cifrado": "Bcrypt (Seguro)"
        }
    ]
}

