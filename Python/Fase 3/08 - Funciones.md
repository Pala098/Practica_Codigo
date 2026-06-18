## 1. Mensaje de bienvenida
Crear una función que muestre *Bienvenido al sistema*. 
Mostrar este mensaje 3 veces.

```python
def saludar():
	print('Bienvenido al sistema')

for i in range(0,3):
	saludar()
```

## 2. Encabezado reutilizable
Crear una función que muestre el siguiente formato: 
```
--------------------
REGISTRO DE CLIENTES
--------------------
```
Invocarlo 2 veces.

```python
def encabezado():
	deco = '-' * 20
	print(f'{deco}\nREGISTRO DE CLIENTES\n{deco}')

for i in range(0,2):
	encabezado()
```

## 3. Menú principal
Crear una función que muestre: 
```
1. Alta
2. Baja
3. Modificacion
4. Salir
```
Invocarla 1 vez.

```python
def menu():
	print(f'1. Alta\n2. Baja\n3. Modificiacion\n4. Salir')

menu()
```

## 4. Reporte de empleados
Crear una función que muestre: 
```
REPORTE DE EMPLEADOS
```
y debajo una lista fija de 3 empleados utilizando una lista.
La lista debe recorrerse dentro de la función.

```python
def reporte_empleados():
	lista = ['Diana', 'Nita', 'Morfy']
	deco = '-' * 20
	print(f'REPORTE DE EMPLEADOS\n{deco}')
	for empleado in lista:
		print(f'- {empleado}')

reporte_empelados()
```

## 5. Desafío integrador
Crear dos funciones:
1. Debe mostrar:
```
1. Registrar venta
2. Ver venta
3. Salir
```
2. Debe mostrar
```
Sistema desarrollado en Python
```
Luego construir un programa principal que llame a ambas funciones.

```python
def menu_principal():
	deco = '-' * 20
	print(f'..:: MENU::..\n{deco}\n1. Registrar venta\n2. Ver venta\n3. Salir')

def mensaje_dev():
	print('Sistema desarrollado en Python')

deco = '-' * 20

menu_principal()
print(deco)
mensaje_dev()
print(devo)
```

## Razonamiento
Sin ejecutar nada: 
```python
def mensaje():
    print('Hola')

print('Inicio')

mensaje()

mensaje()

print('Fin')
```
Preguntas:
1. ¿Qué imprime el programa?
	Imprime:
	1. 'Inicio'
	2. 'Hola'
	3. 'Hola'
	4. 'Fin'
2. ¿Cuántas veces se ejecuta la función?
	Se ejecuta 2 veces
3. ¿En qué momento se ejecuta realmente el código dentro de `mensaje()`?
	Se ejecuta luego del llamado, en este caso de los dos llamados.
4. ¿Cuál es la diferencia entre:
```python
def mensaje():
```
y
```python
mensaje()
```

La diferencia es que `def mensaje()` es la definición de la función, donde se la crea y se establece que va a hacer, y `mensaje()` es la ejecución, o llamado de la función, donde realiza las acciones dentro de esta.