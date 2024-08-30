from numpy import inf

def switch(qj):
    qj = 'w' if qj == 'b' else 'b'
    return qj


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


def negaMax_alphaBeta(plateau, qj, profondeur, a=-inf, b=+inf):

    if profondeur == 0:
        return evaluer(plateau, qj)

    score_max = -inf
    CP = plateau.coups_possibles(qj)

    for coup in CP:

        plateau.faire_coup(qj, coup)

        score_max = max(score_max, -negaMax_alphaBeta(plateau, switch(qj), profondeur - 1, -b, -a))

        plateau.annuler_coup()

        a = max(a, score_max)

        if a >= b:
            break

    return score_max


def meilleur_coup(plateau, qj, profondeur, a=-inf, b=+inf):
    meilleur_coup, score = '', -inf
    for coup in plateau.coups_possibles(qj):
        plateau.faire_coup(qj, coup)
        score_coup = -negaMax_alphaBeta(plateau, switch(qj), profondeur - 1, a, b)
        plateau.annuler_coup()
        if score_coup >= score:
            meilleur_coup, score = coup, score_coup
    return meilleur_coup, score
