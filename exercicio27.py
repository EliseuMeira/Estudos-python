nome = str(input('digite seu nome completo:')).strip()

primeiro_nome = nome.split()
ultimo_nome = nome.split()
print ('Ola o seu primeiro nome é {}'.format(primeiro_nome[0]))
print ('O seu ultimo nome é {}'.format(ultimo_nome[len(ultimo_nome) -1 ]))