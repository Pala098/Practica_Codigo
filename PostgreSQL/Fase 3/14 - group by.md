No ejecutes las consultas todavía.

---
## Consulta A

```
SELECT ciudad,
       COUNT(*)
FROM clientes
GROUP BY ciudad;
```
Preguntas
1. ¿Cuántas filas devolverá?
	Devolverá 4 filas.
2. ¿Qué ciudades aparecerán?
	Aparecen:
	- La Plata
	- Córdoba
	- Mendoza
	- Rosario
3. ¿Qué valor tendrá `La Plata`?
	La Plata tendrá como valor 2.
4. ¿Por qué no devuelve una sola fila?
	Porque `group by` agrupa según un una condición que determinemos y nos cuenta a partir este resultado.
---
## Consulta B

```
SELECT ciudad,
       COUNT(*)
FROM clientes
WHERE ciudad <> 'La Plata'
GROUP BY ciudad;
```
Preguntas
1. ¿Qué ciudades aparecerán?
	Aparecerán:
	- Córdoba
	- Mendoza
	- Rosario
2. ¿Cuántas filas devolverá?
	Devolverá 3 filas.
3. ¿Por qué `La Plata` no aparece?
	Porque se pone una condición (con `where ciudad <> 'La Plata'`) donde los registros que se quiere obtener son todos menos los que tengan el vaor de 'La Plata'.
---
## Consulta C
Sin ejecutar.
```
SELECT nombre,
       COUNT(*)
FROM clientes
GROUP BY ciudad;
```
Preguntas
1. ¿La consulta funcionará?
	No, no funcionara.
2. Si pensás que no, explicá por qué.
	Porque el valor de `group by` es diferente de `select`, y es importante que ambos tengan el mismo valor, si no esto dará un error.
	
> [!bug|borde] Correccion
> Aquí hay un pequeño detalle conceptual.
> No es que **deban ser iguales**.
> Por ejemplo, esta consulta es perfectamente válida:
> ```sql
> SELECT ciudad,
>        COUNT(*)
>        FROM clientes
>        GROUP BY ciudad;
> ```
> Y `COUNT(*)` no está en el `GROUP BY`.
> La regla real es:
> Toda columna que aparezca en el `SELECT` y **no esté dentro de una función de agregación** debe aparecer también en el `GROUP BY`.
> El problema de la consulta es este:
> ```sql
> SELECT nombre
> ```
> Dentro del grupo **La Plata** existen:
> 	- Ana
> 	- Lucía 
> Entonces SQL se pregunta:
> ¿Cuál de los dos nombres debo mostrar?
> Y no puede responder.
> Por eso genera un error.


1. ¿Qué regla de `GROUP BY` se está incumpliendo?
	La regla que se esta incumpliendo es que en el `select` solo debe haber columnas usadas en `group by`.
---
## 💼 Caso de negocio

### 📧 Mensaje del gerente comercial

> Necesito saber cuántos clientes tenemos en cada ciudad para planificar la próxima campaña de marketing.

Como siempre, seguí nuestra metodología.
1.  Análisis

```
Análisis

Columnas:
	- ciudad
Tabla(s):
	- Clientes
Condiciones (WHERE):
	- Ninguna
Agrupación (GROUP BY):
	- group by(ciudad)
Orden (ORDER BY):
	- Ninguno
Límite (LIMIT):
	- Ninguno
Operaciones especiales:
	- group by()
	- count()
Observaciones:
	- Se solicita la cantidad de clientes
	- Se pide agrupar por ciudad
```

> **Nota:** A partir de este tema, agregaremos una nueva sección al análisis: **Agrupación (`GROUP BY`)**, porque ya forma parte de la estructura lógica de una consulta.

2. Escribí la consulta SQL.
```sql
select ciudad, count(*)
from clientes
group by(ciudad);
```