from Plateau import *
from numpy import inf
# from time import time

def switch(qj):
    qj = 'w' if qj == 'b' else 'b'
    return qj

def ordonner(coups):
    # coups.sort(key=lambda s: 'x' in s)
    coups.sort(key=len)
    coups.reverse()
    return coups

def evaluer(plateau, qj):
    score_blancs, score_noirs = 0, 0
    for piece in plateau.etat:
        if piece.couleur == 'w' and piece.val is not None:
            score_blancs += piece.val
        elif piece.couleur == 'b' and piece.val is not None:
            score_noirs += piece.val
    avantage = score_blancs - score_noirs
    if qj == 'b':
        avantage *= -1
    return avantage

def meilleur_coup(plateau, qj, profondeur, a=-inf, b=+inf):
    if profondeur == 0:
        return '', evaluer(plateau, qj)

    score_max = -inf
    m_coup = ''
    etat0 = deepcopy(plateau.etat)
    p = Plateau()
    CP = ordonner(plateau.coups_possibles(qj))

    for coup in CP:

        p.etat = deepcopy(etat0)
        p.faire_coup(qj, coup)
        score = -meilleur_coup(p, switch(qj), profondeur - 1, -b, -a)[1]

        if score >= score_max:
            score_max = score
            m_coup = coup

        a = max(a, score_max)

        if a >= b:
            break

    return m_coup, score_max

def show(plateau):
    import numpy as np
    plateau.faire_coup('w', meilleur_coup(plateau, 'w', 3)[0])
    plateau.faire_coup('b', meilleur_coup(plateau, 'b', 3)[0])
    plateau.faire_coup('w', meilleur_coup(plateau, 'w', 4)[0])
    print(np.array([plateau.etat[k].nom()[:2] for k in range(len(plateau.etat))]).reshape(8, 8))
