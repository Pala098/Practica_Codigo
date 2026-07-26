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
<<<<<<< HEAD
=======

> [!bug|borde] Correccion
> Solo una pequeña observación de estilo:
> La función recibe un parámetro:
> ```python
> def mostrar_lista(lista_ventas):
> ```
> pero luego recorres la variable global:
> ```python
> for indice, venta in enumerate(ventas, start=1)
> ```
> Sería mejor usar el parámetro
> ```python
> for indice, venta in enumerate(lista_ventas, start=1):
> ```
> Así la función puede reutilizarse con cualquier lista.

>>>>>>> 0bf49f4 (act-practica-python)
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
<<<<<<< HEAD
=======

> [!bug|borde] Correccion
> Exactamente el mismo detalle.
> En vez de:
> ```
> enumerate(productos)
> ```
> debería ser
> ```python
> enumerate(lista_prod)
> ```

>>>>>>> 0bf49f4 (act-practica-python)
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

<<<<<<< HEAD
=======
```python
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

for numero, empleado in enumerate(empleados, start=1):
    print(f"Empleado {numero}")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Sector: {empleado['sector']}")

    print("-" * 20)
```
>>>>>>> 0bf49f4 (act-practica-python)
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
<<<<<<< HEAD
=======

> [!bug|borde] Corrección
> Aquí apareció un pequeño error.
> Escribiste:
> ```python
> for indice, (producto, precio) in enumerate(zip(list_prod,list_prec), start=1):
> ```
> Eso está perfecto.
> Pero luego imprimís:
> ```python
> print(f"- Nombre: {nombre}")
> ```
> La variable `nombre` no existe.
> Debe ser:
> ```python
> print(f"- Nombre: {producto}")
> ```
> Es un pequeño error de variable, muy común.

>>>>>>> 0bf49f4 (act-practica-python)
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
<<<<<<< HEAD
2. ¿Por qué el primer número es 5 y no 0?
3. ¿Qué imprimirá exactamente el programa?
4. ¿Qué diferencia hay entre usar `start=1` y sumar `+1` al índice dentro del `print()`?
5. Comparando `range(len(lista))` con `enumerate(lista)`, ¿cuál te parece más legible y por qué?
=======
	Los pares que genera son:
	- 5 - Mouse
	- 6 - Monitor
	- 7 - Notebook
2. ¿Por qué el primer número es 5 y no 0?
	Porque se lo esta definiendo en `start = 5`, que es donde podemos definir desde que numero enumera `enumerate()`
3. ¿Qué imprimirá exactamente el programa?
	El programa imprimirá:
	```
	5 Mouse
	6 Monitor
	7 Notebook
	```
4. ¿Qué diferencia hay entre usar `start=1` y sumar `+1` al índice dentro del `print()`?
	Que `start = 1` es un parámetro que le indicamos a `enumerate()` para saber la posición de un elemento.

> [!bug|borde] Corrección
> Aquí haría una pequeña corrección conceptual.
> Dijiste:
> > `start=1` es un parámetro que le indicamos a enumerate() para saber la posición de un elemento.
>
> Eso es cierto, pero la diferencia con sumar `+1` es otra.
> La respuesta completa sería:
> Con
> ```python
> enumerate(lista, start=1)
> ```
> el índice **ya nace** en 1.
> En cambio
> ```python
> for indice, dato in enumerate(lista):
>     print(indice + 1)
> ```
> `enumerate()` sigue generando:
> ```
> 0
> 1
> 2
> 3
> ```
> y simplemente nosotros mostramos:
> ```
> 1
> 2
> 3
> 4
> ```
> Es decir:
> - `start` modifica el valor generado por `enumerate()`.
> - `+1` solamente modifica lo que mostramos o usamos.
>  
> Parece un detalle pequeño, pero conceptualmente son cosas distintas.

5. Comparando `range(len(lista))` con `enumerate(lista)`, ¿cuál te parece más legible y por qué?
	`enumerate(lista)`, porque su sintaxis es mas chica a comparación de `range` y ademas nos permite darle un valor al indice, de ser necesario modificar este también, sin tantas lineas de código.
>>>>>>> 0bf49f4 (act-practica-python)
