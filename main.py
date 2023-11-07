import yfinance as yf
import modules.markovitz as mk
import modules.multiplos as mp
import modules.indicadores as ind

class AnalisadorDeAcoes:
    def __init__(self, tickers):
        self.tickers = tickers
        self.dados = None

    def baixar_dados(self):
        self.dados = yf.download(self.tickers, period='1y')

    def analisar(self):
        if self.dados is None:
            self.baixar_dados()

        # Análise de indicadores
        for ticker in self.tickers:
            dados_ticker = self.dados['Adj Close'][ticker]
            print(f"Média Móvel de {ticker}: ", ind.calcular_media_movel(dados_ticker))
            # Incluir mais chamadas de cálculos de indicadores conforme necessário

        # Cálculo de múltiplos
        # Isso exigiria dados adicionais que você precisaria fornecer ou obter de outra fonte

        # Otimização de portfólio
        pesos, ef = mk.otimizar_portfolio(self.tickers)
        return pesos, ef

# Uso da classe
def main():
    tickers = ['AAPL', 'MSFT', 'GOOG']
    analisador = AnalisadorDeAcoes(tickers)
    pesos, eficiencia = analisador.analisar()

if __name__ == "__main__":
    main()