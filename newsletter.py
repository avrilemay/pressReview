import streamlit as st
import requests
from datetime import datetime, timedelta
from newspaper import Article
from docx import Document
from io import BytesIO
from fpdf import FPDF


braille_symbols = {

    # l'alphabet + signes propres au français
    ' ': '\u2800',  #   (0) espace
    **dict.fromkeys(['a', 'A'], '\u2801'),  # ⠁ (1) lettre a, A
    **dict.fromkeys(['b', 'B'], '\u2803'),  # ⠃ (1-2) lettre b, B
    **dict.fromkeys(['c', 'C'], '\u2809'),  # ⠉ (1-4) lettre c, C
    **dict.fromkeys(['d', 'D'], '\u2819'),  # ⠙ (1-4-5) lettre d, D
    **dict.fromkeys(['e', 'E'], '\u2811'),  # ⠑ (1-5) lettre e, E
    **dict.fromkeys(['f', 'F'], '\u280B'),  # ⠋ (1-2-4) lettre f, F
    **dict.fromkeys(['g', 'G'], '\u281B'),  # ⠛ (1-2-4-5) lettre g, G
    **dict.fromkeys(['h', 'H'], '\u2813'),  # ⠓ (1-2-5) lettre h, H
    **dict.fromkeys(['i', 'I'], '\u280A'),  # ⠊ (2-4) lettre i, I
    **dict.fromkeys(['j', 'J'], '\u281A'),  # ⠚ (2-4-5) lettre j, J
    **dict.fromkeys(['k', 'K'], '\u2805'),  # ⠅ (1-3) lettre k, K
    **dict.fromkeys(['l', 'L'], '\u2807'),  # ⠇ (1-2-3) lettre l, L
    **dict.fromkeys(['m', 'M'], '\u280D'),  # ⠍ (1-3-4) lettre m, M
    **dict.fromkeys(['n', 'N'], '\u281D'),  # ⠝ (1-3-4-5) lettre n, N
    **dict.fromkeys(['o', 'O'], '\u2815'),  # ⠕ (1-3-5) lettre o, O
    **dict.fromkeys(['p', 'P'], '\u280F'),  # ⠏ (1-2-3-4) lettre p, P
    **dict.fromkeys(['q', 'Q'], '\u281F'),  # ⠟ (1-2-3-4-5) lettre q, Q
    **dict.fromkeys(['r', 'R'], '\u2817'),  # ⠗ (1-2-3-5) lettre r, R
    **dict.fromkeys(['s', 'S'], '\u280E'),  # ⠎ (2-3-4) lettre s, S
    **dict.fromkeys(['t', 'T'], '\u281E'),  # ⠞ (2-3-4-5) lettre t, T
    **dict.fromkeys(['u', 'U'], '\u2825'),  # ⠥ (1-3-6) lettre u, U
    **dict.fromkeys(['v', 'V'], '\u2827'),  # ⠧ (1-2-3-6) lettre v, V
    **dict.fromkeys(['w', 'W'], '\u283A'),  # ⠺ (2-4-5-6) lettre w, W
    **dict.fromkeys(['x', 'X'], '\u282D'),  # ⠭ (1-3-4-6) lettre x, X
    **dict.fromkeys(['y', 'Y'], '\u283D'),  # ⠽ (1-3-4-5-6) lettre y, Y
    **dict.fromkeys(['z', 'Z'], '\u2835'),  # ⠵ (1-3-5-6) lettre z, Z
    **dict.fromkeys(['ç', 'Ç'], '\u282F'),  # ⠯ (1-2-3-4-6) c cédille
    **dict.fromkeys(['é', 'É'], '\u283F'),  # ⠿ (1-2-3-4-5-6) e accent aigu
    **dict.fromkeys(['à', 'À'], '\u2837'),  # ⠷ (1-2-3-5-6) a accent grave
    **dict.fromkeys(['è', 'È'], '\u282E'),  # ⠮ (2-3-4-6) e accent grave
    **dict.fromkeys(['ù', 'Ù'], '\u283E'),  # ⠾ (2-3-4-5-6) u accent grave
    **dict.fromkeys(['â', 'Â'], '\u2821'),  # ⠡ (1-6) a accent circonflexe
    **dict.fromkeys(['ê', 'Ê'], '\u2823'),  # ⠣ (1-2-6) e accent circonflexe
    **dict.fromkeys(['î', 'Î'], '\u2829'),  # ⠩ (1-4-6) i accent circonflexe
    **dict.fromkeys(['ô', 'Ô'], '\u2839'),  # ⠹ (1-4-5-6) o accent circonflexe
    **dict.fromkeys(['û', 'Û'], '\u2831'),  # ⠱ (1-5-6) u accent circonflexe
    **dict.fromkeys(['ë', 'Ë'], '\u282B'),  # ⠫ (1-2-4-6) e tréma
    **dict.fromkeys(['ï', 'Ï'], '\u283B'),  # ⠻ (1-2-4-5-6) i tréma
    **dict.fromkeys(['ü', 'Ü'], '\u2833'),  # ⠳ (1-2-5-6) u tréma
    **dict.fromkeys(['œ', 'Œ'], '\u282A'),  # ⠪ (2-4-6) oe ligaturé
    ',': '\u2802',  # ⠂ (2) virgule
    ';': '\u2806',  # ⠆ (2-3) point-virgule
    ':': '\u2812',  # ⠒ (2-5) deux-points
    '.': '\u2832',  # ⠲ (2-5-6) point
    '!': '\u2816',  # ⠖ (2-3-5) point d'exclamation
    '?': '\u2822',  # ⠢ (2-6) point d'interrogation
    '-': '\u2824',  # ⠤ (3-6) trait d'union
    '(': '\u2826',  # ⠦ (2-3-6) parenthèse ouvrante
    ')': '\u2834',  # ⠴ (3-5-6) parenthèse fermante
    **dict.fromkeys(["'", '’'], '\u2804'),  # ⠄ (3) apostrophe ou espace entre les chiffres
    '/': '\u280C',  # ⠌ (3-4) barre oblique
    '@': '\u281C',  # ⠜ (3-4-5) arobas, a commercial
    **dict.fromkeys(['"', '«', '“', '»', '”'], '\u2836'),  # ⠶ (2-3-5-6) guillemet ouvrant ou
    # fermant

    # chiffres et signes arithmétiques de base
    '1': '\u2821',  # ⠡ (1-6) un 1
    '2': '\u2823',  # ⠣ (1-2-6) deux 2
    '3': '\u2829',  # ⠩ (1-4-6) trois 3
    '4': '\u2839',  # ⠹ (1-4-5-6) quatre 4
    '5': '\u2831',  # ⠱ (1-5-6) cinq 5
    '6': '\u282B',  # ⠫ (1-2-4-6) six 6
    '7': '\u283B',  # ⠯ (1-2-4-5-6) sept 7
    '8': '\u2833',  # ⠳ (1-2-5-6) huit 8
    '9': '\u282A',  # ⠪ (2-4-6) neuf 9
    '0': '\u283C',  # ⠼ (3-4-5-6) zéro 0
    '+': '\u2816',  # ⠖ (2-3-5) plus +
    '-': '\u2824',  # ⠤ (3-6) moins -
    '×': '\u2814',  # ⠔ (3-5) multiplié par ×
    '÷': '\u2812',  # ⠒ (2-5) divisé par ÷
    '=': '\u2836',  # ⠶ (2-3-5-6) égale =
    '_': '\u2822',  # ⠢ (2-6) indicateur d’indice inférieur

    '☐': '\u282f\u283d',  # ⠯⠽  (1-2-3-4-6, 1-3-4-5-6) case à cocher
    '•': '\u282a\u2815',  # ⠪⠕ (2-4-6, 1-3-5) puce
    '↔': '\u282A\u2812\u2815',  # ⠪⠒⠕ (2-4-6, 2-5, 1-3-5) flèche bidirectionnelle
    '←': '\u282a\u2812\u2812',  # ⠪⠒⠒ (2-4-6, 2-5, 2-5) flèche vers la gauche
    '→': '\u2812\u2812\u2815',  # ⠒⠒⠕ (2-5, 2-5, 1-3-5) flèche vers la droite
    '…': '\u2832\u2832\u2832',  # ⠲⠲⠲ (2-5-6, 2-5-6, 2-5-6) points de suspension
    '–': '\u2824\u2824',  # ⠤⠤ (3-6, 3-6)  tiret
    '¢': '\u2818\u2809',  # ⠘⠉ (4-5, 1-4) cent
    '€': '\u2818\u2811',  # ⠘⠑ (4-5, 1-5)  euro
    '£': '\u2818\u2807',  # ⠘⠇ (4-5, 1-2-3)  livre
    'µ': '\u2818\u280D',  # ⠘⠍ (4-5, 1-3-4)  mu
    'π': '\u2818\u280F',  # ⠘⠏ (4-5, 1-2-3-4) pi
    '$': '\u2818\u280E',  # ⠘⠎ (4-5, 2-3-4)  dollar
    '¥': '\u2818\u283D',  # ⠘⠽ (4-5, 1-3-4-5-6) yen
    '≤': '\u2818\u2823',  # ⠘⠣ (4-5, 1-2-6) inférieur ou égal
    '≥': '\u2818\u281C',  # ⠘⠜ (4-5, 3-4-5) supérieur ou égal
    '[': '\u2818\u2826',  # ⠘⠦ (4-5, 2-3-6)  crochet ouvrant
    ']': '\u2834\u2803',  # ⠴⠃ (3-5-6, 1-2) crochet fermant
    '©': '\u2810\u2809',  # ⠐⠉ (5, 1-4) copyright
    '°': '\u2810\u2815',  # ⠐⠕ (5, 1-3-5) degré
    '§': '\u2810\u280F',  # ⠐⠏ (5, 1-2-3-4) paragraphe
    '®': '\u2810\u2817',  # ⠐⠗ (5, 1-2-3-5) marque déposée
    '™': '\u2810\u281E',  # ⠐⠞ (5, 2-3-4-5) marque de commerce
    '&': '\u2810\u283F',  # ⠐⠿ (5, 1-2-3-4-5-6) et commercial
    '<': '\u2810\u2823',  # ⠐⠣ (5, 1-2-6) inférieur à
    '>': '\u2810\u281C',  # ⠐⠜ (5, 3-4-5) supérieur à
    '~': '\u2810\u2822',  # ⠐⠢ (5, 2-6)  tilde
    '*': '\u2810\u2814',  # ⠐⠔ (5, 3-5)  astérisque
    '\\': '\u2810\u280C',  # ⠐⠌ (5, 3-4) barre oblique inverse
    '#': '\u2810\u283C',  # ⠐⠼ (5, 3-4-5-6) dièse
    '%': '\u2810\u282C',  # ⠐⠬ (5, 3-4-6) pour cent
    '‰': '\u2810\u282C\u282C',  # ⠐⠬⠬ (5, 3-4-6, 3-4-6) pour mille
    '_': '\u2810\u2824',  # ⠐⠤ (5, 3-6) trait de soulignement
    '{': '\u2820\u2820\u2836',  # ⠠⠠⠶ (6, 6, 2-3-5-6) accolade ouvrante
    '}': '\u2834\u2804\u2804',  # ⠴⠄⠄ (3-5-6, 3, 3)  accolade fermante

}


