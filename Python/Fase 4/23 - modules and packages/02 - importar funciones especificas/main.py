from productos import calcular_iva, calcular_descuento

precio = float(input(f'Ingrese el precio del producto: \n'
                     f'> '))

precio_final = precio + calcular_iva(precio) + calcular_descuento(precio)

print(f'Precio: ${precio:.2f}\n'
      f'IVA: ${calcular_iva(precio):.2f}\n'
      f'Descuento 15%: ${calcular_descuento(precio):.2f}\n'
      f'PRECIO FINAL: ${precio_final:.2f}\n')