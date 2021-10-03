def validacaoData(data):
  data = data.split('/') #separa dia, mes e ano
  dia = int(data[0])
  mes = int(data[1])
  ano = int(data[2])
  
  #Dicionario para facilitar o print da data por extenso no final
  meses = { 1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro' }

  #Validação
  if dia < 0 or dia> 31:
    return "NULL"
    
  if mes>0 and mes<=12:           

    if mes == 2:
      if (dia == 29 and ano % 4 !=0) or dia >= 30: #Verificaçãoa ano bissexto
        return "NULL"

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
      if dia > 30:
        return "NULL"
  
  else:
    return "NULL"
  
  return f'{dia} de {meses[mes]} de {ano} ' 

validacaoData('29/02/2000') #Teste da função