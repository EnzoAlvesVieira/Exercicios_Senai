dias =int(input('Por quanto dias o carro foi alugado? : '))
km =int(input('Quantos quilometros foram percorridos? : '))
total_dias = dias*60
total_km = km*0.15
valor_total = total_dias + total_km
print(f'Você percorreu {km} quilometros durante {dias} dias, Então o preço a se pagar é R$: {valor_total}')