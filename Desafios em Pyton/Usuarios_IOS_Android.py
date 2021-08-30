print('Responda essa rapida pesquisa sobre seu celular!')

#android ='android'
#ios = 'ios'



somaandr = 0;
somaios = 0;
resposta = str(input('Seu sistema é Android?' ))
if resposta == 'sim':
 print('Salvo com sucesso, você usa um Android!')
 somaandr +=1
else:
 print('Salvo com sucesso! você tem um IOS!')
 somaios +=1
idade = str(input('Qual a sua idade?'))
concatenar = 'A sua idade é' +idade
print(concatenar)

while resposta:
 print('Salvo com sucesso')
