from django.db import models


class Topico(models.Model):
    """Um tópico sobre o qual o usuário está aprendendo."""
    texto = models.CharField(max_length=200)
    data_adicionada = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Retorna uma representação de string do modelo."""
        return self.texto

