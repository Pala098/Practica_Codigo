## Parte 1
Conceptos

1. Con tus palabras:
	**¿Qué problema resuelve una `FOREIGN KEY`?**
	No repitas la definición. Explicá qué necesidad cubre en una base de datos.
---
2. ¿Cuál es la diferencia entre una `PRIMARY KEY` y una `FOREIGN KEY`?
	Intentá explicarlo pensando en el rol que cumple cada una.
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
2. ¿Qué restricción impediría esa situación?
3. ¿Por qué PostgreSQL debería rechazar ese registro?
Justificá tus respuestas.
---
4. Respondé **Verdadero o Falso** y justificá:
	a) Una `FOREIGN KEY` siempre debe apuntar a una `PRIMARY KEY`.
	b) Una `FOREIGN KEY` puede repetirse muchas veces.
	c) Una `PRIMARY KEY` puede contener valores repetidos.
	d) Una tabla puede tener más de una `FOREIGN KEY`.
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
2. ¿Qué columna debería ser la `PRIMARY KEY` de `ventas`?
3. ¿Cuál debería ser la `FOREIGN KEY`?
4. ¿Qué relación existe entre ambas tablas?
5. ¿Qué problema evitaría esa relación?

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
- ¿Qué ventaja aparente tiene esa idea?
- ¿Qué problemas aparecerían cuando el sistema crezca o cambien los datos de los clientes?