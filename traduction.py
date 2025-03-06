# Nom ......... : traduction.py
# Rôle ........ : Permet de traduire un contenu du français vers le braille de grade I
# Auteur ...... : Avrile Floro
# Version ..... : V0.2 du 06/03/2025
# Licence ..... : réalisé dans le cadre du cours de I&C (projet)


# 1) Dictionnaire des symboles braille
braille_symbols = {
    # l'alphabet + signes propres au français + ponctuation
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

    # ponctuation
    ',': '\u2802',  # ⠂ (2) virgule
    ';': '\u2806',  # ⠆ (2-3) point-virgule
    ':': '\u2812',  # ⠒ (2-5) deux-points
    '.': '\u2832',  # ⠲ (2-5-6) point
    '!': '\u2816',  # ⠖ (2-3-5) point d'exclamation
    '?': '\u2822',  # ⠢ (2-6) point d'interrogation
    '-': '\u2824',  # ⠤ (3-6) trait d'union
    '(': '\u2826',  # ⠦ (2-3-6) parenthèse ouvrante
    ')': '\u2834',  # ⠴ (3-5-6) parenthèse fermante
    **dict.fromkeys(["'", '’'], '\u2804'),  # ⠄ (3) apostrophe/espace entre les chiffres
    '/': '\u280C',  # ⠌ (3-4)
    '@': '\u281C',  # ⠜ (3-4-5)
    **dict.fromkeys(['"', '«', '“', '»', '”'], '\u2836'),  # ⠶ (2-3-5-6) guillemets

    # chiffres et signes arithmétiques de base
    '1': '\u2821',  # ⠡ (1-6)
    '2': '\u2823',  # ⠣ (1-2-6)
    '3': '\u2829',  # ⠩ (1-4-6)
    '4': '\u2839',  # ⠹ (1-4-5-6)
    '5': '\u2831',  # ⠱ (1-5-6)
    '6': '\u282B',  # ⠫ (1-2-4-6)
    '7': '\u283B',  # ⠯ (1-2-4-5-6)
    '8': '\u2833',  # ⠳ (1-2-5-6)
    '9': '\u282A',  # ⠪ (2-4-6)
    '0': '\u283C',  # ⠼ (3-4-5-6)
    '+': '\u2816',  # ⠖ (2-3-5)
    '-': '\u2824',  # ⠤ (3-6)
    '×': '\u2814',  # ⠔ (3-5)
    '÷': '\u2812',  # ⠒ (2-5)
    '=': '\u2836',  # ⠶ (2-3-5-6)
    '_': '\u2822',  # ⠢ (2-6)

    # caractères spéciaux
    '☐': '\u282f\u283d',  # case à cocher
    '•': '\u282a\u2815',  # puce
    '↔': '\u282A\u2812\u2815',  # flèche bidirectionnelle
    '←': '\u282a\u2812\u2812',  # flèche gauche
    '→': '\u2812\u2812\u2815',  # flèche droite
    '…': '\u2832\u2832\u2832',  # points de suspension
    '–': '\u2824\u2824',        # tiret (demi-cadratin)
    '¢': '\u2818\u2809',        # cent
    '€': '\u2818\u2811',        # euro
    '£': '\u2818\u2807',        # livre
    'µ': '\u2818\u280D',        # mu
    'π': '\u2818\u280F',        # pi
    '$': '\u2818\u280E',        # dollar
    '¥': '\u2818\u283D',        # yen
    '≤': '\u2818\u2823',        # inférieur ou égal
    '≥': '\u2818\u281C',        # supérieur ou égal
    '[': '\u2818\u2826',        # crochet ouvrant
    ']': '\u2834\u2803',        # crochet fermant
    '©': '\u2810\u2809',        # copyright
    '°': '\u2810\u2815',        # degré
    '§': '\u2810\u280F',        # paragraphe
    '®': '\u2810\u2817',        # marque déposée
    '™': '\u2810\u281E',        # marque de commerce
    '&': '\u2810\u283F',        # et commercial
    '<': '\u2810\u2823',        # inférieur à
    '>': '\u2810\u281C',        # supérieur à
    '~': '\u2810\u2822',        # tilde
    '*': '\u2810\u2814',        # astérisque
    '\\': '\u2810\u280C',       # backslash
    '#': '\u2810\u283C',        # dièse
    '%': '\u2810\u282C',        # pourcent
    '‰': '\u2810\u282C\u282C',  # pour mille
    '_': '\u2810\u2824',        # soulignement
    '{': '\u2820\u2820\u2836',  # accolade ouvrante
    '}': '\u2834\u2804\u2804',  # accolade fermante
}


