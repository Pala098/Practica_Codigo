# Actividad de comprensión
## Parte 1 
Conceptos
1. Con tus palabras:
	**¿Qué problema resuelve `DEFAULT`?**
	No repitas la definición; explicá por qué resulta útil.

	El problema que resuelve es el hecho de tener que estar cargando datos que pueden omitirse, por diferentes motivos, por el usuario. Permitiendo establecer un valor predeterminado para ciertas columnas en las cuales tengamos que tener un dato cargado, pero que puede omitirse por algún motivo.

> [!bug|borde] Correccion
> Solo haría un pequeño ajuste en esta frase:
> > "...en las cuales tengamos que tener un dato cargado..."
>
> No necesariamente debe ser un dato obligatorio. También puede aplicarse a una columna que admite `NULL`.
> Por ejemplo:
> ```
> observaciones TEXT DEFAULT 'Sin observaciones'
> ```
> La columna podría permitir `NULL`, pero si el usuario no envía nada, PostgreSQL escribirá "Sin observaciones".

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

Depende la situación, si lo pongo como ejemplo de una tienda de productos electrónicos puede pasar que tengan el producto pero por cierto motivo en ese mismo día no tiene el dato del precio, así que en este caso si seria una buena idea definirlo así. Pero si se tiene toda la información, no, porque el precio es un dato de importancia entonces lo mejor seria agregar `not null`.

---
## Parte 2
Diseño de TechStore

Para cada columna decidí si utilizarías `DEFAULT` o no, y explicá por qué.

| Columna         | ¿DEFAULT? | Valor (si aplica)                    | Justificación                                                                      |
| --------------- | --------- | ------------------------------------ | ---------------------------------------------------------------------------------- |
| `stock`         | Si        | `0`                                  | Porque puede que  en el el momento de cargar el registro no se tenga este dato.    |
| `estado_pedido` | Si        | `peniente`                           | Porque todo pedido puede estar pendiente                                           |
| `precio`        | No        | -                                    | Porque en general es un dato que no debería faltar                                 |
| `fecha_alta`    | Si        | fecha en la que se carga el registro | Porque es importante tener una fecha para registrar cuando se cargo la informacion |
| `descripcion`   | No        | -                                    | Es un dato no vital, que puede omitirse o cargar a futuro.                         |

---

## Mini desafío de análisis

El encargado de depósitos propone lo siguiente:

> "Todos los productos nuevos deberían crearse automáticamente con un stock de **100**, así nadie se olvida de cargarlo."

Como diseñador de la base de datos:

- ¿Estás de acuerdo o no?
	No.
- ¿Qué ventaja podría tener esa idea?
	La única ventaja que le encuentro es el hecho que se tendrá todos los productos con el valor de 100 por defecto.
- ¿Qué problemas podría generar en el funcionamiento del sistema?
	El problema esta en el valor, porque si no tenemos stock de un producto, este se almacenara con el valor de 100 osea que existe una cantidad fantasma de un producto que no se tiene.

No escribas SQL. Analizá la decisión desde el punto de vista del diseño de una base de datos.