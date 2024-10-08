def obter_detalhes_pedido():
    # Simula a obtenção de detalhes de um pedido
    pedido = {
        'item': 'notebook',  # Use vírgula para separar os itens
        'preco': 1200.00,
        'quantidade': 2      # Use dois pontos para atribuir valor
    }
    pedido2 = {
        'item': 'celular' ,
        'preco': 1000,
        'quantidade': 3     
        
        
    }
    print('Detalhes do pedido obtidos.')
    return pedido , pedido2

def calcular_preço_total(pedido):
    #Calcula o preço total do pedido
    preco_total = pedido['preco'] * pedido['quantidade']
    print(f'Preço total calculado: R${preco_total}')
    return preco_total 

def calcular_preço_total2(pedido2):
    #Calcula o preço total do pedido2
    preco_total2 = pedido2['preco'] * pedido2['quantidade']
    print(f'Preço total calculado: R${preco_total2}')
    return preco_total2


def enviar_confirmacao(pedido,preco_total):
    # Simula o envio de uma confirmação de pedido
    print(f'Confirmação enviada para o {pedido["quantidade"]} {pedido["item"]}(s)')
    print(f'Valor total a ser pago: R${preco_total}')


def enviar_confirmacao2(pedido2,preco_total2):
    # Simula o envio de uma confirmação de pedido2
    print(f'Confirmação enviada para o {pedido2["quantidade"]} {pedido2["item"]}(s)')
    print(f'Valor total a ser pago: R${preco_total2}')

def processar_pedido():
    # Chama as funçoes auxiliares para processar o pedido
    pedido = obter_detalhes_pedido()
    preco_total = calcular_preço_total(pedido)
    enviar_confirmacao = (pedido, preco_total)

def processar_pedido2():
    # Chama as funçoes auxiliares para processar o pedido
    pedido2 = obter_detalhes_pedido()
    preco_total2 = calcular_preço_total2(pedido2)
    enviar_confirmacao2 = (pedido2, preco_total2)


# Chamando a função principal

processar_pedido()
processar_pedido2()
