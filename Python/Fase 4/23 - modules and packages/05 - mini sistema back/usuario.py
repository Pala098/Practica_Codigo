def cargar_usuario(lista):
  usuario = input(f'Ingese su nombre: ')

  lista.append(usuario)
  print(f'Usuario cargado...')

def mostrar_usuarios(lista):
  for usuario in lista:
    print(usuario.upper())