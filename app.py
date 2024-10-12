# Nom ......... : app.py
# Rôle ........ : Application Streamlit (génération de revue de presse) + formatage
# Auteur ...... : Avrile Floro
# Version ..... : V0.3 du 01/09/2024
# Licence ..... : réalisé dans le cadre du cours de I&C & DLL (projet)

from traduction import traduction
import streamlit as st
import requests
from datetime import datetime, timedelta
from newspaper import Article
from io import BytesIO
from fpdf import FPDF
import re


# fonction pour formater le texte braille avec des espaces au début de chaque paragraphe (alinéa)
def texte_braille_pdf(texte, largeur_max, pdf):
    texte_formate = ""

    # initialisation de la 1ere ligne du paragraphe avec trois espaces (alinéa)
    ligne_actuelle = "\u2800\u2800\u2800"

    # sépare le texte du paragraphe aux espaces braille ('\u2800') --> obtient une liste de mots
    mots = texte.split('\u2800')

    for mot in mots:
        # ajoute le mot et l'espace à la ligne courante
        ligne_avec_mot = ligne_actuelle + mot + '\u2800'

        # calcule la largeur de la ligne actuelle si le mot et l'espace sont ajoutés
        largeur_ligne = pdf.get_string_width(ligne_avec_mot)

        if largeur_ligne <= largeur_max:
            # si la largeur de la ligne est dans la limite, on y ajoute le mot et l'espace
            ligne_actuelle = ligne_avec_mot
        else:
            # sinon, on ajoute la ligne au texte formaté (sans espace à la fin)
            texte_formate += ligne_actuelle.rstrip('\u2800') + '\n'
            # on commence une nouvelle ligne (sans alinéa)
            ligne_actuelle = mot + '\u2800'

    # ajoute la dernière ligne
    if ligne_actuelle:
        texte_formate += ligne_actuelle.rstrip().rstrip('\u2800')

    return texte_formate


##### Application Streamlit

st.title("Générateur de Revue de Presse")  # titre de l'interface Streamlit

duree = st.selectbox(  # sélection de la durée
    "Récupérer des articles publiés...",
    options=["depuis hier", "depuis 7 jours", "depuis 30 jours"], )

date_fin = datetime.today()  # jusqu'à date du jour

if duree == "depuis hier":  # date de début selon la durée choisie
    date_debut = date_fin - timedelta(days=1)
elif duree == "depuis 7 jours":
    date_debut = date_fin - timedelta(days=7)
elif duree == "depuis 30 jours":
    date_debut = date_fin - timedelta(days=30)

langue = st.radio(  # choix de la langue
    "Sélectionnez la langue de génération",
    options=["Français", "Braille"])

