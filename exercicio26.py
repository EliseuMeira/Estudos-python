nome = str(input("qual o seu nome:")).strip().upper()

print ('em seu nome apareceu {} letras A '.format(nome.count('A')))
print ('A primeira letra A apareceu na {} posição'.format(nome.find('A') +1))
print ('A ultima letra A aparece a posição {}'.format(nome.rfind('A') +1 ))