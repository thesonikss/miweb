def filter_by_length(words):
    filtro = list(filter(lambda x: len(x) >= 4, words))
    return filtro


words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)
