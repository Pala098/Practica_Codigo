1. Realizar una consulta para obtener --> *Mostrar únicamente los nombres de los productos*
	Esta es la tabla en cuestión.
	

| id_producto | producto | precio |
| ----------- | -------- | ------ |
|             |          |        |
```sql
SELECT nombre FROM productos; --✖
-- SELECT producto FROM productos;
```

2. Escribir una consulta que muestre: 
	- Nombre del producto
	- Precio
	De la tabla productos.

```sql
select producto, precio from productos;
```
## Ronda de consolidación
1. Mostrar únicamente las ciudades de los clientes.

```sql
select ciudades from clientes; # ✖ --> 'ciudad'
```

2. Mostrar:
	- id_cliente
	- nombre
	De la tabla clientes

```sql
select id_cliente, nombre from clientes;
```

3. Mostrar:
	- id_producto
	- producto
	- precio
	De la tabla productos.

```sql
select id_producto, producto, precio from productos;
```