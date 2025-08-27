# meiospagamentos.py

class MeioPagamento:
    """Classe base para todos os meios de pagamento"""
    def pagar(self, valor):
        raise NotImplementedError("Método pagar deve ser implementado pela subclasse")

class CartaoCredito(MeioPagamento):
    def __init__(self, numero, titular, validade, cvv):
        self.numero = numero
        self.titular = titular
        self.validade = validade
        self.cvv = cvv
    
    def pagar(self, valor):
        print(f"💳 Processando pagamento com cartão de crédito")
        print(f"   Titular: {self.titular}")
        print(f"   Valor: R$ {valor:.2f}")
        print(f"   Transação aprovada!")
        return True

class Dinheiro(MeioPagamento):
    def __init__(self):
        pass
    
    def pagar(self, valor):
        print(f"💰 Processando pagamento em dinheiro")
        print(f"   Valor: R$ {valor:.2f}")
        print(f"   Pagamento recebido!")
        return True

class Pix(MeioPagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix
    
    def pagar(self, valor):
        print(f"📱 Processando pagamento via PIX")
        print(f"   Chave PIX: {self.chave_pix}")
        print(f"   Valor: R$ {valor:.2f}")
        print(f"   Transferência realizada com sucesso!")
        return True

class Caixa:
    def __init__(self):
        self.vendas = []
    
    def processar_pagamento(self, meio_pagamento, valor):
        print("=" * 50)
        print("🛒 INICIANDO PROCESSAMENTO DE PAGAMENTO")
        print("=" * 50)
        
        try:
            # Verifica se o meio de pagamento tem o método pagar
            if hasattr(meio_pagamento, 'pagar') and callable(getattr(meio_pagamento, 'pagar')):
                sucesso = meio_pagamento.pagar(valor)
                
                if sucesso:
                    # Registrar a venda
                    self.vendas.append({
                        'meio_pagamento': type(meio_pagamento).__name__,
                        'valor': valor,
                        'timestamp': 'agora'
                    })
                    
                    # Gerar cupom de desconto
                    self.gerar_cupom_desconto(valor)
                return sucesso
            else:
                print("❌ Erro: Meio de pagamento não possui método pagar()")
                return False
                
        except Exception as e:
            print(f"❌ Erro durante o processamento: {e}")
            return False
    
    def gerar_cupom_desconto(self, valor_compra):
        """Gera um cupom de desconto baseado no valor da compra"""
        print("-" * 50)
        print("🎫 CUPOM DE DESCONTO")
        print("-" * 50)
        
        if valor_compra > 100:
            desconto = "10% na próxima compra"
        elif valor_compra > 50:
            desconto = "5% na próxima compra"
        else:
            desconto = "R$ 5,00 off na próxima compra acima de R$ 30,00"
        
        print(f"   Valor da compra: R$ {valor_compra:.2f}")
        print(f"   Cupom gerado: {desconto}")
        print(f"   Código: CUPOM{len(self.vendas):03d}")
        print(f"   Validade: 30 dias")
        print("-" * 50)
        print("📝 Obrigado pela compra! Volte sempre!")
        print("=" * 50)
        print("\n")

# Função para testar os pagamentos
def testar_pagamentos():
    # Criar instância do caixa
    caixa = Caixa()
    
    # Criar meios de pagamento
    cartao = CartaoCredito("1234 5678 9012 3456", "Marcos Silva", "12/25", "123")
    dinheiro = Dinheiro()
    pix = Pix("marcos.silva@email.com")
    
    # Testar os pagamentos
    print("🧪 TESTANDO MEIOS DE PAGAMENTO")
    print("=" * 50)
    
    # Teste 1: Cartão de crédito
    caixa.processar_pagamento(cartao, 150.0)
    
    # Teste 2: Dinheiro
    caixa.processar_pagamento(dinheiro, 50.0)
    
    # Teste 3: PIX
    caixa.processar_pagamento(pix, 20.0)
    
    # Resumo das vendas
    print("📊 RESUMO DAS VENDAS PROCESSADAS")
    print("=" * 50)
    total_vendas = sum(venda['valor'] for venda in caixa.vendas)
    print(f"Total de vendas: {len(caixa.vendas)}")
    print(f"Valor total: R$ {total_vendas:.2f}")

# Executar testes se o arquivo for executado diretamente
if __name__ == "__main__":
    testar_pagamentos()