1. Hacer un programa que imprima los números del 1 al 10.

```python
for numero in range(1,11):
	print(numero)
```

2. Hacer un programa que imprima los números del 10 al 1.

```python
for numero in range(10,0,-1):
	print(numero)
```

3. Solicite una palabra al usuario y muestre cada letra en una lineá distinta.

```python
txt_user = input('Ingrese una palabra'):

for letra in txt_user:
	print(letra)
```

4. Realizar un programa que solicite 5 números, los sume usando `for` y muestre el total.

```python
num_user = 0
suma = 0

for i in range(1,6):
	num_user = int(input(f'Ingrese el numero {i}: '))
	suma += num_user

print(f'La suma total es: {suma}')
```

5. Realizar un programa que muestre la tabla de multiplicar del 7.

```python
NUM_TABLA = 7
operacion = 0
for numero in range(1,11):
	operacion = NUM_TABLA * numero
	print(f'{NUM_TABLA} x {numero} = {operacion}')
```

6. Una tienda tiene los siguientes productos: 
	- `productos = ['Mouse', 'Teclado','Monitor']`
	- `precios = [15000, 30000, 120000]`
	Mostrar:
	`1. Mouse - $15000`
	`2. Teclado - $30000`
	`3. Monitor - $120000`
	Luego solicitar al usuario `Que producto desea actualizar ?`.
	El usuario ingresara `1`,`2` o `3`.
	Después pedir el nuevo precio.
	Finalmente mostrar la lista actualizada.

```python
productos = ['Mouse', 'Teclado', 'Monitor']
precios = [15000, 30000, 120000]
opcion = 0

for i in range(0,3):
	print(f'{i}. {productos[i]} - ${precios[i]}')

opcion = int(input('Que producto desea actualizar ?'))

if opcion == 1:
	aux = float(input('Ingrese el nuevo precio: $'))
	precios[0] = aux
elif opcion == 2:
	aux = float(input('Ingrese el nuevo precio: $'))
	precios[1] = aux
elif opcion == 3:
	aux = float(input('Ingrese el nuevo precio: $'))
	precios[2] = aux
else:
	print('Opcion incorrecta...')
	
print('Lista actualizada')
for i in range(0,3):
	print(f'{i}. {productos[i]} - ${precios[i]}')
```

7. Registrar 5 alumnos en una lista, luego mostrar algo similar a:
	1. Juan
	2. Pedro
	3. María
	4. Ana
	5. Lucas
	Después solicitar un numero -->`ingrese el numero del alumno`. 
	Si el numero es valida, mostrar --> `Alumno seleccionado: Maria`

```python
alumnos = []

for i in range(1,6): # --> cargar lista
	alumno = input(f'Ingrese el alumno {i}: ').capitalize()
	alumnos.append(alumno)

for x in range(int(len(alumnos))):
	print(f'{x}. {alumnos[x]}')

num_alum = int(input(f'\nIngrese el numero del alumno: '))

if num_alum in alumnos:
	print(f'Alumno seleccionado: {alumnos[num_alum]}')
else:
	print('Alumno no encontrado!')
```

8. Una empresa necesita registrar exactamente 3 empleados.
	Guardar:
	- `nombres = []`
	- `edades = []`
	Solicitar:
	- Nombre
	- Edad
	para cada empleado.
	Al finalizar mostrar:
	Empleado 1: Juan - 25 años
	Empleado 2: María - 31 años
	Empleado 3: Pedro - 28 años
	Y además indicar --> `Empleado con mas caracteres en su nombre: Maria`