import empleados as emp

pago_por_dia = float(input(f'Ingrese el pago diario que recibe: \n> $'))

print(f'Pago diario: ${pago_por_dia:.2f}\n'
      f'Salario anual aprox.: ${emp.salario_anual(pago_por_dia):.2f}\n'
      f'Salario mensual aprox.: ${emp.salario_mensual(pago_por_dia):.2f}')