def metade(preco):
    met = preco / 2
    return met


def dobro(preco):
    dob = preco * 2
    return dob


def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)