def traduction(texte):
    # les symboles modifications
    modificateur_chiffre = '\u2820'  # ⠠ (6) // placé avant les chiffres
    modificateur_maj = '\u2828'  # ⠰ (46) // placé avant les majuscules ou sigles

    caracteres_arith = ['+', '-', '×', '÷', '÷', '=', '_'] # pour la notation Antoine

    # indicateurs pour savoir si le dernier caractère était un chiffre ou une majuscule
    dernier_c_etait_chiffre = False
    dernier_c_etait_maj = False

    # pour garder trace du mot en cours
    mot = ""
    index = 0
    texte_len = len(texte)

    # Initialiser une chaîne pour accumuler les résultats
    resultat = ""


    texte_len = len(texte)

    while index < texte_len:
        c = texte[index]

        # lorsque l'espace précède un caractère de resserrement
        if c == " " and (index + 1) < texte_len and texte[index+1] in "»”')]\"":
            index += 1  # on saute l'espace
            c = texte[index]
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c
            index += 1
            continue  # on passe à l'itération suivante

        # lorsqu'un caractère de resserrement précède un espace
        if c in "«“'([\"" and (index + 2) < texte_len and texte[index+1] == " " and texte[
            index+2].isascii():
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c
            index += 2  # on avance dans l'index (en sautant l'espace)
            continue  # on passe à l'itération suivante

        # lorsqu'un signe de ponctuation suit un mot
        if c.isspace() and not dernier_c_etait_chiffre and (index - 1) >= 0 and texte[
            index-1].isalpha() and (index+1) < texte_len and texte[index+1] in ",;:.?!…":
                index += 1  # on saute l'espace (supprime)
                c = texte[index]   # on récupère le signe de ponctuation
                if c in braille_symbols:
                    resultat += braille_symbols[c]
                else:
                    resultat += c
                index += 1  # on avance dans l'index
                continue  # on passe à l'itération suivante

        # un nombre ou signe arithmétique
        if c.isdigit() or c in caracteres_arith:
            # premier nombre ou chiffre arithmétique du mot
            if not dernier_c_etait_chiffre:
                resultat += modificateur_chiffre
                dernier_c_etait_chiffre = True
            # si le mot contient des majuscules
            if dernier_c_etait_maj:
                # on réinitialise (car on veut afficher le symbole maj à chaque fois)
                dernier_c_etait_maj = False
            # imprime le symbole braille correspondant au chiffre
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c
            index += 1
            continue

        elif c.isupper():
            # vérifie si le mot contient un mélange de majuscules, minuscules et nombres
            j = index
            mix_maj_min_num = False
            while j < texte_len and not texte[j].isspace():
                if texte[j].islower() or texte[j].isdigit():
                    mix_maj_min_num = True
                    break
                j += 1

            # ajoute le modificateur de majuscule si c'est la première majuscule ou si le mot est
            # mixte
            if (not dernier_c_etait_maj) or mix_maj_min_num:
                resultat += modificateur_maj
            # imprime le symbole braille correspondant à la majuscule
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c
            dernier_c_etait_maj = True


        # si c'est un point après une majuscule, imprime le point en braille
        elif c == '.' and dernier_c_etait_maj:
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c

        elif c.isspace() and dernier_c_etait_chiffre:
            j = index
            if c == " " and (j+1) < texte_len and texte[j+1].isdigit():
                # plutôt qu'un espace on imprime le séparateur de chiffre
                resultat += "\u2804"
            else:
                dernier_c_etait_chiffre = False
                if c in braille_symbols:
                    resultat += braille_symbols[c]
                else:
                    resultat += c

        elif (not c.isalnum() or c.isalpha()) and dernier_c_etait_chiffre:
            # dans un mot qui contient des chiffres
            # le c est un signe de ponctuation ou une lettre
            j = index
            # et il se trouve avant un espace
            if (j + 1) < texte_len and texte[j + 1].isspace():
                dernier_c_etait_chiffre = False
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c

        else:
            # imprime le symbole braille pour les autres caractères
            if c in braille_symbols:
                resultat += braille_symbols[c]
            else:
                resultat += c

        # incrémente l'index pour avancer dans le texte
        index += 1

    return resultat

