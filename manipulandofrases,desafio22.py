nome =  (input('digite o seu nome completo: ')).strip()
dividido = nome.split()

print ('O seu nome todo em maiusculo:',nome.upper())
print ('o seu nome todo em minusculo:',nome.lower())
print ('em seu nome tem {} caracteres'.format(len(nome) - nome.count(' ')))
print ('o seu primeiro nome tem {} caracteres'.format(len(dividido[0])))


