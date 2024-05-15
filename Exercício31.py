distancia = float (input("qual é a distancia da viagem:"))

print (f'fazendo uma viagem de {distancia}Km ')
n1 = distancia * 0.50
n2 = distancia * 0.45

if distancia > 200:
    print(f"vai pagar RS${n2}")
else:
    print(f"vai pagar muito RS${n1}")