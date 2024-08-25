# Générateur de Newsletter en français et Braille

## Description

Ce projet est une application Streamlit déployée qui permet de générer une newsletter à partir d'articles populaires en français. L'utilisateur peut sélectionner une période, un mot-clé, et une langue (français ou Braille) pour générer et télécharger la newsletter sous forme de fichier PDF.

L'application utilise l'API de NewsAPI pour récupérer les articles, la bibliothèque Newspaper pour extraire le contenu complet des articles, et une fonction de traduction pour convertir le texte en Braille si nécessaire.

## Fonctionnalités

- **Sélection de la période** : Choisissez de récupérer les articles publiés depuis hier, les 7 derniers jours, ou les 30 derniers jours.
- **Mot-clé** : Filtrez les articles en fonction de mots-clés spécifiques (technologie, culture, France, politique, international).
- **Langue** : Sélectionnez la langue de génération de la newsletter (Français ou Braille).
- **Téléchargement** : Téléchargez la newsletter générée au format PDF.

## Utilisation

L'application est disponible en ligne via une instance Streamlit déployée. Pour l'utiliser :

1. Accédez à l'application en suivant ce lien : 
2. Sélectionnez la période, le mot-clé et la langue souhaitée.
3. Cliquez sur "Générer la newsletter".
4. Téléchargez le fichier PDF généré.

## Dépendances

- `streamlit` : Pour créer l'interface utilisateur.
- `requests` : Pour interagir avec l'API de NewsAPI.
- `newspaper` : Pour extraire le contenu des articles.
- `fpdf` : Pour générer des fichiers PDF.

## License

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
