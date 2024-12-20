import mysql.connector
from configDB import DB_USER, DB_PASSWORD, DATABASE_INDEX, DB_HOST,DB_NAMEDB

def create_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        print("Base de datos creada correctamente...")
        DATABASE_INDEX = True

    except mysql.connector.Error as error:
        print("Error al crear la base de datos:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a la base de datos cerrada.")


def create_tables(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = connection.cursor()

        if not DATABASE_INDEX:
            # Crear tabla Cliente
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cliente (
                clienteID INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50),
                telefono VARCHAR(50)
            )
            """)

            # Crear tabla Vehiculo (relación con Cliente)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Vehiculo (
                vehiculoID INT AUTO_INCREMENT PRIMARY KEY,
                marca VARCHAR(50),
                modelo VARCHAR(50),
                patente VARCHAR(10),
                año INT,
                kmActual INT,
                clienteID INT,
                FOREIGN KEY (clienteID) REFERENCES Cliente(clienteID) ON DELETE CASCADE
            )
            """)

            # Crear tabla Mecanico
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Mecanico (
                mecanicoID INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50),
                fechaIngreso DATE
            )
            """)

            # Crear tabla Intervencion (relación con Vehiculo y Mecanico)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Intervencion (
                intervencionID INT AUTO_INCREMENT PRIMARY KEY,
                fecha DATE,
                descripcion VARCHAR(600),
                costo DECIMAL(10, 2),
                vehiculoID INT,
                mecanicoID INT,
                FOREIGN KEY (vehiculoID) REFERENCES Vehiculo(vehiculoID) ON DELETE CASCADE,
                FOREIGN KEY (mecanicoID) REFERENCES Mecanico(mecanicoID) ON DELETE CASCADE
            )
            """)

        print("Tablas creadas correctamente.")

    except mysql.connector.Error as error:
        print("Error al crear las tablas:", error)

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

# Crear la base de datos y las tablas
create_database(host, user, password, database)
create_tables(host, user, password, database)
