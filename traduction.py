# Nom ......... : traduction.py
# Rôle ........ : Permet la traduction du français vers le braille de grade I
# Auteur ...... : Avrile Floro
# Version ..... : V0.1 du 27/08/2024
# Licence ..... : réalisé dans le cadre du cours de I&C (projet)

from dico_braille import braille_symbols

# fonction qui traduit une str du français vers le braille
def traduction(texte):

    # les symboles modifications
    modificateur_chiffre = '\u2820'  # ⠠ (6) // à placer avant les chiffres
    modificateur_maj = '\u2828'  # ⠰ (46) // à placer avant les majuscules ou sigles
    caracteres_arith = ['+', '-', '×', '÷', '÷', '=', '_']  # pour la notation Antoine
    fin_exposant = ['+', '-', '×', '÷', '÷', '=', '_', '.', ':', ';', '…', ',']  # pour exposant
    c_exposant = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', 'ⁱ', 'ⁿ', 'ᵉ', 'ᵐ']

    # les indicateurs (opération arithmétiques, majuscules, exposants)
    math_last_c = False
    majuscule_last_c = False
    exposant_last_c = False

    resultat = ""  # la chaîne traduite en braille
    texte_len = len(texte)  # longueur de la str
    index = 0  # initialisation à 0

    while index < texte_len:  # parcourt de la str
        c = texte[index]  # on isole le caractère

        # si le marqueur d'exposant est à vrai et on rencontre le symbole de fin d'exposant
        if (c in fin_exposant or c.isspace()) and exposant_last_c:
            exposant_last_c = False # passage du marqueur à faux
            # on continue dans la boucle pour le traitement selon le type de caractère;

        # lorsqu'un espace précède un caractère de resserrement
        if c == " " and (index + 1) < texte_len and texte[index+1] in "»”')]\"":
            index += 1  # on saute l'espace (en avançant dans l'index)
            c = texte[index]  # on met à jour le caractère étudié
            resultat += braille_symbols[c]  # on imprime le caractère en Braille
            index += 1  # on avance dans l'index
            continue  # on passe à l'itération suivante

        # lorsqu'un caractère de resserrement précède un espace et un caractère non blanc
        if c in "«“'([\"" and (index + 2) < texte_len and texte[index+1] == " " and not texte[
            index+2].isspace():
            resultat += braille_symbols[c]  # on imprime le caractère en Braille
            index += 2  # on avance de 2 dans l'index (on saute l'espace)
            continue  # on passe à l'itération suivante

        # lorsqu'un signe de ponctuation suit un mot après un espace
        if c.isspace() and not math_last_c and (index - 1) >= 0 and texte[
            index-1].isalpha() and (index+1) < texte_len and texte[index+1] in ",;:.?!…":
                index += 1  # on saute l'espace (on le supprime car non retranscrit)
                c = texte[index]  # on met à jour le caractère (signe de ponctuation)
                if c in braille_symbols:
                    resultat += braille_symbols[c]  # on imprime le caractère en braille
                else:
                    resultat += c
                index += 1  # on avance dans l'index
                continue  # on passe à l'itération suivante

        # lorsqu'on rencontre un trait-d'union entre deux mots
        if (c == "-" and index - 1 >= 0 and texte[index-1].isalpha() and index + 1 < texte_len
                and texte[index+1].isalpha()):
            resultat += braille_symbols[c]  # on imprime le caractère en Braille
            majuscule_last_c = False
            index += 1  # on avance de 2 dans l'index (on saute l'espace)
            continue  # on passe à l'itération suivante

        # lorsqu'on rencontre un chiffre ou un caractère arithmétique
        if c.isdigit() or c in caracteres_arith:
                # premier nombre ou chiffre arithmétique du mot
                if not math_last_c:  # si le marqueur de maths n'était pas actif
                    resultat += modificateur_chiffre  # on ajoute le modificateur pour les maths
                    math_last_c = True  # on passe le marqueur à vrai
                # si le mot contient des majuscules (et des chiffres)
                if majuscule_last_c:
                    # on réinitialise le marqueur (pour afficher le symbole maj à chaque fois)
                    majuscule_last_c = False
                resultat += braille_symbols[c]  # on imprime le c en braille
                index += 1  # avance dans l'index
                continue  # passe à l'itération suivante

        # lorsqu'on rencontre une majuscule
        if c.isupper():
            # vérifie si le mot contient un mélange de majuscules, minuscules et nombres
            j = index   # on garde trace de l'index actuel
            mix_maj_min_num = False  # on initialise à faux le marqueur de mot mélangé
            while j < texte_len and not texte[j].isspace():  # on parcourt le mot en cours
                if (texte[j].islower() or texte[j].isdigit()) and texte[j] not in c_exposant :
                    # si on rencontre un chiffre ou une minuscule
                    mix_maj_min_num = True   # on passe le marqueur à vrai
                    break   # on sort
                j += 1   # on avance dans notre index bis
            #
            # si c'est la 1e majuscule ou si le mot est mixte (maj, minus et chiffre)
            if not majuscule_last_c or mix_maj_min_num:
                resultat += modificateur_maj   # on imprime le modificateur de majuscule
            resultat += braille_symbols[c]   # imprime le symb braille de la lettre
            majuscule_last_c = True   # passe à vrai l'indicateur de maj
            index += 1  # avance dans l'index
            continue   # passe à l'itération suivante

        # lorsqu'on rencontre un espace après un chiffre et avant un autre chiffre
        if (c == " " and index-1 >= 0 and texte[index-1].isdigit() and (index+1) < texte_len and
                texte[index+1].isdigit()):
                resultat += "\u2804"  # plutôt qu'un espace, imprime le séparateur de chiffre
                index += 1  # avance dans l'index
                continue   # passe à l'itération suivante

        # lorsqu'on rencontre un espace au sein d'une expression arithmétique
        if (c == " " and math_last_c and index-1 >= 0 and (texte[index-1].isdigit() or texte[
            index-1] in caracteres_arith) and index+1 <= texte_len and
            (texte[index+1].isdigit() or texte[index+1] in caracteres_arith)):
                index += 1  # avance dans l'index (on supprime l'espace)
                continue   # passe à l'itération suivante

        # lorsqu'on rencontre un espace après une expression chiffrée ou arithmétique et avant
        # un autre mot
        if c.isspace() and math_last_c:
            math_last_c = False   # passe l'indicateur d'expression arithmétique à faux
            if c in braille_symbols:
                resultat += braille_symbols[c]  # on imprime le caractère en braille
            else:
                resultat += c
            index += 1  # avance dans l'index
            continue   # passe à l'itération suivante

        # lorsqu'on rencontre une lettre ou de la ponctuation dans un mot qui contient des chiffres
        if (c.isalpha() or not c.isalnum()) and math_last_c:
            # si le caractère est avant un espace
            if (index+1) < texte_len and texte[index+1].isspace():
                math_last_c = False  # on passe l'indicateur d'expressions arithmétiques à faux
            symbole_exposant, equivalent_non_exposant = est_exposant(c)  # traite l'exposant
            if symbole_exposant:  # si exposant il y a
                if not exposant_last_c: # s'il ce n'était pas déjà un exposant
                    resultat += symbole_exposant  # ajoute le symbole exposant
                resultat += braille_symbols[equivalent_non_exposant]  # ajoute c non exposant équiv
                exposant_last_c = True  # passe le marqueur à true
            elif c in braille_symbols:
                resultat += braille_symbols[c]  # on imprime le caractère en braille
            else:
                resultat += c
            index += 1  # avance dans l'index
            continue   # passe à l'itération suivante

        # lorsqu'on rencontre un espace
        if c.isspace():
            majuscule_last_c = False
            math_last_c = False
            exposant_last_c = False
            if c in braille_symbols:
                resultat += braille_symbols[c]  # on imprime le caractère en braille
            else:
                resultat += c
            index += 1  # avance dans l'index
            continue   # passe à l'itération suivante

        # lorsqu'il s'agit d'un autre cas de figure
        else:
            symbole_exposant, equivalent_non_exposant = est_exposant(c)  # traite l'exposant
            if symbole_exposant:  # si exposant il y a
                if not exposant_last_c:  # s'il ce n'était pas déjà un exposant
                    resultat += symbole_exposant  # ajoute le symbole exposant
                resultat += braille_symbols[equivalent_non_exposant]  # ajoute c non exposant équiv
                exposant_last_c = True  # passe le marqueur à true
            elif c in braille_symbols:
                resultat += braille_symbols[c]  # on imprime le caractère en braille
            else:
                resultat += c
            # incrémente l'index pour avancer dans le texte
            index += 1

    return resultat





# fonction qui vérifie si un c est un exposant et renvoie le marqueur et équiv non exposant
def est_exposant(c):
    # dico pour associer les exposants avec leurs équivalents non exposants
    exposants = {
        '¹': '1',  # ¹ -> 1
        '²': '2',  # ² -> 2
        '³': '3',  # ³ -> 3
        '⁰': '0',  # ⁰ -> 0
        '⁴': '4',  # ⁴ -> 4
        '⁵': '5',  # ⁵ -> 5
        '⁶': '6',  # ⁶ -> 6
        '⁷': '7',  # ⁷ -> 7
        '⁸': '8',  # ⁸ -> 8
        '⁹': '9',  # ⁹ -> 9
        'ⁱ': 'i',  # ⁱ -> i
        'ⁿ': 'n',  # ⁿ -> n
        'ᵉ': 'e',  # ᵉ -> e
        'ᵐ': 'm',  # ᵐ -> m
    }

    if c in exposants:   # si le caractère est dans la liste des exposants, retourne
        return '\u2808', exposants[c]  # ⠈ (4) + caractère non exposant
    else:           # sinon rien
        return None, None




