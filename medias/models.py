from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    nota1 = models.DecimalField(max_digits=4, decimal_places=2)
    nota2 = models.DecimalField(max_digits=4, decimal_places=2)
    nota3 = models.DecimalField(max_digits=4, decimal_places=2)

    def getMedia(self):
        media = round(((self.nota1+self.nota2+self.nota3)/3), 1)
        return media