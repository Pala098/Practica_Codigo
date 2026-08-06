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


