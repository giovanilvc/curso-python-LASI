tamanho = float(input('Tamanho em metros quadrados da área a ser pintada: '))   #Recebe o tamanho da área a ser pintada
qnt_litros = tamanho / 6                                                        #Calcula a quantidade de litros necessários

n_latas = qnt_litros/18                                                         #Calcula a quantidade de latas necessárias
if(n_latas <= 1):
  n_latas = 1
elif(n_latas > 1 and n_latas <= 2):
  n_latas = 2
elif(n_latas>2 and n_latas % 2 != 0):
  n_latas = int(n_latas) + 1
valor_latas = n_latas * 80        #Calcula preço

n_galao = qnt_litros/3.6                                                        #Calcula a quantidade de galões necessários
if(n_galao <= 1):
  n_galao = 1
elif(n_galao > 1 and n_galao <= 2):
  n_galao = 2
elif(n_galao>2 and n_galao % 2 != 2):
  n_galao = int(n_galao) + 1
valor_galao = n_galao * 25      #Calcula preço

print(f'Quantidade de latas : {n_latas:.0f}, Valor: {valor_latas:.2f}R$')
print(f'Quantidade de galões : {n_galao:.0f}, Valor: {valor_galao:.2f}R$')