# Utiliser l'image officielle Python comme image de base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de votre application dans le conteneur
COPY . /app/

# Installer les dépendances à partir du fichier requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# Exposer le port 8000 pour le serveur Django
EXPOSE 8000

# Exécuter le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
