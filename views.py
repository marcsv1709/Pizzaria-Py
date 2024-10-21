from pizzas import MargueritaPizza, PepperoniPizza
from pagamentos import PagamentoCartao, PagamentoDinheiro

def criar_pedido(tipo_pizza, metodo_pagamento):
    if tipo_pizza == "marguerita":
        pizza = MargueritaPizza()
    elif tipo_pizza == "pepperoni":
        pizza = PepperoniPizza()
    else:
        return "Pizza não disponível."

    if metodo_pagamento == "cartao":
        pagamento = PagamentoCartao()
    elif metodo_pagamento == "dinheiro":
        pagamento = PagamentoDinheiro()
    else:
        return "Método de pagamento não aceito."

    pizza_pronta = pizza.fazer_pizza()
    preco = pizza.calcular_preco()
    pagamento_confirmado = pagamento.realizar_pagamento(preco)

    return f"{pizza_pronta}\n{pagamento_confirmado}"
