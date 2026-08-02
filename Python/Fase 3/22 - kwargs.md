## Ejercicio 1
*Información de un producto*

Crear una función:

```
def mostrar_producto(**datos):
```

Debe recibir información como:

```
mostrar_producto(
    nombre="Mouse",
    precio=18000,
    stock=15
)
```

Y mostrar:

```
nombre: Mouse
precio: 18000
stock: 15
```

Recorré el diccionario usando un `for`.

---
## Ejercicio 2
*Empleado*

Crear una función

```
def crear_empleado(**datos):
```

Debe devolver el diccionario recibido.

Luego:

- guardar el resultado en una variable
- imprimir el diccionario completo
- imprimir solamente el nombre del empleado usando la clave correspondiente.

---
## Ejercicio 3
*Sistema de usuarios*

Crear una lista de usuarios.

Cada usuario debe crearse usando:

```
crear_usuario(**datos)
```

Ejemplo

```
usuario = crear_usuario(

    nombre="Ana",

    edad=25,

    ciudad="La Plata"
)
```

Guardar varios usuarios en una lista y luego recorrer la lista mostrando toda la información de cada uno.

---
## Ejercicio 4
*Productos con información variable*

Crear una función

```
def registrar_producto(**producto):
```

Debe permitir registrar productos con distinta cantidad de información.

Ejemplo:

```
registrar_producto(

    nombre="Notebook",

    precio=950000
)
```

y también:

```
registrar_producto(

    nombre="Mouse",

    precio=18000,

    stock=15,

    marca="Logitech",

    garantia="12 meses"
)
```

La función debe mostrar **todas** las claves y valores, sin asumir cuáles existen.

---
## Ejercicio 5
*Mini sistema de configuración*

Crear una función

```
def configurar_servidor(**config):
```

Llamarla así:

```
configurar_servidor(

    host="localhost",

    puerto=8000,

    debug=True,

    database="postgres"

)
```

La función debe recorrer el diccionario e imprimir:

```
host : localhost

puerto : 8000

debug : True

database : postgres
```

---

# Desafío de razonamiento

Analizá el siguiente código **sin ejecutarlo**:

```
def mostrar(**datos):
    print(datos)

mostrar(
    nombre="Ana",
    edad=25,
    ciudad="Córdoba"
)
```

Respondé:
1. ¿Qué tipo de dato contiene `datos`?
2. ¿Cuántos elementos tendrá ese objeto?
3. ¿Qué claves tendrá?
4. ¿Qué ocurriría si llamáramos `mostrar()` sin enviar argumentos?
5. Explicá con tus palabras la diferencia conceptual entre `*args` y `**kwargs`.