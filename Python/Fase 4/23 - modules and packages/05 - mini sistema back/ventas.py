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