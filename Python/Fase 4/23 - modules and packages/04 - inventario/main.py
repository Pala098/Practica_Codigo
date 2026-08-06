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