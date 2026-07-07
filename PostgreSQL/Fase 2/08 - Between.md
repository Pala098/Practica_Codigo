## Consulta A
```sql
SELECT producto, precio
FROM productos
WHERE precio BETWEEN 70 AND 300;
```
Preguntas
1. ¿Qué productos aparecerán?
	Aparecen:
	- Teclado - 70
	- Auriculares - 90
	- Monitor - 300
2. ¿Cuántas filas devolverá?
	Devuelve 3 filas.
3. ¿Por qué aparece (o no aparece) `Monitor`?
	Aparece porque su precio es 300, y `between` incluye a este registro (ya que es el limite superior).
---
## Consulta B
```sql
SELECT nombre
FROM clientes
WHERE id_cliente BETWEEN 2 AND 4;
```
Preguntas
1. ¿Qué nombres aparecerán?
	Aparecen:
	- Juan
	- Pedro
	- María
2. ¿Cuántas filas devolverá?
	Devuelve 3 filas.
3. ¿Por qué no aparece Ana?
	Porque su id_cliente es 1, y este no esta contemplado dentro de los limites del `between`.
---
## Consulta C
```sql
SELECT producto
FROM productos
WHERE precio BETWEEN 26 AND 299;
```
Preguntas
1. ¿Qué producto aparecerá primero?
	Aparecerán:
	- Teclado - 70
	- Auriculares - 90
2. ¿Qué producto NO aparecerá aunque esté muy cerca del límite?
	No aparecen:
	- Mouse - 25
	- Monitor - 300
	- Notebook - 1200
3. Explica por qué.
	Porque estan por fuera del rango de los limites establecidos dentro de `between`.
---
## Caso de negocio 1
### Mensaje del jefe
> Hola.
> El área financiera está revisando productos de gama media.
> Necesitan un listado con el **nombre** y el **precio** de todos los productos cuyo precio esté **entre $50 y $300**, incluyendo ambos valores.
> El resultado debe estar **ordenado del más barato al más caro**.
### Tarea
Escribir la consulta SQL completa.
```sql
select producto, precio
from productos
where precio between 50 and 300
order by precio asc;
```
> [!hint|borde] Checklist mental antes de escribir SQL
> Antes de empezar una consulta, dedica 15 a 20 segundos a responder mentalmente estas cinco preguntas:
> 1. Que columnas me piden ?
> 2. De qué tabla salen ?
> 3. Qué condición deben cumplir ?
> 4. Hay que ordenar ?
> 5. En que sentido ?

