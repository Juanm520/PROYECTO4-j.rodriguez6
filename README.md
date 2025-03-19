# 🐧 API Sammy el Heladero

Esta API permite gestionar productos e ingredientes, incluyendo su consulta, actualización y venta.

## 🔐 Autorización

Debe tener autorización para ingresar a algunos endpoints.
    Usuarios disponibles para pruebas: 
    `admin:admin1`
    `empleado:empleado1`
    `cliente:cliente1`

# 📌 API Endpoints:
## 🍨🥤 Productos

### 🔹 Obtener todos los productos
**GET** `/productos` `No requiere autorizacion`

### 🔹 Obtener un producto por ID
**GET** `/producto_id?id={id}` `Admin - Empleado`

### 🔹 Obtener un producto por nombre
**GET** `/producto_nombre?nombre={nombre}` `Admin - Empleado`

### 🔹 Obtener las calorías de un producto
**GET** `/producto_calorias?id={id}` `Admin - Empleado - cliente`

### 🔹 Obtener la rentabilidad de un producto
**GET** `/producto_rentabilidad?id={id}` `Admin`

### 🔹 Obtener el costo de un producto
**GET** `/producto_costo?id={id}` `Admin`

### 🔹 Vender un producto
**POST** `/vender_producto?id={id}` `Admin - Empleado - cliente`

## 🍓 Ingredientes

### 🔹 Obtener todos los ingredientes
**GET** `/ingredientes` `Admin - Empleado`

### 🔹 Obtener un ingrediente por ID
**GET** `/ingrediente_id?id={id}` `Admin - Empleado`

### 🔹 Obtener un ingrediente por nombre
**GET** `/ingrediente_nombre?nombre={nombre}` `Admin - Empleado`

### 🔹 Verificar si un ingrediente es sano
**GET** `/ingrediente_es_sano?id={id}` `Admin - Empleado`

### 🔹 Reabastecer un ingrediente
**POST** `/ingrediente_reabastecer?id={id}` `Admin - Empleado`

### 🔹 Renovar un ingrediente
**POST** `/ingrediente_renovar?id={id}` `Admin - Empleado`

### 🔀 CAMBIOS:
### **Adaptado a Mysql** `Proyecto 3 estaba adaptado para una BD postgreSQL.`
### **Despliegue** `Adaptado para el despliegue en un hosting administrado con CPanel.`