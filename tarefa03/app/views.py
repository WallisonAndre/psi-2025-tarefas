from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'app/index.html')

def usuarios(request):
    lista = [
        {"nome": "Ana Lima", "matricula": "202301", "idade": 20, "cidade": "Natal"},
        {"nome": "Carlos Souza", "matricula": "202302", "idade": 22, "cidade": "Mossoró"},
        {"nome": "Juliana Melo", "matricula": "202303", "idade": 19, "cidade": "Caicó"},
        {"nome": "Roberto Dias", "matricula": "202304", "idade": 21, "cidade": "Parnamirim"},
        {"nome": "Fernanda Costa", "matricula": "202305", "idade": 23, "cidade": "Currais Novos"},
    ]
    return render(request, 'app/usuarios.html', {'usuarios': lista})

