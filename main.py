import yfinance as yf
import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns

def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetches historical stock data for given tickers within the provided date range.
    """
    prices = pd.DataFrame()
    for ticker in tickers:
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            prices[ticker] = data['Adj Close']
        except Exception as e:
            print(f"Error fetching data for {ticker}: {str(e)}")
    return prices

def calculate_metrics(prices):
    """
    Calculates expected returns and sample covariance from historical stock prices.
    """
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)
    return mu, S

def optimize_portfolio(mu, S):
    """
    Optimizes the portfolio for maximal Sharpe ratio while ensuring a minimum weight of 5% for any asset.
    """
    ef = EfficientFrontier(mu, S)
    ef.add_constraint(lambda w: w >= 0.05)
    weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    return cleaned_weights, ef

def main():
    # Define the stocks and analysis period
    tickers = ['DIS', 'VZ', 'PFE', 'QCOM', 'FCNCA', 'BRK-B']
    start_date = '2010-01-01'
    end_date = '2023-10-10'
    
    # Fetch stock data, calculate metrics, and optimize the portfolio
    prices = fetch_stock_data(tickers, start_date, end_date)
    mu, S = calculate_metrics(prices)
    cleaned_weights, ef = optimize_portfolio(mu, S)
    
    # Display expected portfolio performance and weights
    ef.portfolio_performance(verbose=True)
    print(cleaned_weights)

if __name__ == "__main__":
    main()