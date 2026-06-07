1. Crear una lista vaciá, solicitar 5 nombres de invitados, guardar cada nombre con el formato 'Nombre', al finalizar mostrar:
```
Lista de invitados:
1. nombre
2. nombre
...	
```

```python
for i in range(0,3):
  invitados.append(input(f'Ingrese el nombre del invitado {i}: '))

print('Lista de invitados: ')
for i in range(len(invitados)):
  print(f'{i+1}. {invitados[i]}')
```

2. Crear una lista, solicitar 4 productos y luego mostrar todos los productos, la cantidad total de productos registrados. Como requisito se debe utilizar `append()` y `len()` dentro del programa.

```python
productos = []

for i in range(0,4):
	producto = input(f'Ingrese el producto {i + 1}: ')
	productos.append(producto)

print('Lista de productos: ')
for producto in productos:
	print(f'- {producto}')

print(f'Cantidad todal de productos: {len(productos)}')
```

3. Registrar 5 alumnos en una lista, luego solicitar un nombre. Indicar si el alumno existe dentro de esta lista o no.

```python
alumnos = []

for i in range(0,5): # --> carga de alumnos a la lista
	alumno = input(f'Ingrese el alumno {i + 1}: ')
	alumnos.append(alumno)
	
buscar_alumno = input('Ingrese el alumno a buscar: ')

if buscar_alumno in alumnos:
	print(f'El alumno {buscar_alumno} existe.')
else: 
	print(f'El alumno no existe.')
```


4. Registrar las ventas de 5 días. Al finalizar mostrar todas la ventas, calcular el total vendido.

```python
ventas = []
acumulador_dia = []
opcion = True
total = 0
contador = 1

while opcion:
	dato = float(input('Ingrese el importe de venta: $'))
	ventas.append(dato)
	print(f'Dato cargado...\n')
	
	aux = int(input('Cargar una nueva venta?\n1. Si\n2. No\n'))
	
	if aux == 2:
		opcion = False
		acumulador_dia.append(acumulador)
		break
	else: 
		acumulador += dato

for venta in acumulador_dia:
	print(f'Venta Nro. {contador}: ${venta:.2f}')
	total += venta

print(f'Total vendida: ${total}')

```

5. Una empresa desea registrar empleados. Solicitar nombres y edad de 3 empleados. Utilizar 2 listas, donde se deben guardar los datos en su lista correspondiente. al finalizar mostrar el siguiente formato, y la cantidad de empleados registrados.
```
Empleado 1: Juan - 25 años
Empleado 2: María - 31 años
Empleado 3: Pedro - 28 años
```

```python
empleados = []
edades = []
opcion = True
i = 0
while opcion:
	if opcion: 
		empleado = input('Ingrese nombre: ')
		edad = int(input('Ingrese edad: '))
		
	empleados.append(empleado)
	edades.append(edad)
	print('Datos cargados...')
	
	aux = int(input('Ingresar otro empleado?\n1. Si\n2. No\n'))
	
	if aux == 2:
		opcion = False
		break

for i in len(empleados):
	print(f'Empleado {i + 1}: {empleado[i + 1].capitalize()} - {edades[i + 1]}')
```

```python
ventas = []

acumulador_dia = []

opcion = True

total = 0

contador = 1

acumulador = 0

  

while opcion:

  dato = float(input('Ingrese el importe de venta: $'))

  ventas.append(dato)

  print(f'Dato cargado...\n')

  aux = int(input('Cargar una nueva venta?\n1. Si\n2. No\n'))

  if aux == 2:

    opcion = False

    acumulador_dia.append(acumulador)

    break

  else:

    acumulador += dato

  

for venta in ventas:

  print(f'Venta Nro. {contador}: ${venta:.2f}')

  contador += 1

  total += venta

  

print(f'Total vendida: ${total}')
```