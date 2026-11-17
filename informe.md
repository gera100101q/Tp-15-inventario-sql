# Informe - Trabajo Práctico N.º 15
## Sistema de inventario de gorras

### 1. Temática elegida y motivo
Elegí desarrollar un inventario de gorras porque permite representar una situación concreta de administración de productos. El sistema sirve para registrar modelos, marcas, colores, precios y cantidades disponibles.

### 2. Diseño de la tabla
La base de datos se llama `inventario_gorras` y contiene una tabla llamada `gorras`. Incluye los campos `id`, `modelo`, `marca`, `color`, `precio` y `stock`. El campo `id` es la clave primaria y se genera automáticamente.

### 3. Funcionamiento del programa
El programa se conecta a MySQL desde Python y ofrece un menú para agregar, mostrar, buscar, actualizar y eliminar registros. Estas funciones corresponden a las operaciones CRUD. El funcionamiento debe comprobarse ejecutando cada opción con la base de datos creada.

### 4. Dificultades encontradas
Una dificultad posible es configurar correctamente la conexión entre Python y MySQL, además de verificar que el servidor esté iniciado y que los datos de acceso sean correctos. También es importante controlar que los datos ingresados tengan el formato esperado.

### 5. Aprendizajes
Aprendí cómo Python puede conectarse con una base de datos MySQL para consultar y modificar información. También comprendí la utilidad de separar la estructura de la base de datos del código de la aplicación.

### 6. Consultas parametrizadas y transacciones
Las consultas parametrizadas permiten enviar los valores por separado de las instrucciones SQL, lo que ayuda a evitar la inyección SQL y errores al construir consultas. El método `commit()` confirma los cambios realizados en la base de datos. Si ocurre un error, `rollback()` permite deshacer los cambios pendientes para evitar que la información quede en un estado incorrecto.

### 7. Uso de inteligencia artificial
Se utilizó ChatGPT como apoyo para organizar la estructura inicial del proyecto, preparar ejemplos de código y redactar documentación. El código debe ser revisado, probado y comprendido antes de la entrega.
