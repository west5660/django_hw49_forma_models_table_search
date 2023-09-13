from django import forms
from .models import *


class FormJuice(forms.Form):
    all = Company.objects.all()
    # mas = []
    # for a in all:
    #     mas.append((a.id, a.title))
    # firma = forms.ChoiceField(choices=tuple(mas))
    firma = forms.ModelChoiceField(Company.objects.all(), required=False)
    # firma = forms.ModelChoiceField(Company.objects.all(), required=False)
    sok=forms.ModelChoiceField(Product.objects.all(), required=False)

class FormStud(forms.Form):
    all = Student.objects.all()
    kurs=forms.ModelChoiceField(Course.objects.all(), required=False)
    nik=forms.ModelChoiceField(Student.objects.all(), required=False)