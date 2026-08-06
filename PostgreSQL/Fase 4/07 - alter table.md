## Parte 1 
*Conceptos*
1. Con tus palabras:
	**¿Qué problema resuelve `ALTER TABLE`?**
	No repitas la definición. Explicá qué necesidad cubre en un proyecto real.

El problema que resuelve es si tenemos que modificar algún valor en la estructura de una tabla, ya sea agregar un nuevo atributo, modificar su nombre, eliminarlo, cambiar el tipo de dato, cambiar el mismo nombre de la tabla.

---
2. Explicá la diferencia entre:
	- `CREATE TABLE`
	- `ALTER TABLE`
	¿En qué situaciones utilizarías cada uno?

`create table` es de uso único, es decir, se utiliza solo para crear una tabla nueva inexistente y solo se puede ejecutar una vez. Mientras que `alter table` se utiliza para modificar la estructura de una tabla ya creada, y se puede utilizar múltiples veces.

---
3. Imaginá la siguiente situación.
	Existe esta tabla:

```
productos
---------
id
nombre
precio
```

El dueño de TechStore quiere agregar una columna llamada `stock`.
Respondé:
1. ¿Hace falta crear una tabla nueva?
	No, ya tenemos la tabla que necesitamos, solo debemos agregar un nuevo atributo.
2. ¿Qué comando utilizarías?
	Utilizaría `alter table` para alterar la estructura de la tabla y agregar esta nueva columna
3. ¿Qué ocurrirá con los productos que ya estaban cargados?
	Nada, seguirán cargados pero en esta nueva columna tendrán asignado el valor de `null`, o un valor definido si lo establecemos.
4. ¿Se perderán los datos existentes?
	No, no se perderán los datos existentes. Seguirán los mismos datos pero con un atributo mas agregado, el cual no tenemos aun cargado.
Justificá cada respuesta.
---
4. Analizá este caso.
	Una tabla ya tiene miles de registros y el negocio decide agregar una columna `descripcion`.
	¿Por qué sería una mala idea eliminar la tabla y crearla nuevamente?
	Pensá en un sistema que ya está siendo utilizado por clientes.

	La razón única y mas importante, toda la información ya cargada se perderá, y crear una tabla nueva es volver a cargar toda la información desde cero.

---
## Parte 2
*Análisis de cambios*

Para cada situación, indicá si usarías `CREATE TABLE` o `ALTER TABLE` y justificá.

| Situación                                                | ¿Qué usarías?  | ¿Por qué?                                                               |
| -------------------------------------------------------- | -------------- | ----------------------------------------------------------------------- |
| Crear la tabla `clientes` por primera vez                | `create table` | La tabla en cuestión aun no existe                                      |
| Agregar la columna `telefono` a `clientes`               | `alter table`  | Tenemos la tabla solo queremos agregar un nuevo atributo                |
| Cambiar el nombre de una columna                         | `alter table`  | La columna ya existe, solo queremos su nombre                           |
| Agregar una nueva restricción `CHECK`                    | `alter table`  | El atributo ya se estableció, queremos agregarle una nueva restricción  |
| Crear una tabla completamente nueva llamada `categorias` | `create table` | Asumimos que la tabla no existe, entonces la estamos creando desde cero |

---

# 🧩 Desafío de análisis
Un compañero propone lo siguiente:

> "Cada vez que haya que agregar una columna, eliminemos la tabla y la volvemos a crear. Es más simple."

Como diseñador de la base de datos, respondé:

- ¿Estás de acuerdo o no?
	No
- ¿Qué ventaja aparente tiene esa idea?
	Que la estructura de la tabla estará acorde a lo que se busca.
- ¿Qué problemas puede generar en una aplicación que ya está en producción?
	Que se pierden los datos y relaciones en la estructura de la base de datos.
- ¿Cómo afectaría a los usuarios y a la información almacenada?
	Se pierde toda su información ya cargada y además su información al volverla a cargar puede tener modificaciones.