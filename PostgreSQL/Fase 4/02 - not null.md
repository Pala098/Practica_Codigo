# Actividad de comprensión
## Parte 1 
Conceptos
1. Con tus palabras:
	**¿Qué problema resuelve la restricción `NOT NULL`?**
	No repitas la definición; explicar por qué resulta útil.
	Resuelve el problema de que se cargue datos necesarios vacíos, es decir, que nos ayuda a no permitir datos en sin completar o en blanco.
> [!bug|borde] Correccion
> Solo haría una pequeña precisión en la redacción.
> Dijiste:
> > "...datos vacíos..."
> 
> En realidad sería más correcto decir:
> > "...evita que se almacenen registros sin información obligatoria."
> 
> ¿Por qué hago esta aclaración?
> Porque un dato "vacío" (`''`) y un dato `NULL` son cosas distintas, como vimos en la teoría.

---
2. Explicar con tus palabras la diferencia entre:
	- un valor `NULL`;
	- una cadena vacía (`''`).
	Un valor con `null` significa que no se cargo nada, es decir sin nada o ningún tipo de dato.
	Una cadena vacía indica que se cargo algo pero esta vació, pero existe dentro de la tabla.
---
3. Imaginá esta tabla:

| id  | nombre  | precio |
| --- | ------- | ------ |
| 1   | Mouse   | 25.00  |
| 2   | NULL    | 40.00  |
| 3   | Monitor | NULL   |

Responder:
1. ¿Qué registros serían un problema si `nombre` y `precio` fueran obligatorios?
	Ninguno.
> [!bug|borde] Correccion
> La pregunta era:
> > ¿Qué registros serían un problema?
> 
> Vos respondiste:
> > Ninguno.
> 
> ✗ En este caso no.
> Los registros problemáticos serían:
> - Registro 2 → porque `nombre` es `NULL`.
> - Registro 3 → porque `precio` es `NULL`.
> 
> Si esas columnas fueran `NOT NULL`, ambos registros serían inválidos.
1. ¿Por qué?
	Porque si `nombre` y `precio` fueran obligatorios, tendria que si o si cargar un dato.

---
4. ¿Es correcto marcar **todas** las columnas de una tabla como `NOT NULL`?
	Justificar tu respuesta.
	No, porque dentro de una tabla puede existir columnas que no es necesario o vital que tenga un valor almacenado o cargado.
---
## Parte 2
Diseño de TechStore
Para cada columna indicar si usarías `NOT NULL` o permitirías `NULL`, y explicar por qué.

| Columna       | ¿NOT NULL o NULL? | Justificación                                                                                                                           |
| ------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `id`          | `not null`        | Es un dato vital para la identificacion de los registros (igualmente `not null` no se utiliza, ya que este siempre es la PK mayormente) |
| `nombre`      | `not null`        | Es lo que nos indica el nombre de un producto, de faltar no sabriamos a que producto pertenece una descripcion                          |
| `precio`      | `not null`        | Al igual que el nombre, es importante para saber el precio  que se tiene, y también para realizar ciertas operaciones matemáticas.      |
| `stock`       | `not null`        | Al igual que el nombre, es importante para saber la cantidad que se tiene, y también para realizar ciertas operaciones matemáticas.     |
| `descripcion` | `null`            | Se puede omitir la descripcion, se puede agregar a futuro o simplemente omitirla.                                                       |
| `fecha_alta`  | `not null`        | Tener un registro de la fecha exacta ayuda a tener mucho mejor control y análisis.                                                      |

---
## Mini desafío de análisis
El gerente propone lo siguiente:

> "Hagamos que **todas** las columnas sean `NOT NULL`. Así nunca faltará información."

Como desarrollador de la base de datos:
- ¿Estás de acuerdo?
	No.
- ¿Qué ventajas tendría esa idea?
	Que tendremos obligatoriamente que cargar todos los campos de una tabla y esto permite tener toda la información de un elemento que estamos trayendo de la vida real.
- ¿Qué problemas podría generar?
	Viéndolo con un ejemplo si tenemos un elemento pero no sabemos la descripción de este por x motivos, o la información en el momento de un campo en particular, entonces sera un freno para cargar a la base de datos.