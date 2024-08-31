# Nom ......... : dico_braille.py
# Rôle ........ : Dictionnaire français vers le braille de grade I
# Auteur ...... : Avrile Floro
# Version ..... : V0.1 du 27/08/2024
# Licence ..... : réalisé dans le cadre du cours de I&C (projet)


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

    # caractères spéciaux
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
