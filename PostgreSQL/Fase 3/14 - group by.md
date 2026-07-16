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
2. ¿Qué ciudades aparecerán?
3. ¿Qué valor tendrá `La Plata`?
4. ¿Por qué no devuelve una sola fila?
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
2. ¿Cuántas filas devolverá?
3. ¿Por qué `La Plata` no aparece?
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
2. Si pensás que no, explicá por qué.
3. ¿Qué regla de `GROUP BY` se está incumpliendo?
---
## 💼 Caso de negocio

### 📧 Mensaje del gerente comercial

> Necesito saber cuántos clientes tenemos en cada ciudad para planificar la próxima campaña de marketing.

Como siempre, seguí nuestra metodología.
1.  Análisis

```
Análisis

Columnas:
Tabla(s):
Condiciones (WHERE):
Agrupación (GROUP BY):
Orden (ORDER BY):
Límite (LIMIT):
Operaciones especiales:
Observaciones:
```

> **Nota:** A partir de este tema, agregaremos una nueva sección al análisis: **Agrupación (`GROUP BY`)**, porque ya forma parte de la estructura lógica de una consulta.

2. Escribí la consulta SQL.