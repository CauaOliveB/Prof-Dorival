# 1. Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
# métodos para calcular a área e o perímetro do círculo.

# class Circulo():
#     def __init__(self,raio):
#         self.raio = raio
        
#     def calcularArea(self):
#         return (3.14* self.raio **2)
    
#     def calcularPerimetro(self):
#         return (2*3.14*self.raio)

        
#     def exibir(self):
#         area = self.calcularArea()
#         perimetro = self.calcularPerimetro()
#         print(f"Raio:{self.raio}, Área:{area}, Perimetro:{perimetro}")
        
# circulo1 = Circulo(1)

# circulo1.exibir()

# 2. Implemente uma classe chamada “ContaBancária” que possua atributos para 
# armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
# depósitos e saques.

# class ContaBancaria():
#     def __init__(self, numeroConta, nomeTitular,saldo):
#         self.numeroConta = numeroConta
#         self.nomeTitular = nomeTitular
#         self.saldo = saldo

#     def deposito(self, valor):
#         self.saldo += valor
#         return (f"Depósito realizado: R${valor}. Saldo atual: R${self.saldo}")

#     def saque(self, valor):
#         if valor > self.saldo:
#             print("Saldo insuficiente para realizar o saque.")
#         else:
#             self.saldo -= valor
#             print(f"Saque realizado: R${valor}. Saldo atual: R${self.saldo}")

# contaBradesco = ContaBancaria(123456, "Fernanda Militão Fretes", 1000 )
# contaBradesco.deposito(500)
# contaBradesco.saque(100)    
        
# 3. Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
# a altura. Implemente métodos para calcular a área e o perímetro do retângulo. 

# class Retangulo():
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
        
#     def calcularArea(self):
#         return self.largura * self.altura
    
#     def calcularPerimetro(self):
#         return 2 * (self.largura + self.altura)
    
# retangulo1 = Retangulo(2,6)
# area = retangulo1.calcularArea()
# print(area)
# perimetro = retangulo1.calcularPerimetro()
# print(perimetro)

# 4. Implemente uma classe chamada “Aluno” que possua atributos para armazenar o 
# nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
# notas e verificar a situação do aluno (aprovado ou reprovado). 

# class Aluno():
#     def __init__(self,nome,MT,nota1, nota2, nota3):
#         self.nome = nome
#         self.MT = MT
#         self.nota1 = nota1
#         self.nota2 = nota2
#         self.nota3 = nota3

#     def mediaNotas(self):
#         return (self.nota1+self.nota2+self.nota3) /3

#     def situacao(self):
#         if (self.mediaNotas() < 5):
#             return("Reprovado")
#         else:
#             return("Aprovado")

# aluno1 = Aluno("Carlos", 1123, 5, 3 , 4)
# print(f"Média:{aluno1.mediaNotas()}")
# print(f"Situação:{aluno1.situacao()}")

# 5. Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o 
# salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
# considerando descontos de impostos e benefícios. 

# class Funcionario():
#     def __init__(self,nome,salario,cargo):
#         self.nome = nome
#         self.salario = salario
#         self.cargo = cargo

#     def salarioLiquido(self):
#         return self.salario - 336 - 20

# funcionario1 = Funcionario("Carlos", 3000, "Programador Junior")
# print(f"Salário líquido:{funcionario1.salarioLiquido()}")