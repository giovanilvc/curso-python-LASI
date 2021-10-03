#Função
def calculo(n):
  aux = 1
  A = n
  while((aux + 1) <= n):
    A = A + ((n-aux)/(aux+1))
    aux+=1
  return A

#Print do resultado
print(f'A = {calculo(4)}')