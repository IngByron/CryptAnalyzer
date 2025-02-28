# backend/db_connector.py
import pymysql
import psycopg2
import pyodbc
import sqlite3
from dotenv import load_dotenv
import os

# Cargar configuraciones desde el archivo .env
load_dotenv()

# Función para conectar a la base de datos
def conectar_db(motor_bd):
    if motor_bd == "mysql":
        # Conexión a MySQL/MariaDB
        return pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_NAME")
        )
    
    elif motor_bd == "postgresql":
        # Conexión a PostgreSQL
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME")
        )
    
    elif motor_bd == "sqlserver":
        # Conexión a SQL Server
        return pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=" + os.getenv("DB_HOST") + ";"
            "DATABASE=" + os.getenv("DB_NAME") + ";"
            "UID=" + os.getenv("DB_USER") + ";"
            "PWD=" + os.getenv("DB_PASSWORD")
        )
    
    elif motor_bd == "sqlite":
        # Conexión a SQLite
        return sqlite3.connect(os.getenv("DB_NAME"))
    
    else:
        raise ValueError("Motor de base de datos no soportado")

