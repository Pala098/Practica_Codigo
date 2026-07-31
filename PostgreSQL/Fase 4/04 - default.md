# Actividad de comprensión
## Parte 1 
Conceptos
1. Con tus palabras:
	**¿Qué problema resuelve `DEFAULT`?**
	No repitas la definición; explicá por qué resulta útil.

	El problema que resuelve es el hecho de tener que estar cargando datos que pueden omitirse, por diferentes motivos, por el usuario. Permitiendo establecer un valor predeterminado para ciertas columnas en las cuales tengamos que tener un dato cargado, pero que puede omitirse por algún motivo.

---
2. Explicá la diferencia entre:
	- `DEFAULT`
	- `NOT NULL`
	Hablá del propósito de cada uno.

	`default` tiene como propósito establecer un valor automático en caso que no se proporcione un registro para esa columna.
	`not null` tiene como fin obligar al usuario a cargar si o si un registro en la columna establecida.

---
3. Analizá la siguiente definición:

```
stock INTEGER NOT NULL DEFAULT 0
```

Respondé:
1. ¿Qué garantiza `NOT NULL`?
	`not null` garantiza que no puedo no tener un registro, o no puede tener `null` como valor en esa columna.
2. ¿Qué hace `DEFAULT 0`?
	Establece un valor automático, en este caso 0.
3. ¿Qué ocurrirá si el usuario inserta un producto sin indicar el stock?
	Se completara automáticamente con 0 por defecto.
4. ¿Qué ocurrirá si el usuario indica un stock de 25?
	Se guardara el registro con el valor que se indica, en este caso 25.

---
4. ¿Creés que sería una buena idea definir esta columna así?

```
precio NUMERIC DEFAULT 0
```

Justificá tu respuesta pensando en un sistema real.



---
## Parte 2
Diseño de TechStore

Para cada columna decidí si utilizarías `DEFAULT` o no, y explicá por qué.

| Columna         | ¿DEFAULT?                             | Valor (si aplica) | Justificación |
| --------------- | ------------------------------------- | ----------------- | ------------- |
| `stock`         | ¿Sí o No?                             | ?                 | ?             |
| `estado_pedido` | ¿Sí o No?                             | ?                 | ?             |
| `precio`        | ¿Sí o No?                             | ?                 | ?             |
| `fecha_alta`    | ¿Sí o No? _(por ahora sin funciones)_ | ?                 | ?             |
| `descripcion`   | ¿Sí o No?                             | ?                 | ?             |

---

## Mini desafío de análisis

El encargado de depósitos propone lo siguiente:

> "Todos los productos nuevos deberían crearse automáticamente con un stock de **100**, así nadie se olvida de cargarlo."

Como diseñador de la base de datos:

- ¿Estás de acuerdo o no?
- ¿Qué ventaja podría tener esa idea?
- ¿Qué problemas podría generar en el funcionamiento del sistema?

No escribas SQL. Analizá la decisión desde el punto de vista del diseño de una base de datos.