# 2) Dictionnaire d'exposants
def est_exposant(c):
    """ Vérifie si c est un exposant et renvoie:
        - Le marqueur d'exposant Braille (⠈, U+2808) + l'équivalent non exposant
        - (None, None) si c n'est pas un exposant géré
    """
    exposants = {
        '¹': '1', '²': '2', '³': '3', '⁰': '0', '⁴': '4', '⁵': '5', '⁶': '6',
        '⁷': '7', '⁸': '8', '⁹': '9', 'ⁱ': 'i', 'ⁿ': 'n', 'ᵉ': 'e', 'ᵐ': 'm',
    }

    if c in exposants:
        # ⠈ (point 4) = U+2808
        return '\u2808', exposants[c]
    else:
        return None, None


# 3) Fonction de normalisation des caractères «exotiques»
def normaliser_caracteres_speciaux(texte: str) -> str:
    """
    Remplace certains caractères 'exotiques' (tirets cadratin, guillemets spéciaux, etc.)
    par leurs équivalents déjà pris en charge dans braille_symbols ou par ASCII standard.
    """
    remplacements = {
        '—': '-',     # Tiret cadratin -> tiret simple
        '–': '-',     # Demi-cadratin -> tiret simple
        '‒': '-',     # figure dash -> tiret simple
        '−': '-',     # signe moins -> tiret simple
    }

    for ancien, nouveau in remplacements.items():
        texte = texte.replace(ancien, nouveau)
    return texte


