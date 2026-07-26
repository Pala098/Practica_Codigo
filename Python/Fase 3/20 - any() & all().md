## Ejercicio 1 — Control de inventario
Una tienda registra el siguiente inventario:

```
productos = [
    {"nombre": "Mouse", "stock": 15},
    {"nombre": "Monitor", "stock": 8},
    {"nombre": "Notebook", "stock": 0},
    {"nombre": "Auriculares", "stock": 5}
]
```

Mostrar un único mensaje indicando si **existe al menos un producto sin stock**.

```python
productos = [
    {"nombre": "Mouse", "stock": 15},
    {"nombre": "Monitor", "stock": 8},
    {"nombre": "Notebook", "stock": 0},
    {"nombre": "Auriculares", "stock": 5}
]

def sin_stock(list_prod):
    hay_stock = any(producto["stock"] > 0 for producto in list_prod)
    print(hay_stock)

sin_stock(productos)
```

> [!bug|borde] Corrección
> La consigna era:
> 
> > Mostrar si **existe al menos un producto sin stock**.
> 
> Tu código:
> ```python
> hay_stock = any(producto["stock"] > 0 for producto in list_prod)
> ```
> ¿Qué está preguntando realmente?
> 
> > ¿Existe algún producto con stock?
>
> Y la respuesta es:
> ```
> True
> ```
> porque Mouse ya tiene stock.
> Pero la pregunta era otra.
> Debería ser:
> ```python
> resultado = any(
>     producto["stock"] == 0
> 	for producto in list_prod
> )
> ```
> o también
> ```python
> resultado = any(
> 	producto["stock"] <= 0
> 	for producto in list_prod
> )
> ```
> Fijate que ahora la condición coincide exactamente con la pregunta.

---
## Ejercicio 2 — Estado del curso
Se registraron las siguientes notas:

```
notas = [8, 7, 10, 6, 9]
```

Mostrar un mensaje indicando si **todos los alumnos aprobaron**.

```python
NOTA_MINIMA = 6

notas = [8, 7, 10, 6, 9]

def todos_aprobados(list_notas,aux):
    resultado = all(nota > aux for nota in list_notas)
    print(resultado)

todos_aprobados(notas,NOTA_MINIMA)
```

> [!bug|borde] Corrección
> Muy cerca.
> Escribiste:
> ```
> all(nota > aux ...)
> ```
> La nota mínima vale:
> ```
> 6
> ```
> Una nota de **6 aprueba**.
> Entonces:
> ```
> 6 > 6
> ```
> es
> ```
> False
> ```
> Debería ser:
> ```python
> all(
>     nota >= aux
> 	for nota in list_notas
> )
> ```
> Este error aparece muchísimo en programación.

---
## Ejercicio 3 — Control de acceso

Una empresa registra los siguientes empleados:

```
empleados = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Juan", "activo": True},
    {"nombre": "Pedro", "activo": False},
    {"nombre": "María", "activo": True}
]
```

Mostrar un mensaje indicando si **existe al menos un empleado inactivo**.

```python
empleados = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Juan", "activo": True},
    {"nombre": "Pedro", "activo": False},
    {"nombre": "María", "activo": True}
]

def empleados_inactivos(list_empl):
    resultado = any(empleado["activo"] for empleado in list_empl)
    print(resultado)

empleados_inactivos(empleados
```

> [!bug|borde] Correccion
> La consigna era:
> 
> > ¿Existe al menos un empleado inactivo?
> 
> Vos escribiste:
> ```python
> any(
>     empleado["activo"]
> )
> ```
> Eso pregunta:
> ¿Existe algún empleado activo?
> Y devuelve:
> ```
> True
> ```
> porque Ana ya lo es.
> La condición correcta sería cualquiera de estas:
> ```python
> any(
>     empleado["activo"] == False
> 	for empleado in list_empl
> )
> ```
> o, más pythonico:
> ```python
> any(
> 	not empleado["activo"]
> 	for empleado in list_empl
> )
> ```
> Esta segunda forma la vas a encontrar muchísimo.
> Además, te quedó un pequeño error de sintaxis:
> ```
> empleados_inactivos(empleados
> ```
> faltó cerrar el paréntesis.

---
## Ejercicio 4 — Verificación de salarios

```
SALARIO_MINIMO = 900000

empleados = [
    {"nombre": "Ana", "salario": 950000},
    {"nombre": "Juan", "salario": 1200000},
    {"nombre": "Pedro", "salario": 980000},
    {"nombre": "María", "salario": 870000}
]
```

Informar si **todos los empleados cobran al menos el salario mínimo definido**.

```python
SALARIO_MINIMO = 900000

empleados = [
    {"nombre": "Ana", "salario": 950000},
    {"nombre": "Juan", "salario": 1200000},
    {"nombre": "Pedro", "salario": 980000},
    {"nombre": "María", "salario": 870000}
]

def salario_min(list_empl,sal_min):
    resultado = all(empleado["salario"] >= sal_min for empleado in list_empl)
    print(resultado)

salario_min(empleados,SALARIO_MINIMO)
```
---
## Ejercicio 5 — Validación de pedidos

```
pedidos = [
    {"cliente": "Carlos", "pagado": True},
    {"cliente": "Laura", "pagado": True},
    {"cliente": "Ana", "pagado": False},
    {"cliente": "Pedro", "pagado": True}
]
```

Indicar si **hay algún pedido pendiente de pago**.

```python
pedidos = [
    {"cliente": "Carlos", "pagado": True},
    {"cliente": "Laura", "pagado": True},
    {"cliente": "Ana", "pagado": False},
    {"cliente": "Pedro", "pagado": True}
]

def pendien_pago(list_pedi):
    resultado = any(not(pedido["pagado"]) for pedido in list_pedi)
    print(resultado)

pendien_pago(pedidos)
```
---

# Desafío de razonamiento

Analizar el siguiente código sin ejecutarlo:

```python
ventas = [1200, 8500, 4300, 15000]

resultado = all(
    venta > 1000
    for venta in ventas
)

print(resultado)
```

Responder:
1. ¿Qué condición evalúa `all()`?
	`all()` evalúa `venta > 1000`.
2. ¿Qué resultado obtiene para cada venta?
	Obtendrá un valor booleano como resultado para cada venta.
3. ¿Qué valor tendrá `resultado`?
	El valor que tendrá es `True`.
4. ¿Qué cambiaría si reemplazáramos `all()` por `any()`?
	El tipo de evaluación que hacemos, si utilizamos `any()` estaríamos preguntando si almeno uno de los elementos cumple con la condición, en cambio `all()` evalúa si todos cumplen, si uno no lo hace ya no cumple con esta condición.
5. ¿En qué situación real sería más apropiado usar `all()` y en cuál `any()`?
	`all()` lo usaría para obtener un resultado rápido de si todos los valores cumplen con una condición, por ejemplo, si todos los alumnos están aprobados o si todos los empleados reciben un cierto salario. En cambio `any()` lo usaría para evaluar si al menos uno de los datos cumple con cierto criterio, por ejemplo, si algún empleado esta inactivo o si recibe un monto especifico.