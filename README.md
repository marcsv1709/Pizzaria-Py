# Pizzaria - Aplicação dos Princípios SOLID
## Antes da Refatoração

### Problemas

Antes da aplicação dos princípios **SOLID**, o código apresentava as seguintes violações:

1. **Violação do SRP (Princípio da Responsabilidade Única)**:
   - A classe `Pizzaria` era responsável por muitas coisas: criar pizzas, calcular preços, processar pagamentos e gerenciar o pedido completo. Isso tornava o código confuso e difícil de manter, pois uma alteração em qualquer uma dessas funcionalidades exigiria a modificação da mesma classe.

2. **Violação do OCP (Princípio Aberto/Fechado)**:
   - Para adicionar novos tipos de pizza ou métodos de pagamento, era necessário modificar a classe `Pizzaria`. Isso viola o OCP, que afirma que classes devem estar abertas para extensão, mas fechadas para modificação.

3. **Violação do DIP (Princípio da Inversão de Dependência)**:
   - A classe `Pizzaria` dependia diretamente de implementações concretas para a criação de pizzas e para os métodos de pagamento. Isso tornava o código rígido e difícil de modificar sem alterar as dependências internas.

4. **Violação do ISP (Princípio da Segregação de Interfaces)**:
   - Todas as funcionalidades estavam agrupadas em uma única classe, sem interfaces segregadas para pizzas e métodos de pagamento. Isso tornava o código difícil de reutilizar ou modificar.

5. **Violação do LSP (Princípio da Substituição de Liskov)**:
   - O código não permitia que classes herdadas fossem substituídas facilmente sem modificar o comportamento geral do sistema.

### Código Antes do SOLID

```python
class Pizzaria:
    def fazer_pizza(self, tipo):
        if tipo == "marguerita":
            return "Pizza de marguerita feita!"
        elif tipo == "pepperoni":
            return "Pizza de pepperoni feita!"
        else:
            return "Pizza não disponível."

    def calcular_preco(self, tipo):
        if tipo == "marguerita":
            return 20.00
        elif tipo == "pepperoni":
            return 25.00
        else:
            return 0.00

    def realizar_pagamento(self, valor, metodo_pagamento):
        if metodo_pagamento == "cartao":
            return "Pagamento realizado com cartão."
        elif metodo_pagamento == "dinheiro":
            return "Pagamento realizado com dinheiro."
        else:
            return "Método de pagamento não aceito."

    def fazer_pedido(self, tipo, metodo_pagamento):
        pizza = self.fazer_pizza(tipo)
        preco = self.calcular_preco(tipo)
        
        if preco == 0:
            return "Pedido não pode ser concluído. Pizza indisponível."

        pagamento = self.realizar_pagamento(preco, metodo_pagamento)
        return f"{pizza}\n{pagamento}"
