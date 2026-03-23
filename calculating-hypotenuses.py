import math
name=input('Seja bem vindo(a)! Como você se chama? ')
print('É um prazer te cohecer {}!'.format(name))
cato=float((input('Qual a medida do seu cateto oposto em cm? ')))
cata=float(input('Qual a medida do cateto adjacente em cm? '))
hip=math.hypot(cato,cata)
print('{}, a hipotenusa do seu triângulo corresponde a: {} cm'.format(name,hip))