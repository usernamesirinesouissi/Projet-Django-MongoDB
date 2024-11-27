# gestion_bibliotheque/forms.py
from django import forms
from .models import Abonne, Document, Emprunt

class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['nom', 'prenom', 'adresse', 'date_inscription']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['titre', 'type', 'auteur', 'date_publication', 'disponibilite']

class EmpruntForm(forms.ModelForm):
    class Meta:
        model = Emprunt
        fields = ['abonne', 'document', 'date_emprunt', 'date_retour_prevue', 'statut_emprunt']
        widgets = {
            'abonne': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.Select(attrs={'class': 'form-control'}),
            'date_emprunt': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_retour_prevue': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'statut_emprunt': forms.Select(attrs={'class': 'form-control'})
        }

