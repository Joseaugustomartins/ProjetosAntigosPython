def metade(preco=0, formato=False):
    met = preco / 2
    return met if formato is False else moeda(met)


def dobro(preco=0, formato=False):
    dob = preco * 2
    return dob if formato is False else moeda(dob)


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')
