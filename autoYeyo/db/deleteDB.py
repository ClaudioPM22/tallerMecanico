import mysql.connector
from configDB import DB_USER, DB_PASSWORD, DB_HOST,DB_NAMEDB

def drop_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        
        # Eliminar la base de datos si existe
        cursor.execute(f"DROP DATABASE IF EXISTS {database}")
        print("Base de datos eliminada correctamente.")

    except mysql.connector.Error as error:
        print("Error al eliminar la base de datos:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")

# Configuración de la conexión a la base de datos
host = DB_HOST
user = DB_USER
password = DB_PASSWORD
database = DB_NAMEDB

# Eliminar la base de datos
drop_database(host, user, password, database)
