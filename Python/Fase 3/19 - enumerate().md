## Ejercicio 1 — Ranking de ventas
Disponés de la siguiente lista:

```
ventas = [
    8500,
    12000,
    5400,
    9800,
    22000
]
```

Mostrá el listado así:

```
Venta N°1: $8500
Venta N°2: $12000
...
```

Utilizá `enumerate()`.

```python
ventas = [
    8500,
    12000,
    5400,
    9800,
    22000
]

def mostrar_lista(lista_ventas):
    for indice, venta in enumerate(ventas, start = 1):
        print(f'Venta N°{indice}: ${venta}')

mostrar_lista(ventas)
```
---
## Ejercicio 2 — Inventario

```
productos = [
    "Mouse",
    "Monitor",
    "Notebook",
    "Auriculares",
    "Teclado"
]
```

Mostrá un menú numerado comenzando desde 1.
Al final informá la cantidad total de productos.

```python
productos = [
    "Mouse",
    "Monitor",
    "Notebook",
    "Auriculares",
    "Teclado"
]

def mostrar_lista(lista_prod):
    for indice, producto in enumerate(productos, start = 1):
        print(f'{indice}. {producto}')
    print(f'Cantidad total de productos: {len(lista_prod)}')

mostrar_lista(productos)
```
---

## Ejercicio 3 — Registro de empleados

```
empleados = [
    {
        "nombre":"Ana",
        "sector":"Ventas"
    },
    {
        "nombre":"Juan",
        "sector":"RRHH"
    },
    {
        "nombre":"Pedro",
        "sector":"IT"
    },
    {
        "nombre":"María",
        "sector":"Compras"
    }
]
```

Mostrá un reporte como:

```
Empleado 1

Nombre: Ana

Sector: Ventas

--------------------
```

---

## Ejercicio 4 — Catálogo

Disponés de:

```
productos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Notebook"
]

precios = [
    18000,
    32000,
    210000,
    980000
]
```

Mostrá un catálogo numerado utilizando **`zip()` y `enumerate()` juntos**.

```python
productos = [
    "Mouse",
    "Teclado",
    "Monitor",
    "Notebook"
]

precios = [
    18000,
    32000,
    210000,
    980000
]

def mostrar_datos(list_prod, list_prec):
    deco = '-' * 25
    for indice, (producto, precio) in enumerate(zip(list_prod,list_prec), start = 1):
        print(f'Producto Nro. {indice}\n'
              f'- Nombre: {nombre}\n'
              f'- Precion: ${precio}\n'
              f'{deco}')

mostrar_datos(productos,precios)
```
---

## Ejercicio 5 — Sistema de alumnos

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

Mostrá un reporte numerado con:
- número de alumno
- nombre
- nota
- estado (Aprobado o Desaprobado)
Intentá resolverlo utilizando **`zip()` + `enumerate()`**.

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

def mostrar_datos(list_alumnos,list_notas,aux):
    for indice, (alumno,nota) in enumerate(zip(list_alumnos,list_notas), start = 1):
        if nota >= aux:
            print(f'Alumno {indice}\n'
                  f'- Nombre: {alumno}\n'
                  f'- Nota: {nota}\n'
                  f'- Estado: Aprobado')
        else:
            print(f'Alumno {indice}\n'
                  f'- Nombre: {alumno}\n'
                  f'- Nota: {nota}\n'
                  f'- Estado: Desaprobado')

mostrar_datos(alumnos,notas,NOTA_MINIMA)
```
---

# Desafío de razonamiento

Analizá el siguiente código **sin ejecutarlo**:

```
productos = [
    "Mouse",
    "Monitor",
    "Notebook"
]

for numero, producto in enumerate(productos, start=5):
    print(numero, producto)
```

Respondé:

1. ¿Qué pares genera `enumerate()`?
2. ¿Por qué el primer número es 5 y no 0?
3. ¿Qué imprimirá exactamente el programa?
4. ¿Qué diferencia hay entre usar `start=1` y sumar `+1` al índice dentro del `print()`?
5. Comparando `range(len(lista))` con `enumerate(lista)`, ¿cuál te parece más legible y por qué?