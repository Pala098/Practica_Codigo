# Actividad de comprensión
## Parte 1
Conceptos
1. Con tus palabras:
	**¿Qué problema resuelve la restricción `UNIQUE`?**
	No repitas la definición; explicá por qué resulta útil.

	El problema que resuelve `unique` es el de almacenar valores repetidos, permite que ciertos columnas solo tengan un valor único, y no repetido.
> [!bug|borde] Correccion
> Solo haría un pequeño ajuste de redacción:
> > "Evita que se almacenen valores duplicados en columnas donde el negocio exige que cada valor sea único."
>
> ¿Por qué agrego "donde el negocio exige"?
> Porque no todas las columnas deben ser únicas. Esa decisión depende de las reglas del negocio.

---
2. Explicá con tus palabras la diferencia entre:
- `PRIMARY KEY`
- `UNIQUE`
No hables de la sintaxis; hablá del propósito de cada una.
La diferencia principal es que `primary key` es para identificar cada registro, teniendo ciertas características, mientras que `unique` permite que cada columna contenga valores no repetido, pero también varias columnas pueden tener esta misma característica a diferencia de `pk` que solo puede ser una por tabla.

---
3. Imaginá la siguiente tabla:

| id  | nombre | email          |
| --- | ------ | -------------- |
| 1   | Ana    | ana@email.com  |
| 2   | Juan   | juan@email.com |
| 3   | Pedro  | ana@email.com  |

Respondé:

1. ¿Qué problema observás?
	En el registro 1 y 3 tenemos el mismo email.
2. ¿Qué restricción evitaría esa situación?
	La restricción que evitaría esta situación es `unique`.
3. ¿Por qué no alcanzaría con que `id` fuera `PRIMARY KEY`?
	Porque podemos tener el `id` pero pongamos la situación que queremos obtener el correo de el registro 1 y 3, daríamos con que esta duplicado y esto es un problema.

> [!bug|borde] Correccion
> La idea general es correcta, aunque la justificaría de otra manera.
> La razón principal es esta:
> La `PRIMARY KEY` solo garantiza que el **id** sea único.
> No dice absolutamente nada sobre la columna `email`.
> Por lo tanto, podrían existir perfectamente dos filas como:
> 
> |id|email|
> |---|---|
> |1|ana@email.com|
> |2|ana@email.com|
> 
> La `PRIMARY KEY` seguiría siendo válida porque los `id` son distintos.
> El problema es que el correo electrónico quedó duplicado.

---
4. ¿Es correcto que una tabla tenga varias columnas con `UNIQUE`?
	Explicá el motivo.
	Si, porque pueden exitir diferentes columnas en las cuales necesitemos que los datos sean unicos.

---
## Parte 2
Diseño de TechStore

Para cada columna indicá si usarías `UNIQUE` o no, y justificá tu decisión.

| Columna             | ¿UNIQUE? | Justificación                                                 |
| ------------------- | -------- | ------------------------------------------------------------- |
| `id`                | Si       | Es un valor que debe ser unico                                |
| `nombre` (producto) | No       | Porque podemos tener productos con el mismo nombre            |
| `codigo_producto`   | Si       | Porque no podemos tener dos productos con un mismo codigo     |
| `precio`            | No       | Porque podemos tener diferentes productos con el mismo precio |
| `email_cliente`     | Si       | Porque cada cliente debe tener un email unico.                |
| `telefono_cliente`  | Si       | Porque cada cliente debe tener solo un teléfono asociado      |

> **Nota:** Para este ejercicio asumí que en TechStore cada cliente solo puede tener un correo electrónico y un único número de teléfono registrado.

---
## Mini desafío de análisis

El gerente propone la siguiente idea:

> "Como el `email` ya tiene `UNIQUE`, entonces no hace falta tener una columna `id`."

Como diseñador de la base de datos:
- ¿Estás de acuerdo o no?
	No.
- ¿Qué ventajas podría parecer que tiene esa idea?
	La decisión de dejar el email en cuenta de id presentan la única ventaja de que serán valores únicos y no repetidos.
- ¿Qué problemas podría traer en un sistema que crecerá con el tiempo?
	El problema que traería es que el correo puede cambiar, puede modificarse y ademas seria muy difícil a la hora de hacer consultas porque no recordaríamos el email exacto y seria muy engorroso buscar uno por uno o estar adivinando.