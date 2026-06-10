## 1. Datos personales
Crear un tupla con:
- nombre
- edad
- ciudad
Luego mostrar cada dato utilizando índices.
Ejemplo:
```
tupla = (dato1, dato2, dato3)
```

```python
datos = ('Diana', 5, 'La Plata')

for dato in datos:
	print(dato)
```

## 2 . Días de la semana
Crear una tupla con los siete días.
Mostrar:
- primer día
- ultimo día
- cantidad de días
Utilizando:
`[]`
`len()`

```python
dias_semana = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo')

for i in range(len(dias_semana)):
	if i == 0:
		print(f'Primer dia: {dias_semana[i]}')
		
	if i == len(dias_semana) - 1:
		print(f'Ultima dia: {dias_semana[i]}')
print(f'Cantidad de dias: {len(dias_semana)}')
```

## 3. Desempaquetado
Crear una tupla:
`producto = ('Mouse', 15000,25)`
donde:
- nombre
- precio
- stock
Utilizar desempaquetado para guardar cada valor en una variable independiente.
Luego mostrarlo

```python
producto = ('Mouse', 15000, 25)

nombre_prod, precio, stock = producto

print(f'Producto: {nombre_prod}\nPrecio: ${precio}\nStock: {stock}')
```

## 4. Conversión
Crear una lista:
```python
numeros = [10, 20, 30, 40, 50]
```
Convertirla a tupla.
Mostrar:
- la tupla completa
- cantidad de elementos

```python
numeros = [10, 20, 30, 40, 50]

tupla_num = tuple(numeros)

for x in tupla_num:
	print(x)

print(f'Cantidad de elementos: {len(tupla_num)}')
```

## 5. Integrador
Una empresa tiene registrados los siguientes empleados:
```python
empleados = (
    ("Juan", 25),
    ("María", 31),
    ("Pedro", 28)
)
```
Recorrer la estructura y mostrar
```
Empleado: Juan - Edad: 25
Empleado: María - Edad: 31
Empleado: Pedro - Edad: 29
```

```python
empleados = (
    ("Juan", 25),
    ("María", 31),
    ("Pedro", 28)
)

for i in range(len(empleados)):
	nombre, edad = empleados[i]
	print(f'Empleado: {nombre} - Edad: {edad}')
```

## Desafío razonamiento
Sin ejecutar: 
```python
datos = ("Python", "SQL", "Power BI")

print(datos[1])

datos[1] = "Excel"

print(datos)
```
Preguntas:
1. ¿Qué imprime la primera línea?
	La primer lineá 'print(datos[1])' imprimirá SQL.
2. ¿Qué ocurre en la segunda asignación?
	Se intenta cambiar un valor de un elemento, pero esto no se puede dentro de las tuplas.
3. ¿Por qué sucede?
	Porque las tuplas son inmutables, es decir los elementos que estas almacenan no pueden ser modificados.