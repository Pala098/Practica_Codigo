## Consulta A
```sql
SELECT COUNT(*)
FROM clientes;
```
 Preguntas
1. ¿Qué número devolverá?
	Devolverá 5 
2. ¿Por qué?
	Porque hay 5 clientes registrados.
3. ¿Qué está contando exactamente?
	La cantidad de filas.
---
## Consulta B
```sql
SELECT COUNT(telefono)
FROM clientes;
```
 Preguntas
1. ¿Qué número devolverá?
	Devolverá 3.
2. ¿Por qué no devuelve 5?
	Porque solamente hay 3 clientes con el valor de teléfono cargado.
3. ¿Qué ocurriría si todos los clientes tuvieran teléfono?
	Devolvería 5, porque count(telefono) devuelve la cantidad de filas donde teléfono no es null.
---
## Consulta C
```sql
SELECT COUNT(producto)
FROM productos;
```
Preguntas
1. ¿Qué número devolverá?
	Devolverá 5.
2. ¿Será igual a `COUNT(*)`?
	En el caso de esta consulta si, ambos devolverían la misma cantidad.
3. Explica el motivo.
	Porque no hay registro con el valor de null en la columna producto.