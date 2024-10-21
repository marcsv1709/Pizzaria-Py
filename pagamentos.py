from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor):
        pass

class PagamentoCartao(Pagamento):
    def realizar_pagamento(self, valor):
        return f"Pagamento de R$ {valor} realizado com cartão."

class PagamentoDinheiro(Pagamento):
    def realizar_pagamento(self, valor):
        return f"Pagamento de R$ {valor} realizado em dinheiro."
