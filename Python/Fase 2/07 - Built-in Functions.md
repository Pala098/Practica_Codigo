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
```

## 3. Inventario
Registrar 4 productos, guardar sus precios en una lista.
Mostrar:
- lista original
- lista ordenada ascendente
- lista ordenada descendente
- precio mas alto
- precio mas bajo
## 4. Análisis de edades
Solicitar edades de 5 personas.
Mostrar: 
- promedio de edad
- edad máxima
- edad mínima
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
2. ¿Cuál de las funciones devuelve una nueva lista ordenada?
3. ¿Cuál devuelve un único valor?
4. ¿Qué diferencia hay entre `len()` y `sum()`?