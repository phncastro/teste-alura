nome = input("Digite aqui seu nome: ")
idade = int(input("Digite aqui sua idade: "))
condicao = 1

def saudar(saudacao, nome):
    print(f"{saudacao} {nome}!")


saudar("Bom dia,", "Marcio")

saudar("Bom dia", "Pablo")


    

while condicao:
    if idade >= 18:
        print("Você é maior de idade!")
    elif idade > 0 and idade < 18:
        print("Você é menor de idade!")
    elif idade > 99:
        print("Idade inválida!")
    else:
        print("Digite uma idade válida!")
    if isinstance(idade, int):
        break
        
