## 1. Estadística de ventas
Crear una lista con 5 importes ingresados por el usuario.
Al finalizar mostrar:
- total vendido
- venta mas alta
- venta mas baja
- cantidad de ventas
Utilizar funciones integradas.

```python
importes = []
decorador = '-' * 15

for i in range(0,5):
	importe = float(input(f'Ingrese el importe Nro. {i + 1}: '))
	
	importes.append(importe)
	
	print(f'Importe cargado...')

# total vendido
print(f'Total vendido: ${sum(importes):.2f}')
print(decorador)
print(f'Venta mas alta: ${max(importes)}')
print(decorador)
print(f'Venta mas baja: ${min(importes)}')
print(decorador)
print(f'Cantidad de ventas: {len(importes)}')
```

## 2. Ranking de alumnos
Solicitar 5 nombres de alumnos, guardar en una lista y mostrar los nombres ordenados alfabéticamente.
Luego numerarlos, y mostrar: 
```
1. Ana
2. Juan
3. María
...
```

```python
nombres = []
decorador = '-' * 15

for i in range(0,5):
	nombre = input(f'Ingrese el nombre del alumno Nro. {i + 1}: ')
	nombres.append(nombre)
	print(decorador)
	print('Alumno cargado...')
	print(decorador)
print('Listado de alumnos: ')

for alumno in sorted(nombres):
	print(f'- {alumno}')
# for posicion, alumno in enumerate(sorted(nombres), start=1): --> ✔
#   print(f'{posicion}. {alumno}')
```

## 3. Inventario
Registrar 4 productos, guardar sus precios en una lista.
Mostrar:
- lista original
- lista ordenada ascendente
- lista ordenada descendente
- precio mas alto
- precio mas bajo

```python
productos = []
deco = '-' * 25

for i in range(0,4):
	producto = float(input(f'Ingrese el precio del producto {i + 1}: $'))
	productos.append(producto)
	print(deco)
	print('Producto cargado...')
	print(deco)

print('Lista original')
for producto in productos:
	print(f'- {producto}')

print(deco)

print('Lista ordenada ascendente')
for producto in sorted(productos):
	print(f'- {producto}')

print(deco)

print('Lista ordenada descendente')
for producto in sorted(productos, reverse = True):
	print(f'- {producto}')

print(deco)

print(f'Precio mas alto: ${max(productos)}')

print(deco)

print(f'Precio mas bajo: ${min(productos)}')
```

## 4. Análisis de edades
Solicitar edades de 5 personas.
Mostrar: 
- promedio de edad
- edad máxima
- edad mínima

```python
edades = []

deco = '-' * 25

for i in range(0,5):
	print(f'Persona {i + 1}')
	edad = int(input('Ingrese su edad: '))
	edades.append(edad)
	print(deco)
	print('Edad cargada...')
	print(deco)

promedio_edad = sum(edades) / len(edades)
print(f'Promedio de edad: {promedio_edad:.0f}')
print(deco)
print(f'Edad maxima: {max(edades)}')
print(deco)
print(f'edad minima: {min(edades)}')
```

## 5. Integrador
Registrar 3 empleados utilizando diccionarios.
Cada empleado debe tener:
- nombre
- edad
- salario
Guardar todos los empleados en una lista, al finalizar mostrar:
1. Todos los empleados numerados 
2. El salario mas alto registrado
3. El salario mas bajo registrado
4. Promedio salarial

```python
empleados = []
deco = '-' * 25
sal_alto = -9999
sal_bajo = 9999
suma = 0

for i in range(0,3):
  empleado = {}

  print(f'Empleado N°{i+1}')
  print(deco)
  nombre = input('Ingrese su nombre: ')
  edad = int(input('Ingrese su edad: '))
  salario = float(input('Ingrese su salario: $ '))

  empleado['nombre'] = nombre
  empleado['edad'] = edad
  empleado['salario'] = salario

  empleados.append(empleado)

  print('Datos cargados...')

  print(deco)

for i, persona in enumerate(empleados):
  print(f'Datos empleado N°{i+1}')
  print(deco)
  print(f'- Nombre: {persona['nombre']}') # posible error por las comillas --> print(f"- Nombre: {persona['nombre']}") ✔
  print(f'- Edad: {persona['edad']}')
  print(f'- Salario: ${persona['salario']}')
  print(deco)

  if persona['salario'] > sal_alto:
    sal_alto = persona['salario']

  if persona['salario'] < sal_bajo:
    sal_bajo = persona['salario']
    
  suma += persona['salario']

promedio_sal = suma / len(empleados)

print(f'Promedio de salarios: ${promedio_sal:.2f}')
print(deco)
print(f'Salario mas alto: ${sal_alto}')
print(f'Salario mas bajo: ${sal_bajo}')
```

## Ejercicio razonamiento
Sin ejecutar:
```python
numeros = [50, 20, 80, 10]

print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(sorted(numeros))
```
Preguntas:
1. ¿Qué imprime cada línea?

> - sum(numeros) --> imprime la sumatoria de los valores numéricos de la lista
> - max(numeros) --> imprime el valor mas alto
> - min(numeros) --> imprime el valor mas bajo
> - sorted(numeros) --> imprime la lista pero ordenada de manera descendente

2. ¿Cuál de las funciones devuelve una nueva lista ordenada?

> sorted()

3. ¿Cuál devuelve un único valor?

> Son dos las funciones que devuelven un valor único: max() y min().

4. ¿Qué diferencia hay entre `len()` y `sum()`?

> len() devuelve la dimensión, o largo, de una lista (cuanto elementos tiene), y sum() realiza la operación de suma entre los valores numéricos que contenga la lista.