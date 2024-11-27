from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.home, name='home'),  # Page d'accueil
    path('dashboard/', views.dashboard, name='dashboard'),  # Page du tableau de bord
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Abonné
    path('abonne/create/', views.create_abonne, name='create_abonne'),
    path('abonne/list/', views.list_abonne, name='list_abonne'),
    path('abonne/update/<int:id>/', views.update_abonne, name='update_abonne'),
    path('abonne/delete/<int:id>/', views.delete_abonne, name='delete_abonne'),

    # Emprunt
    path('emprunt/list/', views.list_emprunt, name='list_emprunt'),
    path('emprunt/create/', views.create_emprunt, name='create_emprunt'),
    path('emprunt/update/<int:id>/', views.update_emprunt, name='update_emprunt'),
    path('emprunt/delete/<int:id>/', views.delete_emprunt, name='delete_emprunt'),

    # Document
    path('document/list/', views.list_document, name='list_document'),
    path('document/create/', views.create_document, name='create_document'),
    path('document/update/<int:id>/', views.update_document, name='update_document'),
    path('document/delete/<int:id>/', views.delete_document, name='delete_document'),
]
