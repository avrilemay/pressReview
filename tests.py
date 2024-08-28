# Nom ......... : test.py
# Rôle ........ : Permet de tester la fonction de traduction
# Auteur ...... : Avrile Floro
# Version ..... : V0.1 du 27/08/2024
# Licence ..... : réalisé dans le cadre du cours de I&C (projet)

from traduction import traduction

# fonction pour tester différents exemples du doc de référence
def test_traduction():
    exemples = [
        "PIERRE",
        "Pierre",
        "I, II, III",
        "BC/DE",
        "FRISON-ROCHE",
        "L'Europe",
        "UNESCO",
        "UFA",
        "HCl",
        "McDonald",
        "le XVIIIᵐᵉ siècle",
        "Sujet + verbe + complément = phrase complète.",
        "La note A+",
        "Le format A4",
        "La Guerre 1939-1945",
        "31/12/2003",
        "18h30",
        "18:45",
        "2 × 5 = 10",
        "4x4",
        "10²=100",
        "6 ÷ 3 = 2",
        "6÷3=2",
        "2:2=1",
        "Les 2/3 de la population",
        "Réf. AB5XXw10Z",
        "J4K 5G4",
        "Les 36 000 communes de France",
        "Tél.: 01 44 49 35 35",
        "Titres 1.1, 1.2, 1.3",
        "La version 6.00 du logiciel",
        "et/ou",
        "madame / monsieur",
        "20%",
        "30 %",
        "Les taux de natalité et de mortalité sont donnés en ‰",
        "Comment allez-vous ?",
        "Très bien !",
        "« citation »",
        '"citation "',
        "“ citation”",
        "(note)",
        "[123]",
        "À cette époque –juin 2001– fut signé un Accord de coopération à Casablanca.",
        "Les 63 – ou 64 – symboles braille",
        "100 $ ou 100$ ou $100"
    ]

    resultats_attendus = [
        "⠨⠏⠊⠑⠗⠗⠑",  # PIERRE
        "⠨⠏⠊⠑⠗⠗⠑",  # Pierre
        "⠨⠊⠂⠀⠨⠊⠊⠂⠀⠨⠊⠊⠊",  # I, II, III (chiffres romains)
        "⠨⠃⠉⠌⠙⠑",  # BC/DE
        "⠨⠋⠗⠊⠎⠕⠝⠤⠨⠗⠕⠉⠓⠑",  # FRISON-ROCHE
        "⠨⠇⠄⠨⠑⠥⠗⠕⠏⠑",  # L'Europe
        "⠨⠥⠝⠑⠎⠉⠕",  # UNESCO
        "⠨⠥⠋⠁",  # UFA ou U.F.A.
        "⠨⠓⠨⠉⠇",  # HCl
        "⠨⠍⠉⠨⠙⠕⠝⠁⠇⠙",  # McDonald
        "⠇⠑⠀⠨⠭⠧⠊⠊⠊⠈⠍⠑⠀⠎⠊⠮⠉⠇⠑",  # le XVIIIᵐᵉ siècle
        "⠨⠎⠥⠚⠑⠞⠀⠠⠖⠀⠧⠑⠗⠃⠑⠀⠠⠖⠀⠉⠕⠍⠏⠇⠿⠍⠑⠝⠞⠀⠠⠶⠀⠏⠓⠗⠁⠎⠑⠀⠉⠕⠍⠏⠇⠮⠞⠑⠲",  # Sujet + verbe + complément =
        # phrase complète.
        "⠨⠇⠁⠀⠝⠕⠞⠑⠀⠨⠁⠠⠖",  # La note A+
        "⠨⠇⠑⠀⠋⠕⠗⠍⠁⠞⠀⠨⠁⠠⠹",  # Le format A4
        "⠨⠇⠁⠀⠨⠛⠥⠑⠗⠗⠑⠀⠠⠡⠪⠩⠪⠤⠡⠪⠹⠱",  # La Guerre 1939-1945
        "⠠⠩⠡⠌⠡⠣⠌⠣⠼⠼⠩",  # 31/12/2003
        "⠠⠡⠳⠓⠩⠼",  # 18h30
        "⠠⠡⠳⠒⠹⠱",  # 18:45
        "⠠⠣⠔⠱⠶⠡⠼",  # 2 × 5 = 10
        "⠠⠹⠭⠹",  # 4x4
        "⠠⠡⠼⠈⠣⠶⠡⠼⠼",  # 10²=100
        "⠠⠫⠒⠩⠶⠣",     # 6 ÷ 3 = 2
        "⠠⠫⠒⠩⠶⠣",  # 6÷3=2
        "⠠⠣⠒⠣⠶⠡",  # 2:2=1
        "⠨⠇⠑⠎⠀⠠⠣⠌⠩⠀⠙⠑⠀⠇⠁⠀⠏⠕⠏⠥⠇⠁⠞⠊⠕⠝",  # Les 2/3 de la population
        "⠨⠗⠿⠋⠲⠀⠨⠁⠨⠃⠠⠱⠨⠭⠨⠭⠺⠡⠼⠨⠵",  # Réf. AB5XXw10Z
        "⠨⠚⠠⠹⠨⠅⠀⠠⠱⠨⠛⠹",  # J4K 5G4
        "⠨⠇⠑⠎⠀⠠⠩⠫⠄⠼⠼⠼⠀⠉⠕⠍⠍⠥⠝⠑⠎⠀⠙⠑⠀⠨⠋⠗⠁⠝⠉⠑",  # Les 36 000 communes de France
        "⠨⠞⠿⠇⠲⠒⠀⠠⠼⠡⠄⠹⠹⠄⠹⠪⠄⠩⠱⠄⠩⠱",  # Tél.: 01 44 49 35 35
        "⠨⠞⠊⠞⠗⠑⠎⠀⠠⠡⠲⠡⠂⠀⠠⠡⠲⠣⠂⠀⠠⠡⠲⠩",  # Titres 1.1, 1.2, 1.3
        "⠨⠇⠁⠀⠧⠑⠗⠎⠊⠕⠝⠀⠠⠫⠲⠼⠼⠀⠙⠥⠀⠇⠕⠛⠊⠉⠊⠑⠇",  # La version 6.00 du logiciel
        "⠑⠞⠌⠕⠥",  # et/ou
        "⠍⠁⠙⠁⠍⠑⠀⠌⠀⠍⠕⠝⠎⠊⠑⠥⠗",  # madame / monsieur
        "⠠⠣⠼⠐⠬",  # 20%
        "⠠⠩⠼⠀⠐⠬",  # 30 %
        "⠨⠇⠑⠎⠀⠞⠁⠥⠭⠀⠙⠑⠀⠝⠁⠞⠁⠇⠊⠞⠿⠀⠑⠞⠀⠙⠑⠀⠍⠕⠗⠞⠁⠇⠊⠞⠿⠀⠎⠕⠝⠞⠀⠙⠕⠝⠝⠿⠎⠀⠑⠝⠀⠐⠬⠬",  # Les taux de natalité et de
        # mortalité sont donnés en ‰
        "⠨⠉⠕⠍⠍⠑⠝⠞⠀⠁⠇⠇⠑⠵⠤⠧⠕⠥⠎⠢",  # Comment allez-vous ?
        "⠨⠞⠗⠮⠎⠀⠃⠊⠑⠝⠖",  # Très bien !
        "⠶⠉⠊⠞⠁⠞⠊⠕⠝⠶",  # « citation »
        "⠶⠉⠊⠞⠁⠞⠊⠕⠝⠶",  # '"citation "',
        "⠶⠉⠊⠞⠁⠞⠊⠕⠝⠶",  # "“ citation”",
        "⠦⠝⠕⠞⠑⠴",  # (note)
        "⠘⠦⠠⠡⠣⠩⠴⠃",  # [123]
        "⠨⠷⠀⠉⠑⠞⠞⠑⠀⠿⠏⠕⠟⠥⠑⠀⠤⠤⠚⠥⠊⠝⠀⠠⠣⠼⠼⠡⠤⠤⠀⠋⠥⠞⠀⠎⠊⠛⠝⠿⠀⠥⠝⠀⠨⠁⠉⠉⠕⠗⠙⠀⠙⠑⠀⠉⠕⠕⠏⠿⠗⠁⠞⠊⠕⠝⠀⠷⠀⠨⠉⠁⠎⠁⠃⠇⠁⠝⠉⠁⠲",
        # À cette époque –juin 2001– fut signé un Accord de coopération à Casablanca.
        "⠨⠇⠑⠎⠀⠠⠫⠩⠀⠤⠤⠀⠕⠥⠀⠠⠫⠹⠀⠤⠤⠀⠎⠽⠍⠃⠕⠇⠑⠎⠀⠃⠗⠁⠊⠇⠇⠑",  # Les 63 – ou 64 – symboles braille
        "⠠⠡⠼⠼⠀⠘⠎⠀⠕⠥⠀⠠⠡⠼⠼⠘⠎⠀⠕⠥⠀⠘⠎⠠⠡⠼⠼",  # 100 $ ou 100$ ou $100
    ]

    # vérifie les traductions obtenues vs les résultats attendus
    for source, attendu in zip(exemples, resultats_attendus):
        resultat = traduction(source)   # résultat obtenu
        if resultat == attendu:
            print(f"Traduction correcte pour '{source}'.")
        else:
            print(f"Erreur de traduction pour '{source}':\nAttendu : {attendu}\nObtenu  : {resultat}")


# appel de la fonction de test
test_traduction()





