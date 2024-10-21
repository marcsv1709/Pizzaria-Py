from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def fazer_pizza(self):
        pass

    @abstractmethod
    def calcular_preco(self):
        pass

class MargueritaPizza(Pizza):
    def fazer_pizza(self):
        return "Pizza de marguerita feita!"
    
    def calcular_preco(self):
        return 20.00

class PepperoniPizza(Pizza):
    def fazer_pizza(self):
        return "Pizza de pepperoni feita!"
    
    def calcular_preco(self):
        return 25.00
