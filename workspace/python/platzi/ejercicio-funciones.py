def incrementa(x):
    return x + 50


def hof(x, func):
    return x + func(x)


result = hof(20, incrementa)
# 20 + (20 + 50)
print(result)


def increment_v2(x): return x + 5
def hof_v2(x, func): return x + func(x) + func(x)


resultado = hof_v2(10, increment_v2)
#10 + (10 + 5) + (10 + 5)
print(resultado)
