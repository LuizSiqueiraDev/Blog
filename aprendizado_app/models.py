from django.db import models


class Topico(models.Model):
    """Um tópico sobre o qual o usuário está aprendendo."""
    texto = models.CharField(max_length=200)
    data_adicionada = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Retorna uma representação de string do modelo."""
        return self.texto


class Descricao(models.Model):
    """Algo específico aprendido sobre o tópico."""
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    texto = models.TextField()
    data_adicionada = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'descricoes'

    def __str__(self):
        """Retorna uma simples string representando a descrição."""
        if len(self.texto) > 50:
            return f"{self.texto[:50]}..."
        else:
            return self.texto
