def multiIter(lista, n):
    '''
    :param lista: a list of strings
    :param n: how many objects will return
                    before and after any element
    :return: 'context' is a tuple of the element plus its n-neighbors AND the element index
    '''
    for i in range(len(lista)):
        context = []
        before = n
        index = 0
        while before:
            if i - before >= 0:
                context.append(lista[i-before])
                index += 1
            before -= 1
        context.append(lista[i])
        after = 1
        while after <= n:
            if i + after < len(lista):
                context.append(lista[i+after])
            after += 1
        yield [tuple(context), index]
