Sin ejecutar:
```sql
SELECT * FROM productos ORDER BY precio ASC LIMIT 3;
```
1.  ¿Cuántas filas devolverá?
	Devolverá 3 filas.
2. ¿Qué productos aparecerán?
	Los productos que aparecerán son:
	1. Mouse
	2. Teclado
	3. Auriculares
3. ¿Por qué aparecerán esos productos y no otros?
	Porque es lo que pide la consulta, y esto lo indica mediante `order by` y la cantidad de datos que muestra por `limit`.
Explicar el razonamiento paso a paso usando: 
```
FROM → WHERE (si existe) → ORDER BY → LIMIT → SELECT
```
1. `from productos` --> busca los datos de la tabla productos
2. `order by precio ASC` --> los ordena por el precio de forma ascendente
3. `limit 3` --> solo mostrara las 3 primeras filas
4. `select *` --> trae todos los datos