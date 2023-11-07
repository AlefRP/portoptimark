def calcular_media_movel(dados, periodo=50):
    return dados.rolling(window=periodo).mean()

def calcular_rsi(dados, periodo=14):
    # A implementação do RSI é um pouco mais complexa e exigirá mais código.
    pass