# 4) Fonction principale de traduction vers le Braille
def traduction(texte: str) -> str:
    """
    Traduit une chaîne de caractères depuis le français vers le braille de grade I,
    en gérant ponctuellement certains cas (exposants, chiffres, majuscules, etc.).
    """

    # --- Étape de normalisation préliminaire ---
    texte = normaliser_caracteres_speciaux(texte)

    # les symboles modificateurs
    modificateur_chiffre = '\u2820'  # ⠠ (6) pour les chiffres ou signes arithmétiques
    modificateur_maj = '\u2828'     # ⠰ (4-6) pour les majuscules ou sigles

    # caractères arithmétiques, fin d'exposants
    caracteres_arith = ['+', '-', '×', '÷', '÷', '=', '_']
    fin_exposant = ['+', '-', '×', '÷', '÷', '=', '_', '.', ':', ';', '…', ',']
    c_exposant = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', 'ⁱ', 'ⁿ', 'ᵉ', 'ᵐ']

    # indicateurs booléens de contexte
    math_last_c = False
    majuscule_last_c = False
    exposant_last_c = False

    resultat = ""
    texte_len = len(texte)
    index = 0

    while index < texte_len:
        c = texte[index]

        # 1) Si on quitte une zone d'exposant
        if (c in fin_exposant or c.isspace()) and exposant_last_c:
            exposant_last_c = False

        # 2) Espace avant un caractère de resserrement ( ), ] ) etc.
        if c == " " and (index + 1) < texte_len and texte[index+1] in "»”')]\"":
            index += 1
            c = texte[index]
            resultat += braille_symbols.get(c, c)  # .get() => si c absent, on ajoute c brut
            index += 1
            continue

        # 3) Caractère de resserrement + espace + char => on saute l'espace
        if c in "«“'([\"" and (index + 2) < texte_len and texte[index+1] == " " and not texte[index+2].isspace():
            resultat += braille_symbols.get(c, c)
            index += 2  # on saute l'espace
            continue

        # 4) Un signe de ponctuation suit un mot après un espace => on supprime l'espace
        if c.isspace() and not math_last_c and (index - 1) >= 0 and texte[index-1].isalpha() \
           and (index+1) < texte_len and texte[index+1] in ",;:.?!…":
            index += 1
            c = texte[index]
            resultat += braille_symbols.get(c, c)
            index += 1
            continue

        # 5) Trait d'union entre deux mots
        if (c == "-" and index - 1 >= 0 and texte[index-1].isalpha()
            and index + 1 < texte_len and texte[index+1].isalpha()):
            resultat += braille_symbols.get(c, c)
            majuscule_last_c = False
            index += 1
            continue

        # 6) Chiffre ou signe arithmétique
        if c.isdigit() or c in caracteres_arith:
            # Vérifie exposant
            symbole_exposant, equivalent_non_exposant = est_exposant(c)
            if symbole_exposant:
                # c est un exposant
                if not exposant_last_c:
                    resultat += symbole_exposant
                resultat += braille_symbols.get(equivalent_non_exposant, equivalent_non_exposant)
                exposant_last_c = True
                majuscule_last_c = False
                index += 1
                continue
            else:
                # c est un chiffre ou un signe de base
                if not math_last_c:
                    resultat += modificateur_chiffre
                    math_last_c = True
                if majuscule_last_c:
                    majuscule_last_c = False
                resultat += braille_symbols.get(c, c)
                index += 1
                continue

        # 7) Majuscule
        if c.isupper():
            # Vérifie si le mot est mixte (majuscules, minuscules, chiffres)
            j = index
            mix_maj_min_num = False
            while j < texte_len and not texte[j].isspace():
                if (texte[j].islower() or texte[j].isdigit()) and texte[j] not in c_exposant:
                    mix_maj_min_num = True
                    break
                j += 1
            if not majuscule_last_c or mix_maj_min_num:
                resultat += modificateur_maj
            resultat += braille_symbols.get(c, c)
            majuscule_last_c = True
            index += 1
            continue

        # 8) Point après une majuscule sans espace (sigle du style "U.S.A.")
        if (c == '.' and (index-1) >= 0 and texte[index-1].isupper()
            and (index+1) < texte_len and not texte[index+1].isspace()):
            resultat += braille_symbols.get(c, c)
            index += 1
            continue

        # 9) Espace entre deux chiffres => séparateur
        if (c == " " and index-1 >= 0 and texte[index-1].isdigit()
            and (index+1) < texte_len and texte[index+1].isdigit()):
            resultat += '\u2804'  # ⠄
            index += 1
            continue

        # 10) Espace au sein d'une expression arithmétique => on le supprime
        if c == " " and math_last_c and index-1 >= 0 and (texte[index-1].isdigit() or texte[index-1] in caracteres_arith) \
           and (index+1) < texte_len and (texte[index+1].isdigit() or texte[index+1] in caracteres_arith):
            index += 1
            continue

        # 11) Espace après expression chiffrée + avant mot => on ferme l'expression math
        if c.isspace() and math_last_c:
            math_last_c = False
            resultat += braille_symbols.get(c, c)
            index += 1
            continue

        # 12) Lettre ou ponctuation dans un mot chiffré
        if (c.isalpha() or not c.isalnum()) and math_last_c:
            if (index+1) < texte_len and texte[index+1].isspace():
                math_last_c = False
            symbole_exposant, equivalent_non_exposant = est_exposant(c)
            if symbole_exposant:
                if not exposant_last_c:
                    resultat += symbole_exposant
                resultat += braille_symbols.get(equivalent_non_exposant, equivalent_non_exposant)
                exposant_last_c = True
            else:
                resultat += braille_symbols.get(c, c)
            index += 1
            continue

        # 13) Espace standard
        if c == " ":
            majuscule_last_c = False
            math_last_c = False
            resultat += braille_symbols.get(c, c)
            index += 1
            continue

        # 14) Cas générique (lettre minuscule, ponctuation, etc.)
        else:
            symbole_exposant, equivalent_non_exposant = est_exposant(c)
            if symbole_exposant:
                if not exposant_last_c:
                    resultat += symbole_exposant
                resultat += braille_symbols.get(equivalent_non_exposant, equivalent_non_exposant)
                exposant_last_c = True
            else:
                resultat += braille_symbols.get(c, c)
            index += 1

    return resultat
