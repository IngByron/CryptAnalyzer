# backend/routes.py
from flask import Blueprint, request, jsonify
from db_connector import conectar_db
from hash_identifier import detectar_cifrado

bp = Blueprint('routes', __name__)

# Endpoint para conectar a la base de datos
@bp.route('/conectar', methods=['POST'])
def conectar():
    try:
        # Obtener parámetros del request
        motor_bd = request.json.get('motor_bd')
        
        # Conectar a la base de datos con el motor seleccionado
        conn = conectar_db(motor_bd)
        
        # Si la conexión fue exitosa, respondemos con éxito
        return jsonify({"message": f"Conexión exitosa a {motor_bd}"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@bp.route('/analizar', methods=['POST'])
def analizar():
    try:
        # Obtener datos del request
        datos = request.json
        tabla = datos.get('tabla')
        columna = datos.get('columna')
        motor_bd = datos.get('motor_bd')

        if not tabla or not columna:
            return jsonify({"error": "Debe proporcionar tabla y columna"}), 400
        
        # Validamos si 'tabla' o 'columna' no son identificadores válidos
        invalid_fields = []

        # Verificamos 'tabla'
        if not tabla.isidentifier():
            invalid_fields.append(f"tabla ({tabla})")

        # Verificamos 'columna'
        if not columna.isidentifier():
            invalid_fields.append(f"columna ({columna})")

        # Si hay campos inválidos, lanzamos la excepción con los nombres
        if invalid_fields:
            raise ValueError(f"Nombre(s) inválido(s): " + ", ".join(invalid_fields))

        # Conectar a la base de datos
        conn = conectar_db(motor_bd)
        cursor = conn.cursor()

        # Construir consulta segura
        # Lógica para la consulta dependiendo del motor de base de datos
        if motor_bd == 'mysql':
            query = f"SELECT {columna} FROM {tabla} WHERE {columna} IS NOT NULL"
            cursor.execute(query)
        
        elif motor_bd == 'postgresql':
            query = f"SELECT {columna} FROM {tabla} WHERE {columna} IS NOT NULL"
            cursor.execute(query)

        elif motor_bd == 'mssql': 
            query = f"SELECT {columna} FROM {tabla} WHERE {columna} IS NOT NULL"
            cursor.execute(query)

        elif motor_bd == 'sqlite':
            query = f"SELECT {columna} FROM {tabla} WHERE {columna} IS NOT NULL"
            cursor.execute(query)
        
        else:
            return jsonify({"error": "Motor de base de datos no soportado"}), 400
        resultados = cursor.fetchall()
        conn.close()

        # Analizar cada contraseña
        analisis = []
        for (password,) in resultados:
            tipo_cifrado = detectar_cifrado(password)
            analisis.append({"password": password, "tipo_cifrado": tipo_cifrado})

        return jsonify({"analisis": analisis}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/', methods=['GET'])
def home():
    return "Bienvenido a HashScan!"

