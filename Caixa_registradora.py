print('================================== \n')
print('=       CAIXA REGISTRADORA      == \n')
print('================================== \n\n')
    
    
import produtos_banco

total = 0
    
    
print('|===1 - Biscoito Recheado (R$2.00)===|\n')
print('|===2 - Pipoca Salgada (R$3.45)===|\n')
print('|===3 - Cerveja Long Neck (R$10.99)===|\n')
print('|===4 - Tempero Especial (R$8.99)===|\n')
print('|===5 - Chocolate Amargo (R$20.99)===|\n')
print('|===6 - Coca-Cola 2l (R$9.90)===|\n')
print('|===7 - Molho Madeio (R$13.70)===|\n')
print('|===8 - Maionese 1kg (R$15.00)===|\n')
print('|===9 - Amaciante (R$8.86)===|\n')
print('|===10 - Pote (R$12.90)===|\n')
print('|===0 - Digite 0 para Finalizar as compras===|\n')
   
while True:
        Cesta = input('Digite o Código do Produto: ')
        
        if Cesta == '0':
            print('Compra finalizada! Obrigado por comprar com a gente! Volte sempre!')
            break
        elif Cesta in produtos_banco.produtos:
            
            preco_prod = produtos_banco.produtos [Cesta] ["Preco"]
            nome_prod = produtos_banco.produtos [Cesta] ["Nome"]
            
            total += preco_prod
            
            print('<----------------------------------->')
            print(f'{nome_prod} foi adicionado a Cesta! R${preco_prod}')
            print(f'Total até agora: {total:=.2f}')
            print('<----------------------------------->\n\n')
            
            
        else:
            print ('PRODUTO NÃO CADASTRADO!')
            
print(f'O total da sua compra foi de: {total}\n')
            
print('===1 - PIX ===')
print('===2 - Débito ===')
print('===3 - Crédito ===')
print('===4 - Dinheiro ===\n')
            
Paga_type = input('Escolha a forma de pagamento: ')
            
if Paga_type == '1':
        valor = total * 0.90
        print('Desconto de 10% aplicado\n')
        print(f'Você vai pagar R${valor:=.2f}\n')
        
elif Paga_type == '2':
        senha = input('Digite sua senha: ')
        print('Obrigado por comprar conosco!\n')
        
elif Paga_type == '3':
        parcelas = int(input('Em quantas parcelas você vai comprar: '))
        print(f'Sua parcela foi de {parcelas}x! Obrigado por comprar conosco!\n')
        
elif Paga_type == '4':
        dinheiro = float(input('Quanto você vai pagar: '))
        troco = dinheiro - total
        print(f'Seu troco foi de R${troco:=.2f}. Obrigado por comprar conosco!\n')
        
else:
        print('Opção invalida!\n')