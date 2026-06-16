1. Mostrar todos los datos del cliente llamado:
```
Pedro
```

```sql
select * from clientes where nombre = 'Pedro';
```

2. Mostrar todos los productos cuyo precio sea:
```
90.00
```

```sql
select * from productos where precio = 90.00;
```

3. Mostrar únicamente:
	- nombre
	- ciudad
	del cliente llamado:
```
Maria
```

```sql
select nombre, ciudad from clientes where nombre = 'Maria';
```