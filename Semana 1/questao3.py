#Inicializando Variáveis
saldoTotal  = 0
nDevedor    = 0
nCredor     = 0

#Recebendo o saldo dos clientes
for i in range(10):
  print(f'Digite o saldo do cliente {i+1}: ')
  saldo = float(input())
  if(saldo>=0):                   #Contabilizando credores
    nCredor += 1
  else:                           #Contabilizando devedores
    nDevedor +=1
  saldoTotal += saldo

print(f'Saldo Médio dos clientes: {saldoTotal/10:.2f}')
print(f'Porcentagem de clientes com saldo devedor: {(nDevedor/10)*100}%' )
print(f'Porcentagem de clientes com saldo credor: {(nCredor/10)*100}%')