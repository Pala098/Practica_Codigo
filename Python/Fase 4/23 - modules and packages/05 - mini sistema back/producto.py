def cargar_producto(lista):
  producto = input(f'Ingese el producto: ')

  lista.append(producto)
  print(f'Producto cargado...')

def mostrar_productos(lista):
  for producto in lista:
    print(producto.upper())