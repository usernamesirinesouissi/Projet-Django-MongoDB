from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Abonne, Document, Emprunt
from .forms import AbonneForm, DocumentForm, EmpruntForm  
from django.db.models import Q

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import logout




# Vues pour Abonne
def list_abonne(request):
    query = request.GET.get('q', '')  # Récupère la requête de recherche
    abonnes = Abonne.objects.filter(nom__icontains=query) if query else Abonne.objects.all()
    return render(request, 'abonnee/listabonnee.html', {'abonnes': abonnes, 'query': query})


def create_abonne(request):
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_abonne')  
    else:
        form = AbonneForm()
    return render(request, 'abonnee/createabonnee.html', {'form': form})

def update_abonne(request, id):
    abonne = get_object_or_404(Abonne, id=id) 
    if request.method == 'POST':
        form = AbonneForm(request.POST, instance=abonne)
        if form.is_valid():
            form.save()
            return redirect('list_abonne')  
    else:
        form = AbonneForm(instance=abonne)
    return render(request, 'abonnee/updateabonnee.html', {'form': form, 'abonne': abonne})

def delete_abonne(request, id):
    abonne = get_object_or_404(Abonne, id=id) 
    if request.method == 'POST':
        abonne.delete()  
        return redirect('list_abonne')  
    return render(request, 'abonnee/deleteabonnee.html', {'abonne': abonne})

# Vues pour Document
def list_document(request):
    query = request.GET.get('q', '')
    if query:
        documents = Document.objects.filter(
            Q(titre__icontains=query) |
            Q(auteur__icontains=query) |
            Q(type__icontains=query)
        )
    else:
        documents = Document.objects.all()
    return render(request, 'documents/listdocument.html', {'documents': documents, 'query': query})

def create_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_document')  
    else:
        form = DocumentForm()
    return render(request, 'documents/createdocument.html', {'form': form})

def update_document(request, id):
    document = get_object_or_404(Document, id=id)  
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('list_document')  
    else:
        form = DocumentForm(instance=document)
    return render(request, 'documents/updatedocument.html', {'form': form})

def delete_document(request, id):
    document = get_object_or_404(Document, id=id)  
    if request.method == 'POST':
        document.delete()  
        return redirect('list_document')  
    return render(request, 'documents/deletedocument.html', {'document': document})

# Vues pour Emprunt
def list_emprunt(request):
    query = request.GET.get('q', '')
    if query:
        emprunts = Emprunt.objects.filter(
            Q(abonne__nom__icontains=query) |
            Q(abonne__prenom__icontains=query) |
            Q(document__titre__icontains=query) |
            Q(statut_emprunt__icontains=query)
        )
    else:
        emprunts = Emprunt.objects.all()
    return render(request, 'emprunts/listemp.html', {'emprunts': emprunts, 'query': query})


def create_emprunt(request):
    if request.method == 'POST':
        form = EmpruntForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('list_emprunt')  
    else:
        form = EmpruntForm()
    
    return render(request, 'emprunts/createemp.html', {'form': form})

def update_emprunt(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)  
    if request.method == 'POST':
        form = EmpruntForm(request.POST, instance=emprunt)
        if form.is_valid():
            form.save()
            return redirect('list_emprunt')  
    else:
        form = EmpruntForm(instance=emprunt)
    return render(request, 'emprunts/updateemp.html', {'form': form})

def delete_emprunt(request, id):
    emprunt = get_object_or_404(Emprunt, id=id)  
    if request.method == 'POST':
        emprunt.delete() 
        return redirect('list_emprunt')  
    return render(request, 'emprunts/deleteemp.html', {'emprunt': emprunt})


def dashboard(request):
   
    count_abonne = Abonne.objects.count()
    count_document = Document.objects.count()
    count_emprunt = Emprunt.objects.count()

    
    return render(request, 'dashboard.html', {
        'count_abonne': count_abonne,
        'count_document': count_document,
        'count_emprunt': count_emprunt,
    })

def home(request):
    return render(request, 'Home.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Récupère le champ 'username'
        password = request.POST.get('password')  # Récupère le champ 'password'

        # Vérification des champs vides
        if not username or not password:
            messages.error(request, "Veuillez remplir tous les champs.")
            return render(request, 'Login.html')

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')  # Redirige vers 'next' ou la page 'dashboard'
            return redirect(next_url)
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return render(request, 'Login.html')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home') 