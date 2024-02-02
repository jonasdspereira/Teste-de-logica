
#Desafios de lógica 
#Escolhi python por ser uma linguagem em que tenho um certo nível de conhecimento, mesmo sendo básico 😄

#Desafio 1 - Ler um numero até que o usuário digite 10.

n = int(input("Digite um número: "))
while n != 10:
        print("Tente novamente")
        n = int(input("Digite um número: "))

if n == 10:
        print("Número correto!");

#Desafio 2 - Definir a idade de uma pessoa e verificar se ela é maior de idade ou não.
#Esse eu fiquei em duvida do que significa "definir", no caso eu dexei o usuário informar a idade.

idade = int(input("Digite a sua idade: "))
if idade <= 17:
    print("Você é menor de idade!");
#Aqui eu poderia usar o elif com a condiçao "idade >= 18", mas acredito que o else seja o suficiente.
else:
    print("Você é maior de idade!");


#Desafio 3 - Construir uma tabuada de um número

numTab = int(input("Informe o número da tabuada desejada: "))

for i in range (1, 11):
    tab = numTab * i
    print(f'{numTab} x {i} = {tab}');


#Desafio 4 - Gerar 10 numeros aleatórios e informar o menor e o maior deles.


import random
numeros = [random.randint(0,100) for _ in range(10)]
print(numeros)
maior = max(numeros)
menor = min(numeros)
print(f'\n Maior número: {maior}\n Menor número: {menor}')


#Desafio 5 - Jokenpo


import random

def jp(p1):
    opcoes = ["pedra", "papel", "tesoura"]
    p2 = random.choice(opcoes)

    print(f"\nVocê escolheu: {p1}")
    print(f"Jogador 2 escolheu: {p2}")

    if p1 == p2:
        return "Empate!"
    elif (
        (p1 == "pedra" and p2 == "tesoura") or
        (p1 == "papel" and ep2 == "pedra") or
        (p1 == "tesoura" and p2 == "papel")
    ):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

# Solicitar escolha do jogador
p1 = input("Escolha: pedra, papel ou tesoura? ").lower()

# Validar escolha do jogador
if p1 in ["pedra", "papel", "tesoura"]:
    resultado = jp(p1)
    print(resultado)
else:
    print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")


#Desafio 6 - Desconto

def desconto(produto, preco, qtd):
    if qtd <= 10:
        total = preco * qtd
    elif qtd <= 20:
        total = preco * qtd * 0.9
    elif qtd <= 50:
        total = preco * qtd * 0.8
    else:
        total = preco * qtd * 0.75

    print(f"\n Produto: {produto}\n Quantidade: {qtd}\n Total da compra: {total}")

produto = input("Digite o nome do produto: ")
qtd = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço: "))

calcDesc = desconto(produto, preco, qtd)



