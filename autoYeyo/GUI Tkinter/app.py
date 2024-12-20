import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import sys
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar la ruta al directorio 'db' al path de Python
sys.path.append(os.path.join(current_dir, '../db'))

from configDB import DB_USER, DB_PASSWORD, DB_HOST, DB_NAMEDB

# Función para conectar con la base de datos
def connect_db():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAMEDB
    )

# Función para agregar cliente
def add_cliente():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "INSERT INTO Cliente (nombre, telefono) VALUES (%s, %s)"
        values = (entry_nombre_cliente.get(), entry_telefono_cliente.get())
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Éxito", "Cliente agregado correctamente")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error al agregar cliente: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Función para agregar vehículo
def add_vehiculo():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "INSERT INTO Vehiculo (marca, modelo, patente, año, kmActual, clienteID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (entry_marca_vehiculo.get(), entry_modelo_vehiculo.get(), entry_patente_vehiculo.get(), entry_anio_vehiculo.get(), 
                  entry_km_vehiculo.get(), entry_clienteID_vehiculo.get())
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Éxito", "Vehículo agregado correctamente")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error al agregar vehículo: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Función para agregar intervención
def add_intervencion():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "INSERT INTO Intervencion (fecha, descripcion, costo, vehiculoID, mecanicoID) VALUES (%s, %s, %s, %s, %s)"
        values = (entry_fecha_intervencion.get(), entry_descripcion_intervencion.get(), entry_costo_intervencion.get(), 
                  entry_vehiculoID_intervencion.get(), entry_mecanicoID_intervencion.get())
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Éxito", "Intervención agregada correctamente")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error al agregar intervención: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Función para agregar mecánico
def add_mecanico():
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "INSERT INTO Mecanico (nombre, fechaIngreso) VALUES (%s, %s)"
        values = (entry_nombre_mecanico.get(), entry_fechaIngreso_mecanico.get())
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Éxito", "Mecánico agregado correctamente")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error al agregar mecánico: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Taller Mecánico")

# Crear el notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Pestaña de clientes
frame_cliente = ttk.Frame(notebook, width=400, height=400)
frame_cliente.pack(fill='both', expand=True)
notebook.add(frame_cliente, text="Clientes")

# Campos para agregar cliente
label_nombre_cliente = tk.Label(frame_cliente, text="Nombre:")
label_nombre_cliente.pack(pady=5)
entry_nombre_cliente = tk.Entry(frame_cliente)
entry_nombre_cliente.pack(pady=5)

label_telefono_cliente = tk.Label(frame_cliente, text="Teléfono:")
label_telefono_cliente.pack(pady=5)
entry_telefono_cliente = tk.Entry(frame_cliente)
entry_telefono_cliente.pack(pady=5)

btn_add_cliente = tk.Button(frame_cliente, text="Agregar Cliente", command=add_cliente)
btn_add_cliente.pack(pady=10)

# Pestaña de vehículos
frame_vehiculo = ttk.Frame(notebook, width=400, height=400)
frame_vehiculo.pack(fill='both', expand=True)
notebook.add(frame_vehiculo, text="Vehículos")

# Campos para agregar vehículo
label_marca_vehiculo = tk.Label(frame_vehiculo, text="Marca:")
label_marca_vehiculo.pack(pady=5)
entry_marca_vehiculo = tk.Entry(frame_vehiculo)
entry_marca_vehiculo.pack(pady=5)

label_modelo_vehiculo = tk.Label(frame_vehiculo, text="Modelo:")
label_modelo_vehiculo.pack(pady=5)
entry_modelo_vehiculo = tk.Entry(frame_vehiculo)
entry_modelo_vehiculo.pack(pady=5)

label_patente_vehiculo = tk.Label(frame_vehiculo, text="Patente:")
label_patente_vehiculo.pack(pady=5)
entry_patente_vehiculo = tk.Entry(frame_vehiculo)
entry_patente_vehiculo.pack(pady=5)

