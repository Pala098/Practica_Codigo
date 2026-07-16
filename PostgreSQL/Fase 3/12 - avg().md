## Consulta A
```sql
SELECT AVG(precio)
FROM productos;
```
Preguntas
1. ¿Qué número devolverá?
	Devolverá 337
2. ¿Qué representa ese número para la empresa?
	El promedio de venta entre todos los productos.
> [!bug|borde] Corrección
> `avg(precio)`
> Está calculando el **promedio del precio de los productos**, **no el promedio de ventas**.
> Podríamos decir:
> *Representa el precio promedio de los productos del catálogo.*
> o
> *Representa el valor promedio de un producto.*

3. ¿Cuántas filas devolverá?
	Devuelve 1 sola fila.
---
## Consulta B
```sql
SELECT AVG(precio)
FROM productos
WHERE precio >= 100;
```
Preguntas
1. ¿Qué productos participan?
	Los productos que participan son:
	- Monitor --> 300
	- Notebook --> 1200
2. ¿Qué promedio devolverá?
	Devuelve 750.
3. ¿Por qué los demás productos no participan?
	Porque no cumplen con la condición de que el valor de precio sea mayor o igual a 100.
---
## Consulta C
Supongamos esta tabla:

| producto    | precio |
| ----------- | ------ |
| Mouse       | 25     |
| Teclado     | 70     |
| Auriculares | NULL   |
| Monitor     | 300    |
| Notebook    | 1200   |

Y ejecutamos:
```sql
SELECT AVG(precio)
FROM productos;
```
Preguntas
1. ¿Qué resultado devolverá? 
	Devolverá 398.75
2. ¿Por qué divide entre 4 y no entre 5?
	Porque solo son 4 los registros que tienen un valor cargado en precio.
3. ¿Qué relación tiene ese comportamiento con `SUM()` y `COUNT(precio)`?
	En las tres se ignora cualquier registro que tenga `null`, o también se puede decir que no toma valores desconocidos.
---
## Caso de negocio
### Mensaje del gerente comercial

> Necesito conocer el **precio promedio** de los productos que cuestan **$70 o más**.
> 
> No necesito el detalle de los productos, solamente el promedio.

Como ya es costumbre, seguí nuestra metodología.

1. Análisis

```
Análisis

Columnas:
	- avg(precio)
Tabla(s):
	- Productos
Condiciones (WHERE):
	- where precio >= 70
Orden (ORDER BY):
	- Ninguno
Límite (LIMIT):
	- Ninguno
Operaciones especiales:
	- avg()
Observaciones:
	- Se solicita el promedio del precio de los productos.
	- Los registros que se debe tomar son los que tengan como precio 70 o superior.
```

2. Escribí la consulta SQL.
```sql
select avg(precio)
from productos
where precio >= 70;
```