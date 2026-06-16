Sin ejecutar.
1. `select * productos where precio < 100;`
	Que productos aparecen ? 
		Los productos que aparecen son 'Mouse', 'Teclado' y 'Auriculares'

2. `select * from clientes where nombre <> 'Ana';`
	1. Que significa `<>`?
		 Que trae todos los datos que no contengan el valor 'Ana'
	2. Que clientes aparecerán ?
		Los clientes que aparecen son 'Juan', 'Pedro', 'Maria' y 'Lucia'.
	
3. `select * from productos where >= 90;`
	1. Que productos aparecerán ?
		Aparecen 'Auriculares', 'Monitor' y 'Notebook'.

4. `select * from productos where precio <= 70;`
	1. Que productos aparecerán ?
		Aparecen 'Mouse' y 'Teclado'.

5. `select * from clientes where id_cliente > 3;`
	1. Cuantas filas devolverá ?
		Devolverá 2 filas.
	2. Que nombres aparecerán ?
		Aparecer 'Maria' y 'Lucia'.
	3. Cuantas columnas devolverá ?
		Devolverá 3 columnas (id_cliente, nombre y ciudad)

6. `select * from productos where precio <= 70;`
	1. Que productos aparecerán ?
		Aparecen 'Mouse' y 'Teclado'.
7. `select nombre from clientes where id_cliente > 3;`
	1. Cuántas filas devolverá?
		2 filas.
	2. Qué nombres aparecerán?
		'Maria' y 'Lucia'.
	3. Cuántas columnas devolverá?
		1 columna.
8. `select producto from productos where precio <> 300;`
	1. Que producto NO aparecerá ?
		Los producto que tienen el valor de 300, es decir, 'Monitor'
	2. Cuantas filas crees que devolverá ?
		Devolverá 4 filas.
