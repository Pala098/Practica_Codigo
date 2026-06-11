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