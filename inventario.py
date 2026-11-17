"""
TP 15 - Sistema de inventario de gorras
Requisitos: Python 3 y mysql-connector-python.
"""

import os
import mysql.connector
from mysql.connector import Error


def conectar():
    """Abre la conexión con MySQL usando variables de entorno."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "inventario_gorras"),
    )


def mostrar_gorras(cursor):
    """Muestra todos los productos registrados."""
    cursor.execute(
        "SELECT id, modelo, marca, color, precio, stock FROM gorras ORDER BY id"
    )
    registros = cursor.fetchall()

    if not registros:
        print("\nNo hay gorras registradas.")
        return

    print("\n--- INVENTARIO DE GORRAS ---")
    print(f"{'ID':<5}{'MODELO':<22}{'MARCA':<16}{'COLOR':<18}{'PRECIO':>12}{'STOCK':>8}")
    print("-" * 81)
    for gorra in registros:
        print(
            f"{gorra[0]:<5}{gorra[1]:<22}{gorra[2]:<16}{gorra[3]:<18}"
            f"{float(gorra[4]):>12.2f}{gorra[5]:>8}"
        )


def agregar_gorra(cursor, conexion):
    """Solicita los datos y agrega una gorra."""
    print("\n--- AGREGAR GORRA ---")
    modelo = input("Modelo: ").strip()
    marca = input("Marca: ").strip()
    color = input("Color: ").strip()
    precio = float(input("Precio: "))
    stock = int(input("Cantidad en stock: "))

    if not modelo or not marca or not color or precio < 0 or stock < 0:
        print("Error: completá los campos y usá valores no negativos.")
        return

    consulta = """
        INSERT INTO gorras (modelo, marca, color, precio, stock)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(consulta, (modelo, marca, color, precio, stock))
    conexion.commit()
    print(f"Gorra agregada correctamente. ID asignado: {cursor.lastrowid}")


def buscar_gorra(cursor):
    """Busca una gorra por su identificador."""
    id_gorra = int(input("Ingresá el ID de la gorra: "))
    cursor.execute(
        "SELECT id, modelo, marca, color, precio, stock FROM gorras WHERE id = %s",
        (id_gorra,),
    )
    gorra = cursor.fetchone()

    if gorra:
        print("\nID | Modelo | Marca | Color | Precio | Stock")
        print(gorra)
    else:
        print("No se encontró una gorra con ese ID.")


def actualizar_gorra(cursor, conexion):
    """Actualiza los datos de una gorra existente."""
    id_gorra = int(input("ID de la gorra que querés modificar: "))
    cursor.execute("SELECT id FROM gorras WHERE id = %s", (id_gorra,))
    if cursor.fetchone() is None:
        print("No existe una gorra con ese ID.")
        return

    print("Ingresá los nuevos datos:")
    modelo = input("Nuevo modelo: ").strip()
    marca = input("Nueva marca: ").strip()
    color = input("Nuevo color: ").strip()
    precio = float(input("Nuevo precio: "))
    stock = int(input("Nuevo stock: "))

    if not modelo or not marca or not color or precio < 0 or stock < 0:
        print("Error: completá los campos y usá valores no negativos.")
        return

    consulta = """
        UPDATE gorras
        SET modelo = %s, marca = %s, color = %s, precio = %s, stock = %s
        WHERE id = %s
    """
    cursor.execute(consulta, (modelo, marca, color, precio, stock, id_gorra))
    conexion.commit()
    print("Gorra actualizada correctamente.")


def eliminar_gorra(cursor, conexion):
    """Elimina una gorra por su ID luego de pedir confirmación."""
    id_gorra = int(input("ID de la gorra que querés eliminar: "))
    cursor.execute("SELECT modelo FROM gorras WHERE id = %s", (id_gorra,))
    gorra = cursor.fetchone()

    if gorra is None:
        print("No existe una gorra con ese ID.")
        return

    confirmacion = input(f"¿Eliminar '{gorra[0]}'? (s/n): ").strip().lower()
    if confirmacion == "s":
        cursor.execute("DELETE FROM gorras WHERE id = %s", (id_gorra,))
        conexion.commit()
        print("Gorra eliminada correctamente.")
    else:
        print("Operación cancelada.")


def menu():
    """Controla el menú y mantiene abierta la conexión durante el uso."""
    conexion = None
    cursor = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()
        print("Conexión con MySQL establecida.")

        while True:
            print("\n===== INVENTARIO DE GORRAS =====")
            print("1. Agregar gorra")
            print("2. Mostrar inventario")
            print("3. Buscar gorra por ID")
            print("4. Actualizar gorra")
            print("5. Eliminar gorra")
            print("0. Salir")

            opcion = input("Elegí una opción: ").strip()

            try:
                if opcion == "1":
                    agregar_gorra(cursor, conexion)
                elif opcion == "2":
                    mostrar_gorras(cursor)
                elif opcion == "3":
                    buscar_gorra(cursor)
                elif opcion == "4":
                    actualizar_gorra(cursor, conexion)
                elif opcion == "5":
                    eliminar_gorra(cursor, conexion)
                elif opcion == "0":
                    print("Programa finalizado.")
                    break
                else:
                    print("Opción inválida. Intentá nuevamente.")
            except (ValueError, TypeError):
                if conexion and conexion.is_connected():
                    conexion.rollback()
                print("Error: ingresá un número válido y datos correctos.")
            except Error as error:
                if conexion and conexion.is_connected():
                    conexion.rollback()
                print(f"Error en la operación: {error}")

    except Error as error:
        print(f"No se pudo conectar con MySQL: {error}")
        print("Verificá que MySQL esté iniciado y que los datos de conexión sean correctos.")
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()
            print("Conexión cerrada correctamente.")


if __name__ == "__main__":
    menu()
