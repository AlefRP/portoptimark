import yfinance as yf
import logging
import modules.markovitz as mk
import modules.multiplos as mp
import modules.indicadores as ind

# Configuração do logging
logging.basicConfig(level=logging.INFO)

class Acoes:
    def __init__(self, tickers, periodo='1y'):
        self.tickers = tickers
        self.periodo = periodo
        self.dados = None

    def baixar_dados(self):
        try:
            self.dados = yf.download(self.tickers, period=self.periodo)
        except Exception as e:
            logging.error(f"Erro ao baixar dados: {e}")
            raise

    def calcular_multiplos(self):
        multiplos_resultados = {}
        for ticker in self.tickers:
            try:
                dados_financeiros = yf.Ticker(ticker).info
                eps = dados_financeiros.get('trailingEps') or dados_financeiros.get('forwardEps')
                bvps = dados_financeiros.get('bookValue')
                preco = self.dados['Adj Close'][ticker].iloc[-1]  # Preço mais recente
                
                if eps and bvps:
                    pe = mp.calcular_pe(preco, eps)
                    pvp = mp.calcular_pvp(preco, bvps)
                else:
                    pe = pvp = None

                multiplos_resultados[ticker] = {
                    'P/L': pe,
                    'P/VP': pvp
                }
            except Exception as e:
                logging.error(f"Erro ao calcular múltiplos para {ticker}: {e}")
        return multiplos_resultados

    def analisar(self):
        if self.dados is None:
            self.baixar_dados()

        resultados = {
            'indicadores': {},
            'multiplos': self.calcular_multiplos(),
            'portfólio': None
        }

        # Análise de indicadores
        if 'Adj Close' in self.dados.columns:
            for ticker in self.tickers:
                dados_ticker = self.dados['Adj Close'][ticker]
                resultados['indicadores'][ticker] = {
                    'media_movel': ind.calcular_media_movel(dados_ticker),
                    # Outros indicadores podem ser adicionados aqui
                }

        # Otimização de portfólio
        try:
            pesos, ef = mk.otimizar_portfolio(self.tickers)
            resultados['portfólio'] = {
                'pesos': pesos,
                'eficiencia': ef
            }
        except Exception as e:
            logging.error(f"Erro durante a otimização do portfólio: {e}")
            raise

        return resultados

# Uso da classe
def main():
    tickers = ['AAPL', 'MSFT', 'GOOG']
    try:
        analisador = Acoes(tickers)
        resultados = analisador.analisar()
        logging.info(resultados)
    except Exception as e:
        logging.error(f"Erro na análise das ações: {e}")

if __name__ == "__main__":
    main()