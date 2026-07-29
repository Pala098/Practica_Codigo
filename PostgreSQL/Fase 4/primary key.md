# Actividad de comprensión
## Parte 1
Conceptos
1. Con tus palabras:

> ¿Qué problema resuelve una `PRIMARY KEY`?

No repitas la definición; explicá la necesidad que viene a solucionar.

*La primary key resuelve el problema de identificar cada registro, es decir, saber exactamente a cual registro queremos apuntar, ya que si en este dato, podríamos tener valores repetidos dentro de una tabla y causaría un conflicto interno o a futura tanto a la hora de hacer operaciones como de realizar la  estructura general de una BD.*

---
2. ¿Por qué no sería una buena idea usar el nombre de un cliente como clave primaria?
	Mencioná al menos **dos motivos**.
	- Porque este valor puede ser modificado a futuro
	- Porque puede existir la posibilidad de tener registros exactamente iguales
---
3. Imaginá la siguiente tabla:

| id  | nombre |
| --- | ------ |
| 1   | Ana    |
| 2   | Juan   |
| 2   | Pedro  |

Responde:
1. ¿Qué problema observás?
	Tenemos duplicado el valor 2  en la columna `id`.
2. ¿Por qué PostgreSQL no debería permitir esta situación?
	Porque afectaría a operaciones de consulta a futuro, y no sabe diferencia a que registro queremos hacer referencia.
---
4. ¿Puede una `PRIMARY KEY` tener un valor `NULL`?
	Explicá el motivo con tus propias palabras.
	No, porque es una valor que debe estar cargado obligatoriamente ya que no podremos distinguir los registros.
---
## Parte 2
Diseño de TechStore
Analizá las siguientes tablas y elegí cuál sería la mejor **PRIMARY KEY** para cada una. Justificá tu decisión.

| Tabla                                 | ¿Qué columna elegirías como PRIMARY KEY? | ¿Por qué?                                                      |
| ------------------------------------- | ---------------------------------------- | -------------------------------------------------------------- |
| clientes (`id`, `nombre`, `telefono`) | `id`                                     | Porque es un valor identifica a cada registro de manera unica. |
| productos (`id`, `nombre`, `precio`)  | `id`                                     | Porque es un valor identifica a cada registro de manera unica. |
| ventas (`id`, `fecha`, `total`)       | `id`                                     | Porque es un valor identifica a cada registro de manera unica. |

---

## Mini desafío de análisis

Imaginá que el dueño de TechStore propone esto:

> "No hace falta un `id` en la tabla `productos`. Podemos usar el nombre del producto como identificador porque nunca vendemos dos productos con el mismo nombre."

**¿Estás de acuerdo?**

Respondé como si fueras el desarrollador encargado del proyecto y justificá tu decisión. No hay que escribir SQL; quiero ver tu razonamiento.

No, por mas que el dueño afirme esto, no podemos descartar la posibilidad de que existan productos que se llamen igual o hasta que tengan alguna palabra que compone su nombre similar a otros, por ejemplo, si tuviéramos que buscar 'teclado', y en la tabla tenemos 'teclado inalámbrico' y 'teclado USB', si buscamos por solo 'teclado' no podremos identificarlo correctamente en una búsqueda especifica.
