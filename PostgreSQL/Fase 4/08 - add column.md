## Parte 1

1. Con tus palabras:
	**¿Qué problema resuelve `ADD COLUMN`?**
	No repitas la sintaxis. Explicá qué necesidad del negocio puede solucionar.
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
2. ¿Qué ocurrió con los registros existentes?
3. ¿Qué valor tendrán inicialmente en `stock`?
4. ¿Se modificaron los valores de `nombre` o `precio`?
---
3. Tenemos:

```
ALTER TABLE productos
ADD COLUMN stock INTEGER DEFAULT 0;
```

Respondé:

1. ¿Qué valor tendrá `stock` para los productos existentes?
2. ¿Qué ocurrirá si posteriormente insertamos un producto sin indicar `stock`?
3. ¿Qué ocurrirá si insertamos un producto indicando `stock = 50`?

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
2. ¿Cuál modifica los datos?
3. ¿A qué categoría pertenece cada una: DDL o DML?
4. ¿Por qué no son equivalentes?

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
2. ¿Conviene que inicialmente permita `NULL`?
3. ¿Qué debería hacerse con los productos antiguos?
4. ¿En qué momento tendría sentido establecer `NOT NULL`?
5. ¿En qué momento tendría sentido establecer `UNIQUE`?