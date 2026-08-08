## Parte 1

1. Con tus palabras:
	**¿Qué problema resuelve `ADD COLUMN`?**
	No repitas la sintaxis. Explicá qué necesidad del negocio puede solucionar.

El problema que resuelve `add column` es el de poder modificar la estructura de una tabla, agregando un nuevo atributo a una entidad, sin tener que eliminar toda su estructura y volverla a crear desde 0, evitando también la pedida de datos ya cargados..

---
2. Tenemos:

```
productos (
    id,
    nombre,
    precio
)
```

Ejecutamos:

```
ALTER TABLE productos
ADD COLUMN stock INTEGER;
```

Respondé:

1. ¿Qué cambió?
	Agregamos una nueva columna, quedando:
	```
	productos (
		id,
		nombre,
		precio,
		stock
	)
	```
2. ¿Qué ocurrió con los registros existentes?
	Nada, siguen existiendo, pero al agregar una nueva columna se agrega en esta columna como valor `null`.
3. ¿Qué valor tendrán inicialmente en `stock`?
	Como no se preestablece ningún valor, tendrá inicialmente `null`.
4. ¿Se modificaron los valores de `nombre` o `precio`?
	No, no se modificaron, siguen igual.
---
3. Tenemos:

```
ALTER TABLE productos
ADD COLUMN stock INTEGER DEFAULT 0;
```

Respondé:

1. ¿Qué valor tendrá `stock` para los productos existentes?
	El valor que tendrá `stock` para los productos existentes será de `0`.
2. ¿Qué ocurrirá si posteriormente insertamos un producto sin indicar `stock`?
	Al tener `default = 0` este será el valor por defecto si no se indica un valor en `stock`.
3. ¿Qué ocurrirá si insertamos un producto indicando `stock = 50`?
	Ese registro quedara con el valor que se indico, que es `stock = 50`.

---
## Parte 2
*DDL vs DML*

Analizá cada operación:

### A

```
ALTER TABLE productos
ADD COLUMN stock INTEGER;
```

### B

```
UPDATE productos
SET stock = 20;
```

Respondé:

1. ¿Cuál modifica la estructura?
	La operación que modifica la estructura es la 'A'.
2. ¿Cuál modifica los datos?
	La operación que modifica los datos es la 'B'.
3. ¿A qué categoría pertenece cada una: DDL o DML?
	La operación "A" pertenece a la categoría de DDL, mientras que la "B" pertenece a DML.
4. ¿Por qué no son equivalentes?
	Porque manipulan diferentes aspectos de una base de datos, mientras que DDL toca la estructura, DML trabaja con los datos dentro de la base.

---

# 🧩 Desafío de análisis

TechStore ya tiene **10.000 productos registrados**.

El negocio decide agregar una columna:

```
codigo_barras
```

Y establece que:

- cada producto debe tener un código;
- no puede haber códigos repetidos;
- algunos productos antiguos todavía no tienen código asignado.

Sin escribir SQL todavía, analizá:

1. ¿Qué problema presenta agregar directamente la columna como obligatoria?
	Al tener productos antiguos que aun no tiene un código asignado tendremos el problema que si o si debemos asignar un valor a estos registros, de lo contraria la base de datos tendría conflictos.
2. ¿Conviene que inicialmente permita `NULL`?
	Sabiendo que hay productos antiguos los cuales no tienen codigo, si, seria conveniente que inicialmente permita `null`.
3. ¿Qué debería hacerse con los productos antiguos?
	Tratar de actualizar su información y cargar los códigos de los productos faltantes.
4. ¿En qué momento tendría sentido establecer `NOT NULL`?
	Una vez que se tengan todos los registros con sus respectivos datos cargados, o si se decide establecer un valor por defecto.
5. ¿En qué momento tendría sentido establecer `UNIQUE`?
	En el momento en el cual cada producto tenga su codigo correctamente cargado.