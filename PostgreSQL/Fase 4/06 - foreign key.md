## Parte 1
Conceptos

1. Con tus palabras:
	**¿Qué problema resuelve una `FOREIGN KEY`?**
	No repitas la definición. Explicá qué necesidad cubre en una base de datos.

Una `foreign key`  resuelve el problema de la relaciona entre tablas, es decir, permite relacionar dos o mas tablas entre si, como así también garantiza que un valor exista previamente en una tabla.

---
2. ¿Cuál es la diferencia entre una `PRIMARY KEY` y una `FOREIGN KEY`?
	Intentá explicarlo pensando en el rol que cumple cada una.

La diferencia entre amas en si es por su función, en donde, una `priamry key` identifica un registro de forma única y una `foreign key` relaciona un registro con otro de otra tabla.

---
3. Analizá las siguientes tablas:

**Clientes**

| id_cliente | nombre |
| ---------- | ------ |
| 1          | Ana    |
| 2          | Juan   |
| 3          | Pedro  |

**Ventas**

| id_venta | id_cliente |
| -------- | ---------- |
| 1        | 2          |
| 2        | 3          |
| 3        | 8          |

Respondé:
1. ¿Qué problema observás?
	En la tabla `ventas` tenemos un valor que no existe, en la tabla `clientes`, el cual es `id_cliente = 8`
2. ¿Qué restricción impediría esa situación?
	La restricción que impediría esta situación es la de establecer la columna `id_cliente` de la tabla `ventas` como `foreign key` para que las relaciones solo sean con valores existentes.
3. ¿Por qué PostgreSQL debería rechazar ese registro?
	Porque no existe un valor asociado a `id_cliente = 8` y esto generaría un conflicto.

> [!quote] Dato
> Utilizaste una idea importante:
> > *"...generaría un conflicto."*
> 
> Exactamente.
> Ese conflicto se llama **violación de integridad referencial**.

---
4. Respondé **Verdadero o Falso** y justificá:
	a) Una `FOREIGN KEY` siempre debe apuntar a una `PRIMARY KEY`.
		Verdadero, esto porque es quien relaciona las tablas.

> [!bug] Corrección
> **Casi correcta.**
> Para el nivel actual está bien responder Verdadero.
> Pero quiero agregar un detalle profesional.
> Una `FOREIGN KEY` puede apuntar a:
> 	- una `PRIMARY KEY`
> 	- o una columna `UNIQUE`
> Por ejemplo:
> ```
> usuarios
> ---------
> id
> email UNIQUE
> ```
> Una tabla podría referenciar el email.
> Por ahora seguí pensando:
> 
> > FOREIGN KEY → PRIMARY KEY
>
> porque es el caso más habitual

b) Una `FOREIGN KEY` puede repetirse muchas veces.
	Verdadero, porque podemos tener varias `foreing key`, ya que una tabla puede estar asociada con una o muchas entidades.

> [!bug] Corrección
> **Ojo con la justificación**
> Vos escribiste:
> > *"...porque podemos tener varias foreign keys..."*
> 
> Eso no explica exactamente la pregunta.
> La pregunta era:
> > *¿Puede repetirse el valor?*
>
> La respuesta correcta sería:
> > *Sí. Porque varios registros pueden apuntar al mismo registro de otra tabla.*
> 
> Ejemplo:
> ```
> Cliente 1
> ```
> Puede tener:
> ```
> Venta 1
> Venta 2
> Venta 3
> Venta 4
> ```
> Todas con:
> ```
> id_cliente = 1
> ```

c) Una `PRIMARY KEY` puede contener valores repetidos.
	Falso, una `primary key` debe ser única para cada registro.
d) Una tabla puede tener más de una `FOREIGN KEY`.
	Verdadero, como en la respuesta del punto b, esto porque podemos tener varias entidades relacionadas con una misma tabla.

---
## Parte 2
Diseño de TechStore

Imaginá que queremos modelar estas tablas:
### Clientes

- `id_cliente`
- `nombre`

### Ventas

- `id_venta`
- `fecha`
- `id_cliente`

Respondé:
1. ¿Qué columna debería ser la `PRIMARY KEY` de `clientes`?
	La `primary key` para clientes seria `id_cliente`.
2. ¿Qué columna debería ser la `PRIMARY KEY` de `ventas`?
	La `primary key` para ventas seria `id_venta`.
3. ¿Cuál debería ser la `FOREIGN KEY`?
	La `foreing key` seria `id_cliente` de la tabla ventas.
4. ¿Qué relación existe entre ambas tablas?
	La relación que existe es que un cliente puede tener muchas ventas, y muchas o una venta pueden  pertenecer a un cliente.
5. ¿Qué problema evitaría esa relación?
	El problema principal es que se evitarían ventas fantasmas, es decir, que se adjudiquen ventas a clientes que no existen.

---
# 🧩 Desafío de análisis

Un compañero propone este diseño:

**Ventas**

|id_venta|nombre_cliente|
|---|---|
|1|Ana|
|2|Juan|
|3|Pedro|

Dice:

> "No hace falta guardar el `id_cliente`; con el nombre alcanza."

Como diseñador de la base de datos, respondé:

- ¿Estás de acuerdo o no?
	No.
- ¿Qué ventaja aparente tiene esa idea?
	Que en este caso quedaría mas clara a la hora de una lectura, porque se ven directamente los nombres.
- ¿Qué problemas aparecerían cuando el sistema crezca o cambien los datos de los clientes?
	Que pueden aparecer errores de tipeo, o directamente ingresar valores por error. Entonces no se tiene certeza absoluta de que valores son correctos o no, cuales pueden tener error o no. O también cual es el verdadero id de un mismo cliente.