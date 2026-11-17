# TP 15 - Inventario de Gorras

Aplicación de consola en Python conectada a MySQL para administrar un inventario mediante operaciones CRUD.

## Archivos
- `crear_bd.sql`: crea la base de datos, la tabla y carga cinco registros de prueba.
- `inventario.py`: aplicación de consola con las operaciones CRUD.
- `informe.md`: informe del trabajo práctico.

## Requisitos
- Python 3
- MySQL Server en ejecución
- Paquete `mysql-connector-python`

## Instalación
Abrí una terminal en esta carpeta y ejecutá:

```bash
python -m pip install mysql-connector-python
```

## Preparar la base de datos
Ejecutá el contenido de `crear_bd.sql` en MySQL Workbench o desde la consola de MySQL.

## Configurar la conexión
Por defecto, el programa intenta conectarse a `localhost`, puerto `3306`, usuario `root`, contraseña vacía y base `inventario_gorras`.

Si tu configuración es diferente, definí estas variables de entorno antes de ejecutar el programa:
- `DB_HOST`
- `DB_PORT`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`

No subas contraseñas reales a GitHub.

## Ejecutar

```bash
python inventario.py
```

## Operaciones disponibles
1. Agregar gorra (CREATE).
2. Mostrar inventario (READ).
3. Buscar gorra por ID (READ).
4. Actualizar gorra (UPDATE).
5. Eliminar gorra (DELETE).
0. Salir.

Las consultas usan parámetros, los cambios se confirman con `commit()` y ante errores se intenta ejecutar `rollback()`.
