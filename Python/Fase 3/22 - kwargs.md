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

```python
def mostrar_datos(**lista):
    for clave, valor in lista.items():
        print(f'{clave}: {valor}')

mostrar_datos(
    nombre = "Mouse",
    precio = 18000,
    stock = 15
)
```

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

```python
def cargar_datos():
    empleado = {}

    empleado['nombre'] = input('Ingrese su nombre: ')
    empleado['edad'] = int(input('Ingrese su edad: '))
    empleado['sector'] = input('Ingrese su sector: ')

    return empleado

def mostrar_datos(**kwargs):
    print(f'IMPRIMIR DICCIONARIO COMPLETO')
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

def mostrar_nombre(**kwargs):
    print(f'IMPRIMIR SOLO NOMBRE')
    for clave, valor in kwargs.items():
        if clave == "nombre":
            print(f'{clave}: {valor}')

empleado = cargar_datos()

mostrar_datos(**empleado)

mostrar_nombre(**empleado)
```

> [!bug] Corrección
> Hay una pequeña mejora posible.
> En vez de:
> ```python
> def mostrar_nombre(**kwargs):
> for clave, valor in kwargs.items():
>      if clave == "nombre":
>               print(valor
> ```
> podrías hacer simplemente:
> ```python
> def mostrar_nombre(**kwargs):
> print(kwargs["nombre"])
> ```
> o incluso
> ```python
> print(kwargs.get("nombre"))
> ```

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

```python
lista_usuarios = []  
deco = '-' * 25  
def crear_usuario(**kwargs):  
  for clave, valor in kwargs.items():  
    print(clave, valor)  
  return kwargs  
  
def cargar_usuario(lista,usuario):  
  lista.append(usuario)  
  print(f'Usuario cargado exitosamente')  
  
def mostrar_lista(lista):  
  for usuario in lista:  
    print(usuario)  
  
  
  
  
print(f'Ingresa datos de usuario:\n'  
      f'(escribe "si" para cargar datos, "fin" para terminar)\n'  
      f'{deco}')  
while True:  
  entrada = input("> ")  
  
  if entrada.lower() == "fin":  
    break  
  else:  
    usuario = crear_usuario(  
      nombre=input("Ingrese su nombre: "),  
      edad=input("Ingrese su edad: "),  
      ciudad=input("Ingrese su ciudad: ")  
    )    
    print(usuario)  
    cargar_usuario(lista_usuarios, usuario)  
    print(f'Cargar otro usuario ?\n'  
          f'(escribe "si" para cargar datos, "fin" para terminar)\n'  
          f'{deco}')  
  
mostrar_lista(lista_usuarios)
```

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

```python
def registrar_producto(**producto):  
  for clave, valor in producto.items():  
    print(f'{clave} -> {valor}')
    
registrar_producto(  
    nombre="Mouse",  
    precio=18000,  
    stock=15,  
    marca="Logitech",  
    garantia="12 meses"  
)
```
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

```python
def configurar_servidor(**config):  
  for clave, valor in config.items():  
    print(f'{clave} -> {valor}')  
  
configurar_servidor(  
    host="localhost",  
    puerto=8000,  
    debug=True,  
    database="postgres"  
)
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
	Contiene un diccionario, es decir, clave - valor.
2. ¿Cuántos elementos tendrá ese objeto?
	Tendrá un solo elemento.
3. ¿Qué claves tendrá?
	Las claves que tendrá son:
	- nombre
	- edad
	- ciudad
4. ¿Qué ocurriría si llamáramos `mostrar()` sin enviar argumentos?
	Lo que ocurre es que al no tener datos, nos devolverá nada.
5. Explicá con tus palabras la diferencia conceptual entre `*args` y `**kwargs`.
	La diferencia es que `*args` recibe muchos valores, devuelve una tupla y se accede por índice. Mientras que `**kwargs` recibe pares clave-valor, devuelve un diccionario y se accede por clave.