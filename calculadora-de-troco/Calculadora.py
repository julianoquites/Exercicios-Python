notas = [200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
centavos = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
valorCompra = float(input("Por favor, insira o valor da compra: "))
valorRecebido = float(input("Por favor, insira o valor recebido de pagamento: "))
troco = round((valorRecebido - valorCompra),2)
if(troco == 0):
    print("Sem necessidade de troco, pagamento com valor exato.")
else:
    print(f"Troco: R${troco}")

for nota in notas:
    qtd = int(troco/nota)
    if (troco-nota) >= 0:
        print(f"Quantidade de notas de R${round(nota)}: {qtd}")
        troco = float("{:.2f}".format(troco - (nota*qtd)))
  
for centavo in centavos:
    qtd = int(troco/centavo)
    if (troco-centavo) >= 0:
        print(f"Quantidade de moedas de {round(centavo*100)} centavo(s): {qtd}")
        troco = float("{:.2f}".format(troco - (centavo*qtd)))