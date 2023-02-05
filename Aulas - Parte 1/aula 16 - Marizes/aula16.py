carros = [['Modelo', 'HRV'],
          ['Fabricante', 'Honda'],
          ['Ano', 2016]
          ]
carros[2][1] = 2019
for l, c in carros:
    print(f'Linha: {l}' f'| Coluna: {c}')