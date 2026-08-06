Crear un módulo:

```
inventario.py
```

Con las funciones:

- agregar producto
- mostrar productos
- buscar producto

Luego crear un `main.py` que importe el módulo y permita utilizar las tres funciones mediante un menú.

> **Acá podés reutilizar bastante código de ejercicios anteriores.** En este caso sí tiene sentido hacerlo, porque el objetivo es practicar la separación en módulos, no reinventar el sistema de inventario.

### `main.py`
```python
import inventario

lista_productos = []

while True:
  entrada = int(input(f'MENU\n'
                      f'1. Agregar producto\n'
                      f'2. Mostrar productos\n'
                      f'3. Buscar producto\n'
                      f'0. Salir\n'
                      f'Seleccione una opcion:\n'
                      f'> '))

  if entrada == 1:
    inventario.agregar_producto(lista_productos)
  elif entrada == 2:
    inventario.mostrar_productos(lista_productos)
  elif entrada == 3:
    inventario.buscar_producto(lista_productos)
  elif entrada == 0:
    print(f'Saliendo del sistema...')
    break
  else:
    print(f'Opcion incorrecta...')
```

### `inventario.py`
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
