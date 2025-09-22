import math

def valida_positivo(func):
    def wrapper(*args, **kwargs):
        # print(f'[LOG] Args: {args}')
        # print(f'[LOG] Kwargs: {kwargs}')
        for arg in args:
            if arg < 0:
                raise ValueError('Parâmetro não pode ser negativo')
        
        for valor in kwargs.values():
            if valor < 0:
                raise ValueError('Parâmetro não pode ser negativo')
            
        response = func(*args, **kwargs)
        return response
    return wrapper

@valida_positivo
def raiz_quadrada(x):    
    return math.sqrt(x)

@valida_positivo
def divisao(a, b):
    return a / b


# raiz_quadrada(x=-3)
print(raiz_quadrada(x=3))

print(divisao(-1, 3))
