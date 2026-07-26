
---
# Descripción
TechStore es una empresa dedicada a la comercialización de productos tecnológicos para consumidores finales y pequeñas empresas.  
Actualmente posee una única sucursal física y un canal de ventas online.  
Toda la información comercial se almacena en PostgreSQL.  
El equipo de Datos utiliza esta base para responder consultas del área Comercial, Marketing, Finanzas y Gerencia  
# Modelo actual
En esta versión tendremos **tres tablas**, pero mucho más completas.  
- Clientes  
- Productos  
- Ventas  
# Objetivo
Esta versión amplía considerablemente el volumen de información respecto de la versión inicial.  
Su finalidad es permitir practicar consultas SQL en escenarios mucho más cercanos a los de una empresa real, manteniendo una complejidad adecuada para el aprendizaje.

---
## Reglas del negocio
Estas reglas son importantes porque se usaran constantemente para razonar las consultas.
> [!summary|borde] Clientes
> - un cliente puede estar activo o inactivo
> - algunos clientes aun no informaron telegono
> - todos poseen email
> - hay clientes de varias provincias argentinas

> [!summary|borde] Productos
> - puede haber productos sin stock
> - puede haber productos inactivos
> - el precio siempre es mayor que el costo
> - habra varias categorias

> [!summary|borde] Ventas
> - una venta puede incluir varias unidades de un mismo producto
> - puede existir descuento
> - el `precio_unitario` refleja el valor al momento de la venta
> - un mismo cliente puede tener muchas ventas
> - un producto puede venderse muchas veces



---
### Tabla clientes
Pasaremos de 5 registros a aproximadamente 40 clientes.

|Campo|Tipo|Descripción|
|---|---|---|
|id_cliente|INTEGER|Identificador del cliente|
|nombre|VARCHAR|Nombre|
|apellido|VARCHAR|Apellido|
|ciudad|VARCHAR|Ciudad|
|provincia|VARCHAR|Provincia|
|telefono|VARCHAR|Puede ser NULL|
|email|VARCHAR|Correo electrónico|
|fecha_alta|DATE|Fecha de alta como cliente|
|estado|VARCHAR|Activo / Inactivo|
### Tabla productos
Pasaremos a aproximadamente 30 productos.

|Campo|Tipo|Descripción|
|---|---|---|
|id_producto|INTEGER|Identificador|
|producto|VARCHAR|Nombre|
|categoria|VARCHAR|Categoría|
|marca|VARCHAR|Marca|
|costo|NUMERIC|Costo para la empresa|
|precio|NUMERIC|Precio de venta|
|stock|INTEGER|Cantidad disponible|
|proveedor|VARCHAR|Nombre del proveedor (por ahora texto)|
|estado|VARCHAR|Activo / Inactivo|
### Tabla ventas
Tendremos aproximadamente 150 ventas.

|Campo|Tipo|Descripción|
|---|---|---|
|id_venta|INTEGER|Identificador|
|cliente|INTEGER|ID del cliente|
|producto|INTEGER|ID del producto|
|cantidad|INTEGER|Cantidad vendida|
|precio_unitario|NUMERIC|Precio al momento de la venta|
|descuento|NUMERIC|Porcentaje aplicado|
|fecha|DATE|Fecha|
|vendedor|VARCHAR|Nombre del vendedor|
