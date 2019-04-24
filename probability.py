def peso(num, total):
    '''
    :param num: numero de aparicoes da palavra
    :param total: total de palavras nos dados
    :return: um peso baseado na formula usada pelo algoritmo word2vec
    '''
    # variavel ajustavel
    ajuste = 0.001
    return (((num/total)/ajuste)**0.5 + 1) * (ajuste/(num/total))
