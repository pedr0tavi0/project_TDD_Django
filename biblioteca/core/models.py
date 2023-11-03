from django.db import models

class LivroModel(models.Model):
    titulo = models.CharField('Título', max_length=200)
    editora = models.CharField('editora', max_length=200)
    autor = models.CharField('autor',null=True, max_length=200)
    isbn = models.CharField('isbn',null=True,  max_length=200)
    numero_paginas = models.IntegerField('numero_paginas', null=True)
    ano_publicacao = models.IntegerField('ano_publicacao',null=True)

    def __str__(self):
        return self.titulo