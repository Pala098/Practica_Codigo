## Ejercicio #1 - Catálogo de categorías
Una tienda tiene la siguiente lista de productos:

```
productos = [
    {"nombre": "Mouse", "categoria": "Periféricos"},
    {"nombre": "Teclado", "categoria": "Periféricos"},
    {"nombre": "Monitor", "categoria": "Monitores"},
    {"nombre": "Notebook", "categoria": "Computadoras"},
    {"nombre": "Impresora", "categoria": "Periféricos"},
    {"nombre": "Ultrabook", "categoria": "Computadoras"}
]
```

Generá una estructura que contenga únicamente las categorías existentes, sin repetir ninguna.

```python
productos = [  
    {"nombre": "Mouse", "categoria": "Periféricos"},  
    {"nombre": "Teclado", "categoria": "Periféricos"},  
    {"nombre": "Monitor", "categoria": "Monitores"},  
    {"nombre": "Notebook", "categoria": "Computadoras"},  
    {"nombre": "Impresora", "categoria": "Periféricos"},  
    {"nombre": "Ultrabook", "categoria": "Computadoras"}  
]  
  
lista_sin_repetidos = {  
    producto['categoria']  
    for producto in productos  
}  
  
print(lista_sin_repetidos)
```
---
## Ejercicio #2 - Usuarios que iniciaron sesión
El sistema registró los siguientes accesos:

```
accesos = [
    "juan",
    "ana",
    "juan",
    "pedro",
    "lucas",
    "ana",
    "juan",
    "maria"
]
```

Mostrá el listado de usuarios únicos que ingresaron al sistema.

```python
accesos = [  
    "juan",  
    "ana",  
    "juan",  
    "pedro",  
    "lucas",  
    "ana",  
    "juan",  
    "maria"  
]  
  
lista_user_uni = {  
    usuario  
    for usuario in accesos  
}  
  
print(lista_user_uni)
```
---
## Ejercicio #3 - Empleados habilitados
Se tiene la siguiente información:

```
empleados = [
    {"nombre": "Ana", "activo": True},
    {"nombre": "Juan", "activo": False},
    {"nombre": "María", "activo": True},
    {"nombre": "Pedro", "activo": True},
    {"nombre": "Lucas", "activo": False}
]
```

Obtené únicamente los nombres de los empleados que se encuentran activos.

```python
empleados = [  
    {"nombre": "Ana", "activo": True},  
    {"nombre": "Juan", "activo": False},  
    {"nombre": "María", "activo": True},  
    {"nombre": "Pedro", "activo": True},  
    {"nombre": "Lucas", "activo": False}  
]  
  
empleados_activos = {  
    empleado['nombre']  
    for empleado in empleados  
    if empleado['activo'] == True  
}  
  
print(empleados_activos)
```
---
## Ejercicio #4 - Normalización de ciudades
Una empresa tiene registrados clientes provenientes de distintas ciudades, pero los nombres fueron cargados con distintas combinaciones de mayúsculas y minúsculas:

```
ciudades = [
    "La Plata",
    "la plata",
    "LA PLATA",
    "Berisso",
    "berisso",
    "Ensenada",
    "ENSENADA"
]
```

Construí una estructura que permita conocer las ciudades distintas, considerando que `"La Plata"`, `"la plata"` y `"LA PLATA"` representan la misma ciudad.

```python
ciudades = [  
    "La Plata",  
    "la plata",  
    "LA PLATA",  
    "Berisso",  
    "berisso",  
    "Ensenada",  
    "ENSENADA"  
]  
  
lista_ciudades = {  
    ciudad.upper()  
    for ciudad in ciudades  
}  
  
print(lista_ciudades)
```
---
## Ejercicio #5 - Tecnologías utilizadas
Se registraron las tecnologías utilizadas por distintos desarrolladores:

```
desarrolladores = [
    {"nombre": "Ana", "tecnologias": ["Python", "SQL"]},
    {"nombre": "Juan", "tecnologias": ["Python", "Git"]},
    {"nombre": "María", "tecnologias": ["SQL", "Power BI"]},
    {"nombre": "Pedro", "tecnologias": ["Git", "Docker"]},
    {"nombre": "Lucas", "tecnologias": ["Python", "Docker"]}
]
```

Generá una estructura que contenga todas las tecnologías utilizadas en la empresa, sin repetir ninguna.

> El registro de tecnologias contiene listas internamente, y un set no puede almacenar listas.

> [!bug|borde] Corrección
> **Pero había otra forma de resolverlo.**
> La clave estaba en que cada empleado tiene una lista de tecnologías.
> Había que recorrer ambas colecciones.
> Es decir:
> ```python
> {
>  tecnologia
>  for desarrollador in desarrolladores
>  for tecnologia in desarrollador["tecnologias"]
> }
> ```
> Fijate que aparecen **dos `for`**.
> Eso produce:
> ```python
> {
> "Python",
>"SQL",
>  "Git",
>  "Docker",
>  "Power BI"
> }
> ```
> Y acá aprendiste algo nuevo.
> Las comprehensions pueden tener más de un `for`.
---
## Desafío de razonamiento
Analizá el siguiente código **sin ejecutarlo**:

```
ventas = [
    {"cliente": "Juan", "producto": "Mouse"},
    {"cliente": "Ana", "producto": "Monitor"},
    {"cliente": "Juan", "producto": "Teclado"},
    {"cliente": "Pedro", "producto": "Mouse"},
    {"cliente": "Ana", "producto": "Notebook"}
]

clientes = {
    venta["cliente"].upper()
    for venta in ventas
}

print(clientes)
```

Respondé:
1. ¿Qué elementos recorrerá la comprensión?
	Recorrerá la lista de ventas.
2. ¿Qué transformación se aplica a cada cliente?
	Se aplica `upper()`, que lo que hace es que convierte el formato a mayúsculas.
3. ¿Cuántos elementos tendrá el set final?
	El set tendrá los nombres de los clientes, o el valor de la clave 'cliente'.
4. ¿Por qué `"Juan"` aparece una sola vez aunque realizó dos compras?
	Porque un set no almacena duplicados.
5. ¿En qué situaciones de Data Analytics podría ser útil generar un conjunto de valores únicos como este?
	En las situaciones que imagino se pude usar, además de cualquiera donde se necesite un valor único como dato:
	- Un listado de ciudades
	- Un listado de categorías de productos