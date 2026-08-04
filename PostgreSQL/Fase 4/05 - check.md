# Actividad de comprensión

## Parte 1 – Conceptos

1. Con tus palabras:
	**¿Qué problema resuelve `CHECK`?**
	No repitas la definición. Explicá qué necesidad cubre.
	
	`check` resuelve el problema recibir datos erróneos, que estan dentro del tipo de dato que establecemos. Es decir, valores que se incluyen en el tipo de dato pero que no queremos tener en nuestra base de datos mediante una condición.
---
2. Explicá la diferencia entre:
	- `CHECK`
	- `NOT NULL`
	¿En qué se parecen y en qué se diferencian?

Lo que tiene de parecido es que tanto `check` como `not null` permiten que si o si se deba ingresar un dato y no sea `null`. La diferencia entre ellos es que `check` depende de una condición y `not null` establece que no puedo no haber un registro en la columna que lo establecemos.

> [!bug] Corrección
> Acá hay un pequeño detalle importante.
> Vos escribiste:
> > *Ambos permiten que sí o sí se deba ingresar un dato.*
> 
> **Esto no siempre es cierto.**
> `NOT NULL` sí obliga a que exista un valor.
> Pero `CHECK`, por sí solo, **no obliga a ingresar un dato**.
> Por ejemplo:
> ```
> precio NUMERIC CHECK (precio >= 0)
> ```
> Si insertamos:
> ```
> precio = NULL
> ```
> PostgreSQL **puede aceptarlo**, porque `CHECK` no reemplaza a `NOT NULL`.
> Por eso normalmente vemos ambas restricciones juntas:
> ```
> precio NUMERIC
> NOT NULL
> CHECK(precio >= 0)
> ```
> Entonces la diferencia sería:
> 	- `NOT NULL` → obliga a que exista un valor
> 	- `CHECK` → valida que ese valor cumpla una condición.
> Es una diferencia muy importante.

---
3. Analizá la siguiente columna:
```
precio NUMERIC NOT NULL CHECK (precio >= 0)
```
Respondé:
1. ¿Qué garantiza `NOT NULL`?
	Garantiza que se va a ingresar un dato, y no será `null`.
2. ¿Qué garantiza `CHECK`?
	`check` garantiza que el precio sera valores positivos y no negativos.
3. ¿Se podría guardar un precio de `-100`?
	No. Porque con la condición del `check` estamos estableciendo que no se aceptan valores por debajo del cero, es decir, negativos.
4. ¿Se podría guardar un `NULL`?
	No. Porque estamos estableciendo la regla `not null`, la cual no permite valores `null` y obliga a registrar un dato.
5. ¿Se podría guardar `2500`?
	Si. Porque cumple con la condición del `check`.
Justificá cada respuesta.
---
4. Imaginá que un profesor quiere almacenar notas de exámenes.
	¿Qué condición escribirías conceptualmente (sin preocuparte por la sintaxis exacta) para impedir que existan notas menores que 0 o mayores que 10?
	Explicá el razonamiento.

	La condición que escribiría seria `nota >= 0 and nota <= 10`, porque así establecemos un rango entre 0 y 10, y no permitirá valores por fuera de estos.

---
# Parte 2 – Diseño de TechStore
Indicá si usarías `CHECK` y qué regla aplicarías.

| Columna            | ¿CHECK? | Regla                   | Justificación                                           |
| ------------------ | ------- | ----------------------- | ------------------------------------------------------- |
| `precio`           | si      | `precio >= 0`           | evita que se ingresen valores negativos                 |
| `stock`            | si      | `stock >= 0`            | evita que se ingresen valores negativos                 |
| `descuento`        | si      | `decuento >= 0`         | no se puede calcular un descuento con valores negativos |
| `nombre`           | no      | ?                       | ?                                                       |
| `cantidad_vendida` | si      | `cantidad_vendida >= 0` | no existe valores negativos de algo vendido             |

---
# 🧩 Desafío de análisis

El dueño de TechStore propone:

> "No hace falta poner `CHECK`. Los empleados saben que un precio no puede ser negativo."

Como diseñador de la base de datos, respondé:
- ¿Estás de acuerdo o no?
	No.
- ¿Qué ventaja aparente tiene esa idea?
	Que se puede ingresar cualquier tipo de valor.

> [!bug] Corrección
> Acá reformularía un poco la idea.
> Esa no es realmente una ventaja; más bien es una consecuencia.
> La ventaja aparente sería:
> 	- menos restricciones;
> 	- menos trabajo al definir la tabla;
> 	- mayor flexibilidad para cargar datos.
> El problema es que esa flexibilidad también permite errores.

- ¿Qué riesgos genera confiar únicamente en que los usuarios nunca se equivocarán?
	Que si por error se carga un valor negativo este causara un futuro conflicto, y ni hablar si esto se repite en varios registros.