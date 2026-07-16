## Consulta A
```sql
SELECT MIN(precio)
FROM productos;
```
Preguntas
1. ¿Qué número devolverá?
	Devolverá 25.
2. ¿Qué representa ese número para la empresa?
	Representa el precio mas bajo de los productos del catalogo.
3. ¿Cuántas filas devolverá?
	Devuelve 1 fila.
---
## Consulta B
```sql
SELECT MAX(precio)
FROM productos;
```
Preguntas
1. ¿Qué número devolverá?
	Devolverá 1200.
2. ¿Qué representa ese número?
	Representa el precio mas alto de los productos del catalogo.
3. ¿Por qué devuelve una sola fila?
	Porque la función `max()` evaluá cual es el precio mas alto, por ende, solo habrá un solo valor.
> [!bug|borde] Corrección
> Yo agregaría una pequeña precisión:
> Porque una función de agregación resume todas las filas en un único resultado. `MAX()` encuentra un único valor máximo y devuelve solo ese dato.
> No es una corrección, sino una forma más completa de explicarlo.

---
## Consulta C
```sql
SELECT MIN(precio)
FROM productos
WHERE precio >= 100;
```
Preguntas
1. ¿Qué productos participan?
	Los productos que participan son:
	- Monitor
	- Notebook
2. ¿Qué resultado devolverá?
	Devolverá 300
3. ¿Por qué `Mouse` no participa?
	Porque 'Mouse' no cumple con la condición del `where`.
---
## Consulta D
Supongamos la siguiente tabla:

| producto    | precio |
| ----------- | ------ |
| Mouse       | 25     |
| Teclado     | 70     |
| Auriculares | NULL   |
| Monitor     | 300    |
| Notebook    | 1200   |

Y ejecutamos:
```sql
SELECT MAX(precio)
FROM productos;
```
Preguntas
1. ¿Qué resultado devolverá?
	Devolverá 1200.
2. ¿Por qué el `NULL` no afecta el resultado?
	Porque simplemente se ignoran.
3. ¿Qué patrón observás respecto de `SUM()`, `AVG()` y `COUNT(precio)`?
	En todas las funciones el patrón que veo es que no trabajan con valores desconocidos, y además, todos devuelven un solo valor en sus resultados.
---
## Caso de negocio
### Mensaje del gerente financiero

> Necesito conocer el **producto más barato** y el **precio más alto** registrado en el catálogo.
> 
> No necesito el listado completo de productos, solamente esos dos indicadores.

Como siempre, seguí nuestra metodología.
1. Análisis

```
Análisis

Columnas:
	- min(precio)
	- max(precio)
Tabla(s):
	- Productos
Condiciones (WHERE):
	- Ninguna
Orden (ORDER BY):
	- Ninguna
Límite (LIMIT):
	- Ninguno
Operaciones especiales:
	- min()
	- max()
Observaciones:
	- Se solicita el producto mas barato
	- Se solicita el producto con el precio mas alto
```

> [!bug|borde] Corrección
> Observaciones
> - Se solicita conocer el precio mínimo del catálogo.
> - Se solicita conocer el precio máximo del catálogo.
> - Con los conocimientos actuales todavía no podemos identificar qué producto corresponde a esos precios.

2. Escribí la consulta SQL.
> **Importante:** No te preocupes si al leer el requerimiento pensás: _"¿Cómo voy a obtener el nombre del producto más barato?"_. Esa duda es totalmente válida y, de hecho, **todavía no sabemos resolverla** con las herramientas que conocemos. Por ahora, resolvé exactamente lo que podemos obtener con `MIN()` y `MAX()`.

```sql
select min(precio), max(precio)
from productos;
```