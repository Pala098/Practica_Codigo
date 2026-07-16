## Ejercicio #1 - Ajuste de precios
Una tienda tiene la siguiente lista:

```
precios = [1200, 4500, 1800, 7600, 950]
```

Genera una nueva colección con los precios luego de aplicar un aumento del **12%**.
Muestra ambas listas.

```python
precios = [1200, 4500, 1800, 7600, 950]  
  
precios_12 = [precio + (precio * 0.12) for precio in precios]  
  
print(precios)  
print(precios_12)
```

---
## Ejercicio #2 - Control de acceso
Se registraron las edades de las personas que asistieron a un evento.

```
edades = [15, 22, 18, 34, 12, 27, 17, 40]
```

Obtén únicamente las edades correspondientes a personas mayores de edad.
Muestra el resultado.

```python
edades = [15, 22, 18, 34, 12, 27, 17, 40]  
  
mayores = [edad for edad in edades if edad >= 18]  
  
print(f'Mayores: {mayores}')
```

---
## Ejercicio #3 - Inventario
Dispones de la siguiente lista de productos:

```
productos = [
    {"nombre": "Mouse", "stock": 15},
    {"nombre": "Monitor", "stock": 0},
    {"nombre": "Teclado", "stock": 8},
    {"nombre": "Notebook", "stock": 3},
    {"nombre": "Auriculares", "stock": 0}
]
```

Obtén una nueva colección que contenga únicamente los nombres de los productos que tienen stock disponible.

```python
productos = [  
    {"nombre": "Mouse", "stock": 15},  
    {"nombre": "Monitor", "stock": 0},  
    {"nombre": "Teclado", "stock": 8},  
    {"nombre": "Notebook", "stock": 3},  
    {"nombre": "Auriculares", "stock": 0}  
]  
  
prod_en_stock = [producto['nombre'] for producto in productos if producto['stock'] > 0]  
print(prod_en_stock)
```

---
## Ejercicio #4 - Sistema de calificaciones
Se registraron las siguientes notas:

```
notas = [4, 8, 10, 6, 3, 9, 7, 5]
```

Genera una nueva lista que contenga solamente las notas aprobadas (considera aprobadas las mayores o iguales a 6).
Luego muestra ambas listas.

```python
notas = [4, 8, 10, 6, 3, 9, 7, 5]  
  
aprobados = [nota for nota in notas if nota >= 6]  
  
print(f'{notas}\n{aprobados}')
```

---
## Ejercicio #5 - Nómina de empleados
La empresa almacena la siguiente información:

```
empleados = [
    {"nombre": "Ana", "salario": 850000},
    {"nombre": "Juan", "salario": 1250000},
    {"nombre": "María", "salario": 980000},
    {"nombre": "Pedro", "salario": 1500000}
]
```

Obtén una nueva colección que contenga únicamente los nombres de los empleados cuyo salario sea superior a **$1.000.000**.
Muestra el resultado.

```python
TOPE = 1000000  
  
empleados = [  
    {"nombre": "Ana", "salario": 850000},  
    {"nombre": "Juan", "salario": 1250000},  
    {"nombre": "María", "salario": 980000},  
    {"nombre": "Pedro", "salario": 1500000}  
]  
  
empleados_sup_1m = [empleado['nombre'] for empleado in empleados if empleado['salario'] > TOPE]  
print(empleados_sup_1m)
```

---
## Desafío de razonamiento
Sin ejecutar el código, analiza el siguiente programa:

```python
numeros = [2, 4, 6, 8, 10]

resultado = [n * 3 for n in numeros if n >= 6]

print(resultado)
```

Responde:
1. ¿Qué elementos recorre la comprensión de listas?
	Recorre los elementos dentro de la lista `numeros`.
2. ¿Qué condición deben cumplir para formar parte de la nueva lista?
	La condición es: `if n >= 6`
3. ¿Qué operación se realiza sobre cada elemento que cumple la condición?
	Se realiza una multiplicación por 3.
4. ¿Qué imprime el `print()`?
	`print()` imprime la nueva lista generada a partir de la lista números, dentro de la comprensión de lista.
5. ¿Qué ventaja ofrece este enfoque respecto de utilizar un `for` tradicional con `append()`?
	La ventaja que presenta es que hace mas rápido algunas acciones, en comparación a la forma tradicional como son:
	- recorrer la lista
	- convertir o operar cada elemento
	- guardar los valores en otra lista
	> *Las comprensiones de listas permiten crear una nueva lista en una sola expresión, haciendo el código más corto, más legible y generalmente más "pythonico". Además, suelen ser ligeramente más eficientes que construir la lista manualmente utilizando `append()`.*