## Consulta A

```
SELECT ciudad,
       COUNT(*)
FROM clientes
GROUP BY ciudad
HAVING COUNT(*) > 1;
```

Preguntas
1. ¿Cuántas filas devolverá?
	Devolverá 1 fila.
2. ¿Qué ciudad aparecerá?
	Aparecerá La Plata
3. ¿Por qué Córdoba no aparece?
	Porque tiene solo 1 cliente, y la condición es que cuente solo las que tengan mas de un cliente.

---
## Consulta B

```
SELECT ciudad,
       COUNT(*)
FROM clientes
GROUP BY ciudad
HAVING COUNT(*) >= 1;
```

Preguntas
1. ¿Qué ciudades aparecerán?
	Aparecerán:
	- La Plata
	- Córdoba
	- Mendoza
	- Rosario
2. ¿Cuántas filas devolverá?
	Devolverá 4 filas.
3. Explica por qué.
	Porque son 4 valores diferentes que tenemos como valores en la columna de ciudad, donde uno se repite.

---
## Consulta C
Sin ejecutar.

```
SELECT ciudad,
       COUNT(*)
FROM clientes
WHERE COUNT(*) > 1
GROUP BY ciudad;
```

Preguntas
1. ¿La consulta funcionará?
	No.
2. Explica por qué.
	Porque en SQL existe un orden de ejecución y cuando se ejecuta `where` todavía no existe `count(*)`.

> [!bug|borde] Correccion
> Correcto, pero hay un detalle interesante.
> La razón principal no es solamente que existan cuatro ciudades distintas.
> La clave está en la condición:
> ```
> HAVING COUNT(*) >= 1
> ```
> Todos los grupos tienen al menos un cliente.
> Entonces **ningún grupo es eliminado**.
> Una explicación más completa sería:
> *`GROUP BY` genera cuatro grupos (uno por ciudad) y `HAVING COUNT(*) >= 1` permite que todos pasen, porque cada grupo tiene al menos un registro.*

3. ¿Qué herramienta debería utilizarse en lugar de `WHERE`?
	Se debería utilizar `having count(*) > 1`.

---

# 💼 Caso de negocio

## 📧 Mensaje del gerente de marketing

> Necesito identificar únicamente las ciudades donde tenemos **más de un cliente**, porque quiero lanzar una campaña local y no tiene sentido invertir en ciudades donde solo hay un cliente.

Como siempre, seguí nuestra metodología.
1.  Análisis

```
Análisis

Columnas:
	- ciudad, count(*)
Tabla(s):
	- Clientes
Condiciones (WHERE):
	- Ninguna
Agrupación (GROUP BY):
	- group by ciudad
Filtro de grupos (HAVING):
	- having count(*) > 1
Orden (ORDER BY):
	- Ninguno
Límite (LIMIT):
	- Ninguno
Operaciones especiales:
	- having count(*) > 1
Observaciones:
	- Se solicita indetificar las ciudades donde se tenga mas de un cliente.
```
> [!bug|borde] Correccion
> ### Operaciones especiales
> Escribiste:
> `HAVING COUNT(*) > 1`
> ==Acá haría una pequeña mejora.==
> Las **operaciones especiales** son las herramientas utilizadas, no la condición completa.
> Yo escribiría:
> ```
> COUNT()
> GROUP BY
> HAVING
> ```
> Es una diferencia de organización, no de concepto.

> A partir de hoy agregaremos una nueva sección al análisis:
> 
> **Filtro de grupos (`HAVING`)**
> 
> Esto te ayudará a distinguir claramente cuándo un filtro corresponde a `WHERE` y cuándo a `HAVING`.

2. Escribí la consulta SQL.
```sql
select ciudad, count(*)
from clientes
group by ciudad
having count(*) > 1;
```