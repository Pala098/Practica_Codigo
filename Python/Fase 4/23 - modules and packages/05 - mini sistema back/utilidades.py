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