if st.button("Générer la revue de presse"):  # bouton pour générer la revue de presse
    if duree and langue:  # il faut avoir choisi les options
        #api_key = st.secrets["api_key"]  # clé de l'API dans le fichier secret de Streamlit
        api_key = "03085edf113f4403811720f6a880423e"

        # les paramètres pour les 4 appels de l'API
        params_usine = {  # Usine Digitale
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "usine-digitale.fr",
            "apiKey": api_key, }

        params_france_info = {  # France Info
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "francetvinfo.fr",
            "apiKey": api_key, }

        params_huffpost = {  # Huffington Post
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "huffingtonpost.fr",
            "apiKey": api_key, }

        params_journaldunet = {  # Journal du Net
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "journaldunet.com",
            "apiKey": api_key, }

        articles = []  # pour stocker les articles
        # appelle l'API pour les 4 sources souhaitées
        for param in [params_usine, params_france_info, params_huffpost, params_journaldunet]:
            try:
                # envoi la requête GET à l'API
                response = requests.get("https://newsapi.org/v2/everything", params=param)
                # ajout des art obtenus à liste articles avec extends (sous forme de dico)
                articles.extend(response.json().get("articles", []))
            except Exception as e:
                print(f"Erreur lors de la récupération des articles : {e}")

        # crée une str avec le contenu des articles, s'ils ont été récupérés
        if articles:
            sortie = ""  # str vide initialisée pour la sortie
            for index, art in enumerate(articles):  # boucle avec index pour suivre la position
                article_url = art['url']  # récupère l'URL
                try:
                    # utilise Newspaper pour récupérer le contenu de l'article
                    article_news = Article(article_url)  # initialisation avec url
                    article_news.download()  # téléchargement, obligatoire pour...
                    article_news.parse()  # parser l'article
                    contenu = article_news.text  # extrait le texte intégral de l'article
                    date_publication = datetime.strptime(art['publishedAt'],
                                                         "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y")
                    # renvoie juste la date de publication

                    dernier_art = (index == len(articles) - 1)  # vérifie si c'est le dernier
                    # élément

                    if langue == "Français":  # si la revue de presse est en français
                        contenu = re.sub(r'\n{3,}', '\n\n', contenu)
                        sortie += (
                            f"Titre : {art['title']}\n"  # titre
                            f"Source : {art['source']['name']}\n"  # source
                            f"Publié le : {date_publication}\n\n"  # date 
                            f"{contenu}\n\n")  # contenu
                        # séparation seulement si ce n'est pas le dernier
                        if not dernier_art:
                            sortie += "------------------------------\n\n"

                    else:  # si c'est en braille
                        contenu = re.sub(r'\n{3,}', '\n\n', contenu)
                        sortie += (
                            f"⠨⠞⠊⠞⠗⠑⠒ {traduction(art['title'])}\n"  # titre
                            f"\n\n"
                            f"\u2800\u2800\u2800⠨⠎⠕⠥⠗⠉⠑⠒ {traduction(art['source']['name'])}\n\n"  # source
                            f"⠨⠏⠥⠃⠇⠊⠿ ⠇⠑⠒ {traduction(date_publication)}\n\n"  # date 
                            f"{traduction(contenu)}\n")  # contenu
                        # séparation en braille seulement si ce n'est pas le dernier
                        if not dernier_art:
                            sortie += "⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶\n\n\n"

                except Exception as e:
                    print(f"Erreur lors du traitement de l'article : {e}")

            if sortie:  # si la sortie n'est pas vide
                font_path = "fonts/DejaVuSans.ttf"  # dossier contenant DejaVuSans
                pdf = FPDF()  # créer un objet PDF
                pdf.add_page()  # on y ajoute page
                # utilisation de la police DejaVu supportant les caractères brailles
                pdf.add_font('DejaVu', '', font_path, uni=True)

                # traitement du contenu paragraphe par paragraphe pour l'ajout au PDF
                for para in sortie.split("\n\n"):  # pour chaque paragraphe
                    if langue == "Braille":
                        pdf.set_font('DejaVu', '', 18)  # taille plus grand
                        # ajuste le texte pour le braille et ajoute au pdf
                        para_br = texte_braille_pdf(para, 190, pdf)
                        pdf.multi_cell(0, 12, para_br)
                        pdf.ln(1)  # saut de ligne
                    else:   # pour le français
                        pdf.set_font('DejaVu', '', 12)
                        pdf.multi_cell(0, 10, para)
                        pdf.ln()  # saut de ligne

                # buffer pour stocker le fichier PDF
                buffer = BytesIO()
                pdf_data = pdf.output(dest='S').encode('latin1')  # 'S' : contenu sous forme de str
                buffer.write(pdf_data)
                buffer.seek(0)  # retour au début du buffer

                st.download_button(  # bouton pour télécharger le PDF
                    label="Télécharger en PDF",
                    data=buffer,
                    file_name="revueDePresse.pdf",
                    mime="application/pdf"
                )

        # si aucun article n'a été récupéré (les articles de la veille ne sont pas publiés)
        if not articles and duree == "depuis hier":
            st.error(
                "Les articles de la veille ne sont pas encore disponibles en raison"
                " d'un décalage de 24h entre leur publication et leur mise en ligne "
                "sur l'API. Veuillez choisir une durée plus longue s'il vous plaît.")

    else:
        st.error("Veuillez remplir tous les champs avant de générer la revue de presse.")





