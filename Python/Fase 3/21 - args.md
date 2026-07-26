## Ejercicio 1 — Caja del supermercado
Una caja registradora debe calcular el importe total de una compra.
La función debe poder recibir cualquier cantidad de importes.
Ejemplo de uso:

```
calcular_total(1200, 3500, 800, 250)
```

Debe devolver el total de la compra.

```python
def calcular_total(*compras):
    total = 0

    for compra in compras:
        total += compra
    return total

total_compras = calcular_total(1200, 3500, 800, 250)

print(total_compras)

```
---
## Ejercicio 2 — Asistencia a una capacitación
Crear una función que reciba el nombre del instructor y luego cualquier cantidad de nombres de asistentes.
La salida podría verse así:

```
Instructor: Carlos

Asistentes:

Ana
Pedro
María
Lucas
```

---

## Ejercicio 3 — Sistema de ventas
Crear una función que reciba el nombre del cliente y una cantidad variable de importes de compras.
Debe mostrar:
- cliente
- cantidad de compras
- total gastado
- promedio por compra
---
## Ejercicio 4 — Control de stock
Crear una función que reciba una cantidad variable de productos representados por diccionarios como:

```
{
    "nombre": "...",
    "stock": ...
}
```

La función debe indicar:
- cantidad de productos recibidos
- cuántos tienen stock
- cuántos están sin stock
---
## Ejercicio 5 — Evaluación de empleados
Cada empleado estará representado por un diccionario:

```
{
    "nombre": "...",
    "salario": ...
}
```

La función debe recibir una cantidad variable de empleados y devolver:
- salario total
- salario promedio
- nombre del empleado con mayor salario
No utilices funciones como `max()` todavía; resolvelo recorriendo los datos.

---
# Desafío de razonamiento
Analizá el siguiente código sin ejecutarlo:

```
def mostrar(*datos):
    print(datos)

mostrar(10, 20)
mostrar("Ana")
mostrar()
```

Respondé:
1. ¿Qué contiene `datos` en la primera llamada?
2. ¿Qué contiene en la segunda?
3. ¿Qué contiene en la tercera?
4. ¿Por qué `datos` siempre es una tupla, incluso cuando no recibe argumentos?
5. ¿Qué ventaja aporta `*args` frente a definir una función con cinco parámetros fijos?