## Consulta A
```sql
SELECT SUM(precio)
FROM productos;
```
Preguntas
1. ¿Qué número devolverá?
	Devolverá 1685.
2. ¿Qué representa ese número para la empresa?
	Representa el total, o la suma, de el precio de todos los productos.
3. ¿Cuántas filas devolverá la consulta?
	Devolverá 1 sola fila.
---
## Consulta B
```sql
SELECT SUM(precio)
FROM productos
WHERE precio >= 100;
```
Preguntas
1. ¿Qué productos participan en la suma?
	Participan los productos que tengan cargado en la columna precio un valor igual o superior a 100.
2. ¿Qué resultado devolverá?
	Devolverá 1500.
3. Explica por qué los demás productos no participan.
	Porque no cumplen con la condición del `where`, o simplemente porque su precio es inferior a 100.
---
## Consulta C
Imagina que la tabla fuera así:

|producto|precio|
|---|---|
|Mouse|25|
|Teclado|70|
|Auriculares|NULL|
|Monitor|300|
|Notebook|1200|

Y ejecutamos:
```sql
SELECT SUM(precio)
FROM productos;
```
Preguntas
1. ¿Qué número devolverá?
	Devolverá 1595
2. ¿Por qué no produce un error al encontrar un `NULL`?
	Porque `sum()` omite los valores desconocidos.
3. ¿Qué diferencia observas respecto a `COUNT(precio)`?
	La diferencia es que `sum()` realiza la suma con los valores de la columna precio, y `count()` cuenta la cantidad de filas que tienen un valor cargado en esta.
---
## Caso de negocio
### Mensaje del gerente de compras

> Necesito saber cuánto dinero representan los productos cuyo precio es mayor o igual a **$70**.
> 
> Solo necesito ese valor, no el detalle de cada producto.

No escribas la consulta todavía.

Primero responde el análisis siguiendo nuestra metodología:

```
Análisis

Columnas:
	- precio
Tabla(s):
	- Productos
Condiciones (WHERE):
	- `where precio >= 70`
Orden (ORDER BY):
	- Ninguno
Límite (LIMIT):
	- Ninguno
Operaciones especiales:
	- `sum()`
Observaciones:
	- Se solicita la suma de los valores de la columna precio
	- Los valores con los cuales se debe trabajar son con los que sean igual o mayor a 70.
	  
```

Y **después** escribe la consulta SQL.

```sql
select sum(precio)
from productos
where precio >= 70;
```