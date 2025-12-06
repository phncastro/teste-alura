# Projeto de Teste — Verificação de Idade

Este repositório contém apenas um código simples utilizado para testes gerais. O objetivo é praticar conceitos básicos de Python, como entrada de dados, funções, condicionais e loops.

## 📌 Descrição do Código

O script solicita ao usuário seu nome e idade, exibe algumas saudações pré-definidas e depois verifica se a idade informada corresponde a alguém **maior**, **menor** ou se é uma idade **inválida**.

## 🔍 Funcionalidades

* Solicita nome e idade via `input()`
* Define e utiliza uma função `saudar()`
* Exibe saudações fixas
* Verifica:

  * Se o usuário é maior de idade
  * Se é menor de idade
  * Se a idade é inválida
* Utiliza um loop `while` para controle simples

## 🧠 Lógica Principal

```python
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
```

## 📦 Objetivo do Repositório

Este projeto **não** tem finalidade prática específica — trata-se apenas de um ambiente de teste para praticar:

* Estruturação de repositórios
* Escrita de README
* Versionamento de arquivos simples em Python

## 📝 Observações

Sinta-se à vontade para editar, melhorar ou expandir o código conforme a necessidade dos seus testes!
