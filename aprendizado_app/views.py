from django.shortcuts import render


def index(request):
    """Página inicial para aprendizado_app"""
    return render(request, 'aprendizado_app/index.html')