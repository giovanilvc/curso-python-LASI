qnt_hr = float(input('Quanto você ganha por hora? '))           #Recebe a quantidade de dinheiro por horas 
num_hrs = float(input('Quantas horas você trabalha por mês? ')) #Recebe a quantidade de horas trabalhadas
salario = qnt_hr*num_hrs                                        #Calcula salário mensal

print(f'Seu salário mensal é de {salario:.2f} R$')