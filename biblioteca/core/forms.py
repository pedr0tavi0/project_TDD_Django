from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel

def validate_title(value):
    if len(value) < 3:
        raise ValidationError('Deve ter pelo menos três caracteres')

def validate_autor(value):
    if len(value) < 10:
        raise ValidationError('Deve ter pelo menos dez caracteres')

def validate_isbn(value):
    if len(value) != 13 or not value.isdigit():
        raise ValidationError('O campo de ISBN deve ter exatos treze caracteres e todos números')

def validate_numero_paginas(value):
    if value < 1 or value > 999:
        raise ValidationError('O campo de número de páginas deve estar entre 1 e 999')

def validate_ano_publicacao(value):
    value_str = str(value)  # Convert to string
    if len(value_str) != 4 or not value_str.isdigit():
        raise ValidationError('O campo de ano de publicacao deve ter exatos quatro caracteres e todos números')

class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'numero_paginas', 'ano_publicacao']
        error_messages = {
            'titulo': {
                'required': ("Informe o título do livro."),
            },
            'editora': {
                'required': ("Informe a editora do livro."),
            },
            'autor': {
                'required': ("Informe o autor do livro."),
            },
            'isbn': {
                'required': ("Informe o ISBN do livro."),
            },
            'numero_paginas': {
                'required': ("Informe o número de páginas do livro."),
            },
            'ano_publicacao': {
                'required': ("Informe o ano de publicação do livro."),
            },
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora

    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn

    def clean_numero_paginas(self):
        numero_paginas = self.cleaned_data['numero_paginas']
        validate_numero_paginas(numero_paginas)
        return numero_paginas

    def clean_ano_publicacao(self):
        ano_publicacao = self.cleaned_data['ano_publicacao']
        validate_ano_publicacao(ano_publicacao)
        return ano_publicacao

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data