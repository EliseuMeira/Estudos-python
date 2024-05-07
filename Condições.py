#carro = int(input('quantos anos tem seu carro'))

#if carro <=3:
        #print ('carro novo')
#else:
        #print ('carro velho')
#print('---fim---')


n1 = float(input('digite a nota do primeiro semestre:'))
n2 = float (input('digite a nota do seundo semreste:'))

nota = (n1 + n2) / 2

print ('a sua media foi: {:.1f}'.format(nota))

if nota >=6:
    print ('você teve uma boa nota')
else:
    print ('você não teve uma boa nota ESTUDE MAIS')