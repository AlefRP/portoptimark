# Este módulo irá lidar com a otimização de portfólio usando o modelo de Markowitz.
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns
import yfinance as yf

def otimizar_portfolio(tickers, period='1y'):
    # Obtém os retornos esperados e a matriz de covariância do portfólio
    dados = yf.download(tickers, period=period)['Adj Close']
    retornos_esperados = expected_returns.mean_historical_return(dados)
    matriz_covariancia = risk_models.sample_cov(dados)

    # Calcula a fronteira eficiente
    ef = EfficientFrontier(retornos_esperados, matriz_covariancia)
    pesos = ef.max_sharpe()
    ef.portfolio_performance(verbose=True)

    return pesos, ef