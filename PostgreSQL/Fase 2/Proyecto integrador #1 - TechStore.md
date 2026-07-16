En este proyecto podrás usar libremente:
- `SELECT`
- `FROM`
- `WHERE`
- Operadores de comparación
- `ORDER BY`
- `LIMIT`
- `DISTINCT`
- `LIKE`
- `IN`
- `BETWEEN`
- `IS NULL`
Y seguiremos el flujo que definimos:
1. Analizar el requerimiento.
2. Planificar (columnas, tablas, filtros, orden, límite).
3. Escribir la consulta.
4. Auto revisión.
5. Code Review.
---
## Contexto
Acabas de ingresar como **Data Analyst Junior** en **TechStore**, una empresa dedicada a la venta de productos informáticos.
Tu líder de equipo te asignó varias tareas que fueron llegando desde distintos sectores de la empresa (Ventas, Marketing, Compras y Gerencia).
Tu trabajo consiste en responder esos requerimientos utilizando SQL.
No habrá pistas sobre qué operadores utilizar. Deberás decidirlo tú.
> [!info|borde] Reglas
> Para cada ticket, seguiremos estos pasos:
> > [!summary|borde] 1. Análisis
> > Columnas:
> > Tabla(s):
> > Filtros:
> > Orden:
> > Límite:
> > Observaciones:
> 
> > [!summary|borde] 2. Consulta SQL
> > La escribimos completa
> 
> > [!summary|borde] 3. Auto revisión
> > Responder brevemente:
> > - Cumplo el requerimiento ?
> > - Elegí la mejor herramienta ?
> > - Hay algo que podría simplificar ?
> > - Existe otra forma de escribir esta consulta ?

> [!hint|borde] Estructura de presentación
> **Análisis**
> - Columnas:
> - Tabla(s):
> - Condiciones (`WHERE`):
> - Orden (`ORDER BY`):
> - Límite (`LIMIT`):
> - Operaciones especiales
>
> **Observaciones**
> - texto
>  
> ```sql
> codigo
> ```  
> 
> 
> **Auto revisión**
> - Cumple el requerimiento ?
> - Elegiste la herramienta correcta ?
> - Hay algo que podría simplificar ?
> - Existe otra forma de escribir esta consulta ?

---
## Base de datos disponible
Se utilizara la misma base de datos que se construyo al inicio `cliente`,`productos` y `pedidos`.

---
## Ticket #1 - Área comercial
El gerente comercial quiere preparar una campaña para clientes de determinadas ciudades.
Necesita un listado con:
- nombre
- ciudad
Únicamente de los clientes que viven en:
- La Plata
- Rosario
Debe estar ordenado alfabéticamente por nombre.

```sql
select nombre, ciudad
from clientes
where ciudad in ('La Plata','Rosario')
order by nombre asc;
```

---
## Ticket #2 - Compras
Compras quiere revisar los productos cuyo precio está entre **$50 y $500**.
Necesitan visualizar:
- producto
- precio
Ordenados del más caro al más barato.

 **Análisis**
 - Columnas:
	 - producto
	 - precio
 - Tabla(s):
	 - Productos
 - Filtros:
	 - `precio between 50 and 50`
 - Orden:
	 - `precio desc`
 - Límite:
	 - Ninguno
 **Observaciones**
 - Solo se necesita dos columnas.
 - Se solicita registros dentro del rango de 50 y 500.
 - El orden solicitado es por precio descendente.

```sql
select producto,precio
from productos
where precio between 50 and 500
order by precio desc;
```
**Auto revisión**
- Cumple el requerimiento ?
	Si.
- Elegiste la herramienta correcta ?
	Si.
	`between` es la mejor elección para traer valores dentro de un rango establecido.
- Hay algo que podría simplificar ?
	No, las estructura de la consulta es bastante simple.

---
## Ticket #3 - Marketing
Marketing quiere conocer las ciudades donde hay clientes.
No quiere ciudades repetidas.
Además, desea el listado ordenado alfabéticamente.
**Análisis**
 - Columnas:
	- Ciudad
 - Tabla(s):
	- Clientes
 - Filtros:
	 - `distinct ciuda`
 - Orden:
	 - `ciudad asc`
 - Límite:
	- Ninguno
 **Observaciones**
- Se solicita los valores de la columna ciudad pero no repetidos.
- El orden solicitado es por el nombre de ciudad de forma ascendente.