label_anio_vehiculo = tk.Label(frame_vehiculo, text="Año (YYYY):")
label_anio_vehiculo.pack(pady=5)
entry_anio_vehiculo = tk.Entry(frame_vehiculo)
entry_anio_vehiculo.pack(pady=5)

label_km_vehiculo = tk.Label(frame_vehiculo, text="Km Actual:")
label_km_vehiculo.pack(pady=5)
entry_km_vehiculo = tk.Entry(frame_vehiculo)
entry_km_vehiculo.pack(pady=5)

label_clienteID_vehiculo = tk.Label(frame_vehiculo, text="ID Cliente:")
label_clienteID_vehiculo.pack(pady=5)
entry_clienteID_vehiculo = tk.Entry(frame_vehiculo)
entry_clienteID_vehiculo.pack(pady=5)

btn_add_vehiculo = tk.Button(frame_vehiculo, text="Agregar Vehículo", command=add_vehiculo)
btn_add_vehiculo.pack(pady=10)

# Pestaña de intervenciones
frame_intervencion = ttk.Frame(notebook, width=400, height=400)
frame_intervencion.pack(fill='both', expand=True)
notebook.add(frame_intervencion, text="Intervenciones")

# Campos para agregar intervención
label_fecha_intervencion = tk.Label(frame_intervencion, text="Fecha:")
label_fecha_intervencion.pack(pady=5)
entry_fecha_intervencion = tk.Entry(frame_intervencion)
entry_fecha_intervencion.pack(pady=5)

label_descripcion_intervencion = tk.Label(frame_intervencion, text="Descripción:")
label_descripcion_intervencion.pack(pady=5)
entry_descripcion_intervencion = tk.Entry(frame_intervencion)
entry_descripcion_intervencion.pack(pady=5)

label_costo_intervencion = tk.Label(frame_intervencion, text="Costo:")
label_costo_intervencion.pack(pady=5)
entry_costo_intervencion = tk.Entry(frame_intervencion)
entry_costo_intervencion.pack(pady=5)

label_vehiculoID_intervencion = tk.Label(frame_intervencion, text="ID Vehículo:")
label_vehiculoID_intervencion.pack(pady=5)
entry_vehiculoID_intervencion = tk.Entry(frame_intervencion)
entry_vehiculoID_intervencion.pack(pady=5)

label_mecanicoID_intervencion = tk.Label(frame_intervencion, text="ID Mecánico:")
label_mecanicoID_intervencion.pack(pady=5)
entry_mecanicoID_intervencion = tk.Entry(frame_intervencion)
entry_mecanicoID_intervencion.pack(pady=5)

btn_add_intervencion = tk.Button(frame_intervencion, text="Agregar Intervención", command=add_intervencion)
btn_add_intervencion.pack(pady=10)

# Pestaña de mecánicos
frame_mecanico = ttk.Frame(notebook, width=400, height=400)
frame_mecanico.pack(fill='both', expand=True)
notebook.add(frame_mecanico, text="Mecánicos")

# Campos para agregar mecánico
label_nombre_mecanico = tk.Label(frame_mecanico, text="Nombre:")
label_nombre_mecanico.pack(pady=5)
entry_nombre_mecanico = tk.Entry(frame_mecanico)
entry_nombre_mecanico.pack(pady=5)

label_fechaIngreso_mecanico = tk.Label(frame_mecanico, text="Fecha de Ingreso (YYYY-DD-MM):")
label_fechaIngreso_mecanico.pack(pady=5)
entry_fechaIngreso_mecanico = tk.Entry(frame_mecanico)
entry_fechaIngreso_mecanico.pack(pady=5)

btn_add_mecanico = tk.Button(frame_mecanico, text="Agregar Mecánico", command=add_mecanico)
btn_add_mecanico.pack(pady=10)

root.mainloop()
