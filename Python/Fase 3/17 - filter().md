## Ejercicio 1 — Ventas relevantes
Una tienda registró los siguientes importes:

```
ventas = [1200, 8500, 43000, 950, 18000, 52000, 7600]
```

Generá una nueva colección que contenga únicamente las ventas iguales o superiores a **$10.000**.
Mostrá ambas colecciones.

```python
ventas = [1200, 8500, 43000, 950, 18000, 52000, 7600]

lista_ventas = list(
    filter(
        lambda x: x >= 10000, ventas
    )
)

print(lista_ventas)
```
---
## Ejercicio 2 — Control de stock
Disponés del siguiente inventario:

```
productos = [
    {"nombre": "Mouse", "stock": 12},
    {"nombre": "Monitor", "stock": 0},
    {"nombre": "Notebook", "stock": 5},
    {"nombre": "Auriculares", "stock": 0},
    {"nombre": "Teclado", "stock": 9}
]
```

Mostrá únicamente los productos que tienen stock disponible.
La salida debe conservar toda la información de cada producto.

```python
productos = [
    {"nombre": "Mouse", "stock": 12},
    {"nombre": "Monitor", "stock": 0},
    {"nombre": "Notebook", "stock": 5},
    {"nombre": "Auriculares", "stock": 0},
    {"nombre": "Teclado", "stock": 9}
]

lista_en_stock = list(
    filter(
        lambda producto: producto["stock"] > 0,productos
    )
)

print(lista_en_stock)
```
---
## Ejercicio 3 — Empleados habilitados
Una empresa registra:

```
empleados = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Juan", "activo": False},
    {"nombre": "María", "activo": True},
    {"nombre": "Pedro", "activo": True},
    {"nombre": "Lucas", "activo": False}
]
```

Obtené solamente los empleados habilitados para trabajar ese día.

```python
empleados = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Juan", "activo": False},
    {"nombre": "María", "activo": True},
    {"nombre": "Pedro", "activo": True},
    {"nombre": "Lucas", "activo": False}
]

hab_trab = list(
    filter(
        lambda empleado: empleado["activo"] == True, empleados
    )
)

print(hab_trab)
```
---
## Ejercicio 4 — Calificaciones
Se registraron las siguientes notas:

```
notas = [3, 10, 6, 5, 8, 4, 9, 7]
```

Construí una nueva colección que contenga únicamente las notas aprobadas.
Luego mostrala.

```python
NOTA_MINIMA = 6

notas = [3, 10, 6, 5, 8, 4, 9, 7]

aprobados = list(
    filter(
        lambda nota: nota >= NOTA_MINIMA, notas
    )
)

print(aprobados)
```

> Como no se establece una nota mínima, lo definí en una constantes.
---
## Ejercicio 5 — Clientes premium
Una empresa posee el siguiente registro:

```
clientes = [
    {"nombre": "Carlos", "compras": 15},
    {"nombre": "Laura", "compras": 3},
    {"nombre": "Ana", "compras": 22},
    {"nombre": "Pedro", "compras": 8},
    {"nombre": "María", "compras": 19}
]
```

La empresa considera **clientes premium** a quienes realizaron **10 o más compras**.
Generá una nueva colección con esos clientes y mostrá el resultado.

```python
clientes = [
    {"nombre": "Carlos", "compras": 15},
    {"nombre": "Laura", "compras": 3},
    {"nombre": "Ana", "compras": 22},
    {"nombre": "Pedro", "compras": 8},
    {"nombre": "María", "compras": 19}
]

clientes_premium = list(
    filter(
        lambda cliente: cliente["compras"] >= 10, clientes
    )
)

print(clientes_premium)
```
---
## Desafío de razonamiento
Sin ejecutar el código, analiza qué sucede.

```python
productos = [
    {"nombre": "Mouse", "stock": 12},
    {"nombre": "Monitor", "stock": 0},
    {"nombre": "Notebook", "stock": 4},
    {"nombre": "Auriculares", "stock": 0}
]

resultado = list(
    filter(
        lambda producto: producto["stock"] > 0,
        productos
    )
)

print(resultado)
```

Respondé:
1. ¿Qué función recibe `filter()` como primer argumento?
	Recibe una función lambda, la cual es `lambda producto:`
2. ¿Qué condición evalúa esa función?
	La condición que evalúa es `producto["stock"] > 0`
3. ¿Qué elementos conservará la nueva colección?
	Los elementos donde el valor de stock sea mayor a 0
4. ¿Cuántos elementos tendrá `resultado`?
	Tendrá 2 elementos:
	- Mouse -> 12
	- Notebook -> 4
5. ¿Cuál es la diferencia fundamental entre este ejemplo y uno equivalente usando `map()`?
	Que `map()` transforma cada elemento de una colección y `filter()` nos devuelve los valores con los cuales nos queremos quedar, es decir, los filtra.