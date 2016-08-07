from django import forms

class SimpleSearch(forms.Form):
    search = forms.CharField(label='Your name', max_length=100)


class Search(forms.Form):
    title = forms.CharField(label='Titulo libro', max_length=100)
    author = forms.CharField(label='Autor', max_length=100)
