
valor = float(input("numero: "))

if valor < 10:
    print(f"Esse valor é menor que 10", valor)
else:
    print("Esse valor é maior que 10", valor)


numero = float(input("numero: "))
if numero >= 0:
    print("Seu numero é positivo")
else:
    print("Seu numero é negativo")



Quantidade = int(input("Numero de maças: "))
if Quantidade >= 12:
    valor = Quantidade * 1
    print(valor)
else:
    valor = Quantidade * 1.30
    print(valor)


Nota1 = float(input("Nota do p1: "))
Nota2 = float(input("Nota do p2: "))
Media = (Nota1 + Nota2)/2
if Media >= 6:
    print("Aprovado")
else:
    print("Reprovado")



num1 = int(input("Numero1 :"))
num2 = int(input("Numero2 :"))
if num1 > num2:
    print(num1)
else:
    print(num2)


num1 = int(input("Numero1 :"))
num2 = int(input("Numero2 :"))
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

numerodocliente = int(input("Matricula: "))

saldo = float(input("Quanto saldo: "))
Credito = float(input("Quanto credito: "))
debito = float(input("Quanto debito: "))
saldoatual = (saldo - debito + Credito)

if saldoatual >= 0:
    print("Saldo positivo")
else:
    print("Saldo Negativo")




quantidadeatual = float(input("Estoque atual: "))
quantidademax = float(input("Estoque max.: "))
quantidademin = float(input("Estoque min.: "))
mediadeestoque = ((quantidademax + quantidademin)/2)

if quantidadeatual >= mediadeestoque:
    print("Não efetuar compra")
else:
    print("Efetuar compra")
    
    
    
    

    
    

    
prova1 = float(input("Nota1: "))
prova2 = float(input("Nota2: "))
mediadanota = ((prova1 + prova2)/2)

if mediadanota >= 9:
    print("Seu conceito de nota foi é A e você foi Aprovado")
elif 9 > mediadanota >= 7.5:
    print("Seu conceito de nota é B e você foi Aprovado")
elif 7.5 > mediadanota >= 6:
    print("Seu conceito de nota é C e você foi Aprovado")
elif 6 > mediadanota >= 4:
    print("Seu conceito de nota é D e você foi Reprovado")
else:
    print("Seu conceito de nota é E e você foi Reprovado")



 
    

    
    
    
    
    
    
    
    
    
    
    
















