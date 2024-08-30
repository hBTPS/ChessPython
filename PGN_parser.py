""" Parser PGN:
Si path est le chemin d'accès (type str) à un fichier .pgn alors la commande:
d = pgn_to_dict(path) affecte à d le dictionnaire qui à chaque numéro de tour n associe
une liste constituée du coup joué par les blancs puis celui des noirs au tour n
Les coups sont en notation algébrique abrégée, exploitables avec la méthode faire_coup de plateau """

# Hadrien

def del_timestamp(string):
    """ Variable d'entrée: string, au format str (on entrera le texte contenu dans le fichier pgn)
    Supprime les potentiels indicateurs de temps présents dans string (horodatage)
    Retourne string, chaîne de départ pour laquelle on a supprimé l'horodatage"""
    for i in range(len(string)):
        if string[i] == '{':
            i0 = i
            j = i0
            s = string[i0]
            while s != '}':
                j += 1
                s = string[j]
            return del_timestamp(string[:i0] + string[j + 1:])
    return string


def del_number_repetition(string):
    """ Variable d'entrée: string, au format str (on entrera le texte contenu dans le fichier pgn)
     Supprime les potentielles répétitions du numéro de chaque tour présents dans string
     Retourne string, chaîne de départ pour laquelle on a supprimé toutes ces répétitions"""
    for i in range(len(string)):
        s = string[i:i+4]
        if s.endswith('...'):
            return del_number_repetition(string[:i-1] + string[i+4:])
    return string


def turn_into_dict(string):
    """ Variable d'entrée: string, au format str (on entrera le texte contenu dans le fichier pgn
        sans horodatage ni répétition du numéro des tours)
        Supprime toute information annexe concernant la partie et convertit string en dictionnaire
        Retourne d, dictionnaire dont une clé est un numéro de tour et la valeur associée est la liste
        constituée du coup joué par les blancs et du coup joué par les noirs lors de ce tour

        ex: '1. e4  e5  2. f4  Nc6' devient {1:['e4', 'e5'], 2:['f4', 'Nc6']} """


    k = string.index('1. ')
    string = string[k:]
    d = {}

    n = string.count('.')

    for a in range(1, n + 1):
        r = 2
        if len(str(a)) == 2:
            r = 3
        if a != n:
            d[a] = string[string.index(f'{a}.') + r: string.index(f'{a + 1}.')]
        else:
            d[a] = string[string.index(f'{a}.') + r:]

        for char in ['?', '!', '#', '+', '1-0', '0-1']:
            d[a] = d[a].replace(char, '')

        if '\n' in d[a]:
            if d[a][d[a].index('\n') - 1] == ' ':
                d[a] = d[a].replace('\n', '')
            else:
                d[a] = d[a].replace('\n', ' ')

        if d[a][:2] == '  ':
            d[a] = d[a][2:]
        elif d[a][0] == ' ':
            d[a] = d[a][1:]

        if d[a][-2:] == '  ':
            d[a] = d[a][:-2]
        elif d[a][-1] == ' ':
            d[a] = d[a][:-1]

        if ' ' in d[a]:
            if '  ' in d[a]:
                d[a] = d[a].replace('  ', ' ')
            i = d[a].index(' ')
            d[a] = [d[a][:i], d[a][i+1:]]

    return d


def pgn_to_dict(path):
    """ Variable d'entrée: path, type str (chemin d'accès au fichier .pgn)
    Ouvre le fichier pgn, stocke son contenu textuel dans la variable pgn_text
    Applique turn_into_dict à del_number_repetition(del_timestamp(pgn_text))
    Retourne le dictionnaire associant au numéro de chaque tour la liste des coups joués
    par chaque camp """
    f = open(path)
    pgn_text = f.read()
    f.close()
    return turn_into_dict(del_number_repetition(del_timestamp(pgn_text)))


if __name__ ==  "__main__" :
    path = "C:\\Users\\Hadrien\\Documents\\ENSTA 1A\\UE 2.4 Projet\\Projet info\\PGN games\\OwnGame2.pgn"
    f = open(path)
    pgn_text = f.read()
    f.close()
    print(pgn_text)
    print(pgn_to_dict(path))