########################################"

def download_font(url):
    response = requests.get(url)
    response.raise_for_status()  # Vérifie que la requête a réussi
    return BytesIO(response.content)

# Configuration de l'interface Streamlit
st.title("Générateur de Newsletter")

# Afficher la date du jour pour information
date_fin = datetime.today()
st.write(f"Date du jour : {datetime.today().strftime('%Y-%m-%d')}")

# Sélection de la durée avec "Depuis hier" par défaut
duree = st.selectbox(
    "Récupérer des articles publiés...",
    options=["depuis hier", "depuis 7 jours", "depuis 30 jours"],
)

# Calcul de la date de début en fonction de la durée sélectionnée
if duree == "depuis hier":
    date_debut = date_fin - timedelta(days=1)
elif duree == "depuis 7 jours":
    date_debut = date_fin - timedelta(days=7)
elif duree == "depuis 30 jours":
    date_debut = date_fin - timedelta(days=30)

# Sélection du mot clé
mot_cle = st.selectbox(
    "Sélectionnez un mot-clé",
    options=["technologie", "culture", "France", "politique", "international"]
)

# Sélection de la langue
langue = st.radio(
    "Sélectionnez la langue de génération",
    options=["Français", "Braille"]
)

# Bouton pour générer la newsletter
if st.button("Générer la newsletter"):
    # Vérifier que toutes les sélections sont faites
    if duree and mot_cle and langue:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": mot_cle,
            "from": date_debut.strftime('%Y-%m-%d'),
            "to": date_fin.strftime('%Y-%m-%d'),
            "sortBy": "popularity",
            "language": "fr",
            "pageSize": 5,
            "apiKey": "03085edf113f4403811720f6a880423e"
        }

        # Envoyer la requête GET
        reponse = requests.get(url, params=params)
        articles = reponse.json().get("articles", [])

        # Créer un document texte avec le contenu complet des articles
        if articles:
            output = ""
            for article in articles:
                article_url = article['url']
                try:
                    article_news = Article(article_url)
                    article_news.download()
                    article_news.parse()
                    contenu = article_news.text

                    if langue == "Français":
                        output += (f"Titre : {article['title']}\nSource : "
                                   f"{article['source']['name']}\nPublié le : "
                                   f"{article['publishedAt']}\nURL : {article['url']}\nContenu : "
                                   f"{contenu}\n\n"
                                   f"------------------------------\n\n\n\n")
                    else:
                        output += (f"⠨⠞⠊⠞⠗⠑⠒ {traduction(article['title'])}\n⠨⠎⠕⠥⠗⠉⠑⠒ "
                                   f"{traduction(article['source']['name'])}\n⠨⠏⠥⠃⠇⠊⠿ ⠇⠑⠒ "
                                   f"{traduction(article['publishedAt'])}\n⠨⠥⠗⠇⠒ "
                                   f"{traduction(article['url'])}\n⠨⠉⠕⠝⠞⠑⠝⠥⠒ "
                                   f"{traduction(contenu)}\n\n"
                                   f"⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶\n\n\n\n")
                except Exception as e:
                    st.error(f"Erreur lors de la récupération de l'article : {e}")

            # Options de téléchargement
            download_type = st.selectbox("Sélectionnez le format de téléchargement", ["PDF"])

            if download_type == "Texte":
                st.download_button(label="Télécharger en .txt", data=output.encode('utf-8'),
                                   file_name="newsletter.txt")

            if download_type == "PDF":
                if output:  # Vérification que 'output' n'est pas vide

                    # Chemin vers le dossier contenant les polices
                    font_path = "DejaVuSans.ttf"

                    # Créer le PDF
                    pdf = FPDF()
                    pdf.add_page()

                    # Charger la police Unicode
                    pdf.add_font('DejaVu', '', font_path, uni=True)
                    pdf.set_font('DejaVu', '', 12)

                    # Ajouter le contenu ligne par ligne au PDF
                    for line in output.split(
                            "\n\n"):  # Chaque double retour à la ligne représente un nouveau paragraphe
                        pdf.multi_cell(0, 10, line)
                        pdf.ln()

                    # Préparer le fichier PDF en mémoire
                    buffer = BytesIO()
                    pdf.output(buffer, 'F')  # Génère le contenu du PDF dans le buffer
                    buffer.seek(0)  # Retour au début du buffer

                    st.download_button(
                        label="Télécharger en .pdf",
                        data=buffer,
                        file_name="newsletter.pdf",
                        mime="application/pdf"
                    )


    else:
        st.error("Veuillez remplir tous les champs avant de générer la newsletter.")



