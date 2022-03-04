# 1. Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
L = [5, 7, 2, 9, 4, 1, 3]
# a) tamanho da lista;
print(len(L))
# b) maior valor da lista;
print(max(L))
# c) menor valor da lista;
print(min(L))
# d) soma de todos os elementos da lista;
print(sum(L))
# e) lista em ordem crescente;
print(sorted(L))
# f) lista em ordem decrescente.
print(sorted(L,key=int, reverse=True))

# 2. Faça um programa que leia 4 valores, calcule a média e imprima positivo ou negativo (para ser positivo a média deve ser acima de 1).
contador = 1
valores2 = []
while (contador <5):
    valores2.append(int(input(f"Por favor, informe o valor {contador}: "))) 
    contador += 1
mediavalores2 = sum(valores2)/len(valores2)
if mediavalores2 > 1:
    print(f'A média dos valores é {mediavalores2} e o resultado é positivo.')
else: print(f'A média dos valores é {mediavalores2} e o resultado é negativo.')

# 3. Escreva um programa que leia 20 valores inteiros e informe a média deles, o maior e o menor valor.
contador = 1
valores3 = []
while (contador <21):
    valores3.append(int(input(f"Por favor, informe o valor {contador}: "))) 
    contador += 1
mediavalores3 = sum(valores3)/len(valores3)
print(f'A média dos valores é {mediavalores3}, o maior número é {max(valores3)} e o menor é {min(valores3)}.')

# 4. Crie uma função para desenhar uma linha, usando o caractere '_' (underline). O tamanho da linha deve ser definido na chamada da função.
linha = "_"
def funcaolinha(tamanho):
    print(linha*tamanho)
qtdlinha = int(input("Por favor, insira quantas vezes você quer que o caractere '_' apareça: "))
funcaolinha(qtdlinha)

# 5. Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista, enumerando-os.
def funcaolista(lista):
    print(lista)
contador = 1
valores5 = []
while (contador <11):
    valores5.append(input(f"Por favor, informe o valor {contador}: ")) 
    contador += 1
funcaolista(valores5)

#6. Crie um programa que converta horas em segundos, conforme o valor que o usuário informar quando solicitado a ele.
def horaparasegundo(hora):
    hora = hora*60*60
    return hora
valorhora = int(input("Por favor, informe a quantidade de horas: "))
print(f"A quantidade de horas informada foi {valorhora}h e a conversão em segundos fica {horaparasegundo(valorhora)}s.")

# 7. Altere o código a seguir, para o menor número de linhas possível, mantendo o mesmo resultado:
# print(" *")
# print(" * *")
# print(" * *")
# print(" * *")
# print("*** ***")
# print(" * *")
# print(" * *")
# print(" *****")
print(" *", " * *", " * *", " * *", "*** ***", " * *", " * *", " *****", sep="\n")






