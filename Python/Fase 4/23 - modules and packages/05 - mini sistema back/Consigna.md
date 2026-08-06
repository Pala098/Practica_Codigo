Crear esta estructura:

```
sistema/

│

├── usuarios.py

├── productos.py

├── ventas.py

└── main.py
```

Cada módulo debe tener al menos **dos funciones** relacionadas con su responsabilidad.

`main.py` debe importar los tres módulos y ejecutar alguna función de cada uno para demostrar que la organización funciona correctamente.

No hace falta que sea un sistema completo; lo importante es practicar la división del código.

### `main.py`
```python
def agregar_producto(lista):
  nombre = input('Ingese el nombre del producto: ')
  lista.append(nombre)
  print(f'Produco agregado...')

def mostrar_productos(lista):
  for producto in lista:
    print(producto)

def buscar_producto(lista):
  valor = input(f'Ingrese el producto que busca: \n> ')
  for producto in lista:
    if producto.lower() == valor.lower():
      print(f'El producto existe en el listado.')
    else:
      print(f'Producto inexistente !')
```

### `producto.py`
```python
def cargar_producto(lista):
  producto = input(f'Ingese el producto: ')

  lista.append(producto)
  print(f'Producto cargado...')

def mostrar_productos(lista):
  for producto in lista:
    print(producto.upper())
```

### `usuario.py`
```python
def cargar_usuario(lista):
  usuario = input(f'Ingese su nombre: ')

  lista.append(usuario)
  print(f'Usuario cargado...')

def mostrar_usuarios(lista):
  for usuario in lista:
    print(usuario.upper())
```

### `utilidades.py`
```python
def mostrar_menu():
  deco = '-' * 25
  entrada = int(input(f'..:: MENU ::..\n'
                  f'{deco}\n'
                  f'--- usuarios ---\n'
                  f'1. Cargar usuario\n'
                  f'2. Mostrar lista de usuarios\n'
                  f'--- productos ---\n'
                  f'3. Cargar producto\n'
                  f'4. Mostrar lista de productos\n'
                  f'--- ventas ---\n'
                  f'5. Cargar una venta\n'
                  f'0. Salir del sistema\n'
                  f'{deco}\n'
                  f'Seleccione una opcion:\n'
                  f'> '))
  return entrada
```

### `ventas.py`
```python
def registrar_venta(list_user,list_prod):
  venta = {}

  print(f'LISTADO DE USUARIOS')
  for usuario in list_user:
    print(f'- {usuario}')
  # opcion_user = input(f'Ingrese el usuario de la lista que se asigna la venta: \n'
  #                     f'> ')
  venta["usuario"] = input(f'Ingrese el usuario de la lista que se asigna la venta: \n'
                          f'> ')

  for venta in list_prod:
    print(f'- {venta}')

  # opcion_vent = input(f'Ingrese el producto de la lista vendido: \n'
                      # f'> ')
  venta["producto"] = input(f'Ingrese el producto de la lista que se asigna a la venta: \n'
                            f'> ')
  return venta
```