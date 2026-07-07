## Consulta A
```sql
select nombre
from clientes
where telefono is null;
```
Preguntas
1. ¿Qué nombres aparecerán?
	Aparecerán: 
	- Juan
	- Lucia
2. ¿Cuántas filas devolverá?
	Devolverá 2 filas.
3. Explica por qué.
	Porque son las dos únicas filas que no tiene un valor almacenado en la columna teléfono.
---
## Consulta B
```sql
select nombre, telefono
from clientes
where telefono is not null;
```
Preguntas
1. ¿Qué clientes aparecerán?
	Aparecerán:
	- Ana - 221-555-1001
	- Pedro - 351-555-2002
	- Maria - 261-555-3003
2. ¿Cuántas filas devolverá?
	Devolverá 3 filas.
3. ¿Por qué Juan no aparece?
	Porque no tiene asignado un valor almacenado en la columna teléfono.
---
## Consulta C
```sql
select *
from clientes
where telefono = null;
```
Preguntas
1. ¿Qué devolverá esta consulta?
	No devolverá nada.
2. ¿Por qué?
	Porque no podemos comparar un valor desconocido.
3. ¿Cuál sería la forma correcta de escribirla si queremos encontrar clientes sin teléfono?
	La forma correcta seria:
```sql
select *
from clientes
where telefono is null;
```