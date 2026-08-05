## Parte 1 
*Conceptos*
1. Con tus palabras:
	**¿Qué problema resuelve `ALTER TABLE`?**
	No repitas la definición. Explicá qué necesidad cubre en un proyecto real.
---
2. Explicá la diferencia entre:
	- `CREATE TABLE`
	- `ALTER TABLE`
	¿En qué situaciones utilizarías cada uno?
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
2. ¿Qué comando utilizarías?
3. ¿Qué ocurrirá con los productos que ya estaban cargados?
4. ¿Se perderán los datos existentes?
Justificá cada respuesta.
---
4. Analizá este caso.
	Una tabla ya tiene miles de registros y el negocio decide agregar una columna `descripcion`.
	¿Por qué sería una mala idea eliminar la tabla y crearla nuevamente?
	Pensá en un sistema que ya está siendo utilizado por clientes.
---
## Parte 2
*Análisis de cambios*

Para cada situación, indicá si usarías `CREATE TABLE` o `ALTER TABLE` y justificá.

|Situación|¿Qué usarías?|¿Por qué?|
|---|---|---|
|Crear la tabla `clientes` por primera vez|?|?|
|Agregar la columna `telefono` a `clientes`|?|?|
|Cambiar el nombre de una columna|?|?|
|Agregar una nueva restricción `CHECK`|?|?|
|Crear una tabla completamente nueva llamada `categorias`|?|?|

---

# 🧩 Desafío de análisis
Un compañero propone lo siguiente:

> "Cada vez que haya que agregar una columna, eliminemos la tabla y la volvemos a crear. Es más simple."

Como diseñador de la base de datos, respondé:

- ¿Estás de acuerdo o no?
- ¿Qué ventaja aparente tiene esa idea?
- ¿Qué problemas puede generar en una aplicación que ya está en producción?
- ¿Cómo afectaría a los usuarios y a la información almacenada?