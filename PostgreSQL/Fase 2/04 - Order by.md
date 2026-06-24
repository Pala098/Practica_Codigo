Sin ejecutar:
```sql
SELECT * FROM productos ORDER BY precio DESC;
```
- ¿Qué hace `DESC`?
	Indica que el orden en el cual devolverá será de forma descendente.
- ¿Cuál será el primer producto?
	El orden será: Notebook -> monitor -> auriculares -> teclado -> mouse
- ¿Cuál será el último producto?
	El ultimo producto será: Mouse

---
## Consulta A
```sql
SELECT producto, precio
FROM productos
ORDER BY precio ASC;
```
1.  ¿Cuál será el primer producto?
	El primer producto será Mouse
2. ¿Cuál será el último producto?
	El ultimo producto será Notebook
## Consulta B
```sql
SELECT nombre
FROM clientes
ORDER BY nombre DESC;
```
1.  ¿Cuál será el primer nombre?
	El primer nombre será Pedro
2. ¿Cuál será el último nombre?
	El ultimo nombre será Ana
## Consulta C
```sql
SELECT producto
FROM productos
WHERE precio > 50
ORDER BY precio DESC;
```
1. ¿Qué productos aparecerán?
	Aparecerán teclado, monitor, notebook y auriculares.
2. ¿En qué orden aparecerán?
	El orden será: Notebook -> Monitor -> Auriculares -> Teclado