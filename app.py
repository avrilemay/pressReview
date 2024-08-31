# Nom ......... : app.py
# Rôle ........ : Application Streamlit (génération de revue de presse)
# Auteur ...... : Avrile Floro
# Version ..... : V0.2 du 28/08/2024
# Licence ..... : réalisé dans le cadre du cours de I&C (projet)

from traduction import traduction
import streamlit as st
import requests
from datetime import datetime, timedelta
from newspaper import Article
from io import BytesIO
from fpdf import FPDF
import re


# fonction pour formater le texte braille (espaces aux '\u2800')
def texte_braille_pdf(texte, largeur_max, pdf):
    texte_formate = "\u2800\u2800\u2800"

    # sépare le texte aux espaces braille ('\u2800') pour obtenir une liste de mots
    mots = texte.split('\u2800')
    ligne_actuelle = ""

    for mot in mots:
        # ajoute le mot à la ligne courante
        ligne_avec_mot = ligne_actuelle + mot

        # calcule la largeur de la ligne actuelle si le mot est ajouté
        largeur_ligne = pdf.get_string_width(ligne_avec_mot)

        if largeur_ligne <= largeur_max:
            # si la largeur de la ligne est dans la limite, on y ajoute le mot
            ligne_actuelle = ligne_avec_mot + '\u2800'  # on ajoute l'espace braille
        else:
            # sinon, on ajoute la ligne au texte formaté et on commence une nouvelle ligne
            texte_formate += ligne_actuelle.rstrip() + '\n'
            ligne_actuelle = mot + '\u2800'  # nouvelle ligne avec le mot

    # ajoute la dernière ligne
    if ligne_actuelle:
        texte_formate += ligne_actuelle.rstrip()

    return texte_formate



st.title("Générateur de Revue de Presse")  # titre de l'interface Streamlit

duree = st.selectbox(  # sélection de la durée
    "Récupérer des articles publiés...",
    options=["depuis hier", "depuis 7 jours", "depuis 30 jours"],
)

date_fin = datetime.today()  # jusqu'à date du jour

if duree == "depuis hier":  # date de début selon la durée choisie
    date_debut = date_fin - timedelta(days=1)
elif duree == "depuis 7 jours":
    date_debut = date_fin - timedelta(days=7)
elif duree == "depuis 30 jours":
    date_debut = date_fin - timedelta(days=30)


langue = st.radio(  # choix de la langue
    "Sélectionnez la langue de génération",
    options=["Français", "Braille"]
)


if st.button("Générer la revue de presse"):     # bouton pour générer la revue de presse
    if duree and langue:    # il faut avoir choisi les options
        api_key = st.secrets["api_key"]    # clé de l'API dans le fichier secret de Streamlti

        # les paramètres pour les 4 appels de l'API
        params_usine = {    # Usine Digitale
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "usine-digitale.fr",
            "apiKey": api_key,
        }

        params_france_info = {  # France Info
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "francetvinfo.fr",
            "apiKey": api_key,
        }

        params_huffpost = {     # Huffington Post
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "huffingtonpost.fr",
            "apiKey": api_key,
        }

        params_journaldunet = {     # Journal du Net
            "q": "",
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 1,
            "domains": "journaldunet.com",
            "apiKey": api_key,
        }

        articles = []   # pour stocker les articles
        # appelle l'API pour les 4 sources souhaitées
        for param in [params_usine, params_france_info, params_huffpost, params_journaldunet]:
            try:
                # envoi la requête GET à l'API
                response = requests.get("https://newsapi.org/v2/everything", params=param)
                # ajout des art obtenus à liste articles avec extends
                articles.extend(response.json().get("articles", []))
            except Exception as e:
                st.error(f"Erreur lors de la récupération des articles : {e}")

        # crée un doc avec le contenu des articles, s'ils ont été récupérés
        if articles:
            sortie = "" # str vide initialisée pour la sortie
            for article in articles: # boucle et récupère l'URL de chaque article
                article_url = article['url']
                try:
                    # utilise Newspaper pour récupérer le contenu de l'article
                    article_news = Article(article_url)
                    article_news.download()
                    article_news.parse()
                    contenu = article_news.text  # extrait le texte intégral de l'article


                        # remplace trois sauts de ligne ou plus par deux
                    if langue == "Français":    # si la revue de presse est en français
                        sortie += (f"Titre : {article['title']}\nSource : "
                                   f"{article['source']['name']}\nPublié le : "
                                   f"{article['publishedAt']}\nURL : {article['url']}\n\n"
                                   f"{contenu}\n\n"
                                   f"------------------------------\n\n")
                    else:   # si c'est en braille
                        contenu = re.sub(r'\n{3,}', '\n\n', contenu)
                        sortie += (f"\n\n\n⠨⠞⠊⠞⠗⠑⠒ {traduction(article['title'])}\n\n\t⠨⠎⠕⠥⠗⠉⠑⠒ "
                                   f"{traduction(article['source']['name'])}\n\t⠨⠏⠥⠃⠇⠊⠿ ⠇⠑⠒ "
                                   f"{traduction(article['publishedAt'])}\n\t⠨⠥⠗⠇⠒ "
                                   f"{traduction(article['url'])}\n\t"
                                   f"{traduction(contenu)}\n"
                                   f"⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶")
                except Exception as e:
                    st.error(f"Erreur lors de la récupération de l'article : {e}")

            if sortie:  # si la sortie n'est pas vide

                # Chemin vers le dossier contenant les polices
                font_path = "fonts/DejaVuSans.ttf"

                pdf = FPDF()    # créer un PDF
                pdf.add_page()    # y ajoute page

                # utilisation de la police DejaVu supportant les caractères brailles
                pdf.add_font('DejaVu', '', font_path, uni=True)

                # traitement du contenu paragraphe par paragraphe pour l'ajout au PDF
                # Nettoyer `sortie` pour ne garder que des \n\n maximum
                for para in sortie.split("\n\n"):  # pour chaque ligne au sein des paragraphes
                    if langue == "Braille":
                        # para = para.strip()  # supprime les sauts de ligne
                        pdf.set_font('DejaVu', '', 15)  # taille plus grand
                        # ajuste le texte pour le braille et ajoute au pdf
                        lignes_brailles = texte_braille_pdf(para, 180, pdf)
                        pdf.multi_cell(0, 12, lignes_brailles)
                        pdf.ln(1)  # saut de ligne
                    else:
                        pdf.set_font('DejaVu', '', 12)
                        pdf.multi_cell(0, 10, para)
                        pdf.ln(5)  # saut de ligne


                # buffer pour stocker le fichier PDF
                buffer = BytesIO()
                pdf_data = pdf.output(dest='S').encode('latin1')  # 'S' : contenu sous forme de str
                buffer.write(pdf_data)
                buffer.seek(0)  # retour au début du buffer

                st.download_button(     # bouton pour télécharger le PDF
                    label="Télécharger en PDF",
                    data=buffer,
                    file_name="revueDePresse.pdf",
                    mime="application/pdf"
                )

    else:
        st.error("Veuillez remplir tous les champs avant de générer la revue de presse.")
