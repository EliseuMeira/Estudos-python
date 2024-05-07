velocidade = float (input('qual a sua velocidade atual:'))

multa = (velocidade- 80) * 7 

if velocidade > 80:
    print ('você foi mutado')
    print ('você tem que pagar R${:.2f}'.format(multa))
else:
    print ('Esta dentro do limite de velocida da Via')
print ('Tenha uma otima viagem dirija com segurança!!')