a = int(input("primeiro valor: "))
b = int(input("segundo valor: "))
c = int(input("terceira valor: "))
#verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = b
#verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"o menor valor digitado foi {menor}")
print(f"o maior valor digitado foi {maior}")