from django.http import HttpResponse

def hello(request, nome):
    return HttpResponse("<h1>Hello!</h1>".format(nome))

def soma(request, a, b):
    resultado = a + b
    return HttpResponse(f"A soma é: {resultado}")
