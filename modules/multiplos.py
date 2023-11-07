def calcular_pl(preco, lucro_por_acao):
    """
    Calcula o múltiplo Preço/Lucro (P/L) de uma ação.

    :param preco: O preço atual da ação.
    :param lucro_por_acao: O lucro por ação (EPS - Earnings Per Share) da empresa.
    :return: O múltiplo P/L da ação.
    :raises ValueError: Se o lucro por ação for menor ou igual a zero.
    """
    if lucro_por_acao <= 0:
        raise ValueError("O lucro por ação deve ser maior que zero.")
    return preco / lucro_por_acao

def calcular_pvp(preco, valor_patrimonial_por_acao):
    """
    Calcula o múltiplo Preço/Valor Patrimonial (P/VP) de uma ação.

    :param preco: O preço atual da ação.
    :param valor_patrimonial_por_acao: O valor patrimonial por ação da empresa.
    :return: O múltiplo P/VP da ação.
    :raises ValueError: Se o valor patrimonial por ação for menor ou igual a zero.
    """
    if valor_patrimonial_por_acao <= 0:
        raise ValueError("O valor patrimonial por ação deve ser maior que zero.")
    return preco / valor_patrimonial_por_acao