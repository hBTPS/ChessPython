from Plateau import *

def lancer_partie():

    P = Plateau()
    n = -1

    while not P.mat():
        n += 1
        print("Au tour des", ["blancs", "noirs"][n % 2])

        I = input("case de départ")[1:3]
        if I == "ab": # abandon
            break
        CVA = P.cases_vraiment_accessibles(P.etat[P.coords[I]])
        while len(CVA) == 0:
            print("impossible de bouger cette pièce")
            I = input("case de départ")[1:3]
            CVA = P.cases_vraiment_accessibles(P.etat[P.coords[I]])
        print("cases accessibles :", CVA)
        J = input("case d'arrivée")[1:3]
        while J not in CVA:
            print("cette case n'est pas accessible")
            J = input("case d'arrivée")[1:3]

        for piece in P.etat:
            if piece.coord == I:
                P.deplacer(piece, J)