import producto, usuario, ventas, utilidades

lista_productos = []
lista_usuarios = []
registro_ventas = []

while True:
  entrada = utilidades.mostrar_menu()
  if entrada == 1:
    usuario.cargar_usuario(lista_usuarios)
  elif entrada == 2:
    usuario.mostrar_usuarios(lista_usuarios)
  elif entrada == 3:
    producto.cargar_producto(lista_productos)
  elif entrada == 4:
    producto.mostrar_productos(lista_productos)
  elif entrada == 5:
    venta = ventas.registrar_venta(lista_usuarios,lista_productos)
    registro_ventas.append(venta)
  elif entrada == 0:
    print(f'Saliendo del sistema...')
    break
  else:
    print(f'Opcion invalida !')