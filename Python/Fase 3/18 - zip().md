## Ejercicio 1 — Recibo de sueldo
Tenés dos listas:
```
empleados = ["Ana", "Juan", "Pedro", "María"]

sueldos = [850000, 1200000, 980000, 1500000]
```
Mostrá un recibo para cada empleado con el formato:
```
Empleado: Ana
Sueldo: $850000

--------------------
```

```python
deco = '-' * 25

empleados = ["Ana", "Juan", "Pedro", "María"]

sueldos = [850000, 1200000, 980000, 1500000]

def mostrar_recibo(list_empleados,list_sueldos,aux):
    for nombre, sueldo in zip(list_empleados,list_sueldos):
        print(f'Empleado: {nombre}\n'
              f'Sueldo: ${sueldo}\n'
              f'{aux}')

mostrar_recibo(empleados,sueldos,deco
```
---
## Ejercicio 2 — Catálogo de productos
Disponés de:
```
productos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Notebook",
    "Auriculares"
]

precios = [
    18000,
    32000,
    210000,
    980000,
    45000
]
```
Mostrá un catálogo numerado con nombre y precio de cada producto.

```python
deco = '-' * 25

productos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Notebook",
    "Auriculares"
]

precios = [
    18000,
    32000,
    210000,
    980000,
    45000
]

def mostrar_catalogo(list_prod, list_precios, aux):
    contador = 0
    for producto,precio in zip(list_prod,list_precios):
        contador += 1
        print(f'Producto Nro. {contador}\n'
              f'- Nombre: {producto}\n'
              f'- Precio: ${precio}\n'
              f'{aux}')

mostrar_catalogo(productos,precios,deco)
```
---
## Ejercicio 3 — Registro de asistencia
Disponés de:

```
empleados = [
    "Ana",
    "Juan",
    "María",
    "Pedro",
    "Lucas"
]

asistencia = [
    True,
    False,
    True,
    True,
    False
]
```

Mostrá únicamente los empleados que asistieron.

```python
empleados = [
    "Ana",
    "Juan",
    "María",
    "Pedro",
    "Lucas"
]

asistencia = [
    True,
    False,
    True,
    True,
    False
]

def crear_lista(list_emple,list_asis):
    for nombre,asistio in zip(list_emple,list_asis):
       if asistio:
           print(f'{nombre} --> asistio: {asistio}')

crear_lista(empleados,asistencia)
```
---
## Ejercicio 4 — Sistema de calificaciones
Disponés de:

```
alumnos = [
    "Lucas",
    "María",
    "Pedro",
    "Ana",
    "Sofía"
]

notas = [
    8,
    4,
    10,
    6,
    5
]
```
Mostrá un reporte donde aparezcan solamente los alumnos aprobados.

```python
NOTA_MINIMA = 6

alumnos = [
    "Lucas",
    "María",
    "Pedro",
    "Ana",
    "Sofía"
]

notas = [
    8,
    4,
    10,
    6,
    5
]

def mostrar_aprobados(list_alum,list_nota,aux):
    print('ALUMNOS APROBADOS')
    for alumno,nota in zip(list_alum,list_nota):
        if nota >= aux:
            print(f'{alumno.capitalize()} - nota: {nota}')

mostrar_aprobados(alumnos,notas,NOTA_MINIMA)

```
---
## Ejercicio 5 — Inventario
Dispones de:

```
productos = [
    "Mouse",
    "Monitor",
    "Notebook",
    "Auriculares",
    "Teclado"
]

stock = [
    15,
    0,
    3,
    18,
    0
]
```

Mostrá únicamente los productos que todavía tienen stock disponible.

```python
productos = [
    "Mouse",
    "Monitor",
    "Notebook",
    "Auriculares",
    "Teclado"
]

stock = [
    15,
    0,
    3,
    18,
    0
]

deco = '-' * 25

def mostrar_prod_stock(list_prod,list_stock,aux):
    for producto,unidad in zip(list_prod,list_stock):
        if unidad > 0:
            print(f'Producto: {producto}\n'
                  f'Stock: {unidad}\n'
                  f'{aux}')

mostrar_prod_stock(productos,stock,deco)
```
---

# Desafío de razonamiento
Analiza el siguiente código **sin ejecutarlo**:

```python
clientes = ["Ana", "Juan", "Pedro"]
compras = [5, 12, 8]

for cliente, cantidad in zip(clientes, compras):
    if cantidad >= 10:
        print(cliente)
```

Responde:
1. ¿Qué pares de datos genera `zip()`?
	Los pares de datos que genera `zip()` son: (Ana,5) (Juan,12) (Pedro,8)
2. ¿Qué condición se evalúa?
	Se evalúa la condición `cantidad >= 10`, es decir, que el valor de compra sea mayor o igual a 10.
3. ¿Qué cliente o clientes imprime el programa?
	Imprime solamente a `Juan,12`.
4. ¿Qué ocurriría si `compras` fuera `[5, 12]`?
	Simplemente se asignara el valor al la posición de la lista mas corta, es decir solo se asignara a ana y juan, mientras que pedro simplemente se ignorara.
5. ¿Qué ventaja tiene `zip()` frente a recorrer ambas listas usando índices (`range(len(...))`)?
	Que ase asignan valores de forma mas limpia sin tanto código, y solo dependemos de la posición no de un indice.