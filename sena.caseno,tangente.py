from math import cos , sin , tan , radians 

n = float (input('digite o Angulo que você deseja:'))

rad = radians (n)

print ('o valor em seno é {:.2f}'.format(sin(rad)))
print ('o valor em coseno é {:.2f}'.format(cos(rad)),)
print ('o valor em tangente é {:.2f}'.format(tan(rad)))