```sql
select distinct ciudad
from clientes
order by ciudad asc;
```

**Auto revisión**
- Cumple el requerimiento ?
	Si.
- Elegiste la herramienta correcta ?
	Si.
	Considero que aplicando`distinct` es la mejor forma de filtrar únicamente los valores únicos sin traer repetidos.
- Hay algo que podría simplificar ?
	No, la consulta ya es bastante simple.
- Existe otra forma de escribir esta consulta ?
	Considerando mi conocimiento actual, no se me ocurre alguna otra forma de escribir la consulta.

---
## Ticket #4 - Atención al cliente
Necesitan identificar los clientes que todavía no registraron un teléfono.
Mostrar únicamente:
- nombre
- ciudad
> **Análisis**
> - Columnas:
> 	- nombre
> 	- ciudad
> - Tabla(s):
> 	- clientes
> - Condiciones (`WHERE`):
> 	- `telefono is null`
> - Orden (`ORDER BY`):
> 	- Ninguno
> - Límite (`LIMIT`):
> 	- Ninguno
> - Operaciones especiales
> 	- Se agrega `is null` a la consulta `where`
>
> **Observaciones**
> - Se pide mostrar solamente los registros que no tienen un valor en la columna teléfono

```sql
select nombre, ciudad
from clientes
where telefono is null;
```

>**Auto revisión**
>- Cumple el requerimiento ?
>	Si.
>- Elegiste la herramienta correcta ?
>	Si.
>	Considero que utilizar `telefono is null` es lo mejor y lo correcto.
>- Hay algo que podría simplificar ?
>	No.
>- Existe otra forma de escribir esta consulta ?
>	No, pero si podemos encontrar `where telefono = null` lo cual seria erróneo.
---
## Ticket #5 - Inventario
El encargado del depósito quiere revisar todos los productos cuyo nombre contiene la letra:
```
o
```
Mostrar:
- producto
- precio
Ordenados alfabéticamente por nombre del producto.
> **Análisis**
> - Columnas:
> 	- producto
> 	- precio
> - Tabla(s):
> 	- Productos
> - Condiciones (`WHERE`):
> 	- `producto like '%o%'`
> - Orden (`ORDER BY`):
> 	- `producto asc`
> - Límite (`LIMIT`):
> 	- Ninguno
> - Operaciones especiales
> 	- Ninguno
> **Observaciones**
> - Se solicita todos los registros que contenga el caracter 'o', sin importar su posicion.
> - Se pide un orden ascendente por por nombre del producto

```sql
select producto,precio
from productos
where producto like '%o%'
order by producto asc;
```
> **Auto revisión**
> - Cumple el requerimiento ?
> 	Si.
> - Elegiste la herramienta correcta ?
> 	Si.
> 	Se utilizo `like '%o%'` para indicar que muestre los registros en los cuales el nombre del producto contenga 'o', sin importar que numero de caracteres tenga antes o después de esta letra.
> - Hay algo que podría simplificar ?
> 	No, considero que esta bastante simple.
> - Existe otra forma de escribir esta consulta ?
> 	No.
---
## Ticket #6 - Gerencia
El director quiere un informe rápido con **los tres productos más económicos**.
Mostrar:
- producto
- precio

> **Análisis**
> - Columnas:
> 	- producto
> 	- precio
> - Tabla(s):
> 	- Productos
> - Condiciones (`WHERE`):
> 	- Ninguno
> - Orden (`ORDER BY`):
> 	- `precio asc`
> - Límite (`LIMIT`):
> 	-`limit 3`
> - Operaciones especiales
> 	- Ninguno
> **Observaciones**
> - Se solicita mostrar productos mas económicos.
> - Se pide un orden ascendente por el precio.
> - Se limita la muestra de registros a solamente 3 elementos.


```sql
select producto, precio
from productos
order by precio asc
limit 3;
```

 > **Auto revisión**
> - Cumple el requerimiento ?
> 	Si.
> - Elegiste la herramienta correcta ?
> 	Si.
> 	Para lo que se solicita considero que es lo correcto solamente utilizar `orden by` y `limit`, sin aplicar alguna condición (ya que no lo veo necesario).
> - Hay algo que podría simplificar ?
> 	No.
> - Existe otra forma de escribir esta consulta ?
> 	No.
