## Ejercicio #1
Una tienda necesita actualizar todos sus precios aplicando un aumento del **15%**.

```
precios = [1200, 4500, 9800, 15000, 3200]
```

Generá una nueva colección con los precios actualizados.

```python
precios = [1200, 4500, 9800, 15000, 3200]  
  
precios_act = list(map(lambda x: x + (x * 0.15), precios))  
  
print(precios_act)
```
---
## Ejercicio 2 — Normalización de nombres

Se recibió una lista de clientes escrita de manera inconsistente.

```
clientes = [
    "juan perez",
    "MARIA LOPEZ",
    "anA Garcia",
    "pedro gomez"
]
```

Generá una nueva colección donde todos los nombres tengan un formato uniforme (por ejemplo, utilizando `title()`).

```python
clientes = [  
    "juan perez",  
    "MARIA LOPEZ",  
    "anA Garcia",  
    "pedro gomez"  
]  
  
lista_mod = list(map(str.title, clientes))  
  
print(lista_mod)
```
---

## Ejercicio 3 — Conversión de datos

Un archivo CSV fue leído y todos los valores quedaron como texto.

```
cantidades = [
    "12",
    "5",
    "18",
    "30",
    "7"
]
```

Convertí todos los elementos al tipo de dato adecuado para poder realizar cálculos matemáticos.

```python
cantidades = [  
    "12",  
    "5",  
    "18",  
    "30",  
    "7"  
]  
  
cantidades_numerico = list(  
  map(  
    int,cantidades  
  )  
)  
  
print(cantidades_numerico)
```
---

## Ejercicio 4 — Salarios con bono

Una empresa otorgó un bono fijo del **10%** sobre el salario de todos los empleados.

```
empleados = [
    {"nombre": "Ana", "salario": 850000},
    {"nombre": "Juan", "salario": 1200000},
    {"nombre": "María", "salario": 980000},
    {"nombre": "Pedro", "salario": 1500000}
]
```

Generá una nueva colección con los salarios actualizados. Elegí una estructura que te parezca adecuada para representar el resultado.

```python
empleados = [  
    {"nombre": "Ana", "salario": 850000},  
    {"nombre": "Juan", "salario": 1200000},  
    {"nombre": "María", "salario": 980000},  
    {"nombre": "Pedro", "salario": 1500000}  
]  
  
salarios = list(  
  map(  
    lambda empleado:  
      empleado["salario"] + (empleado["salario"] * 0.10), empleados  
  )  
)  
  
print(salarios)
```

> [!bug|borde] Corrección
> Vos elegiste devolver solamente los salarios.
> También habría sido válido devolver un nuevo diccionario.
> Por ejemplo
> ```python
>lambda e: {
>   "nombre": e["nombre"],
>    "salario": e["salario"] * 1.10
> }
> ```

---
## Ejercicio 5 — Catálogo en mayúsculas

Una empresa quiere imprimir su catálogo en carteles.

```
productos = [
    "Mouse",
    "Monitor",
    "Notebook",
    "Auriculares",
    "Teclado"
]
```

Generá una nueva colección donde todos los nombres aparezcan completamente en mayúsculas.

```python
productos = [  
    "Mouse",  
    "Monitor",  
    "Notebook",  
    "Auriculares",  
    "Teclado"  
]  
  
nom_mayusculas = list(
	map(
		str.upper, productos
	)
)  
  
print(nom_mayusculas)
```
---

# Desafío de razonamiento

Analizá el siguiente código **sin ejecutarlo**:

```python
def duplicar(numero):
    return numero * 2

valores = [5, 10, 15, 20]

resultado = list(
    map(
        duplicar,
        valores
    )
)

print(resultado)
```

Respondé:
1. ¿Qué función recibe `map()` como primer argumento?
	`map()` recibe la función de `duplicar`.
2. ¿Sobre qué colección trabaja?
	Sobre la colección de valores.
3. ¿Qué hace la función `duplicar()` con cada elemento?
	Multiplica cada elemento de la colección por 2.
4. ¿Qué imprimirá el programa?
	La colección almacenada en `resultado`
5. Si en lugar de `duplicar` se escribiera `duplicar()`, ¿qué ocurriría y por qué?
	Se generara un error, porque `map()` es quien se encarga de ejecutar a la función.

> [!bug|borde] Corección
> Voy a agregar el detalle técnico.
> Si escribís
> ```
> map(duplicar(), valores)
> ```
> Python intenta ejecutar `duplicar()` inmediatamente.
> Pero esa función necesita recibir un parámetro.
> Como no recibe ninguno...
> obtendrías un error parecido a
> ```
> TypeError:
> duplicar() missing 1 required positional argument
> ```
> La forma correcta es
> ```
> map(duplicar, valores)
> ```
> Porque lo que recibe `map()` es la referencia a la función, no el resultado de ejecutarla.
> Ésta es una diferencia muy importante en programación funcional.

