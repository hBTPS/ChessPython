from Pieces import *
from copy import deepcopy

class Plateau:

    def __init__(self, white_up=False):

        self.white_up = white_up

        self.coords = {'a8': 0, 'b8': 1, 'c8': 2, 'd8': 3, 'e8': 4, 'f8': 5, 'g8': 6, 'h8': 7,
                       'a7': 8, 'b7': 9, 'c7': 10, 'd7': 11, 'e7': 12, 'f7': 13, 'g7': 14, 'h7': 15,
                       'a6': 16, 'b6': 17, 'c6': 18, 'd6': 19, 'e6': 20, 'f6': 21, 'g6': 22, 'h6': 23,
                       'a5': 24, 'b5': 25, 'c5': 26, 'd5': 27, 'e5': 28, 'f5': 29, 'g5': 30, 'h5': 31,
                       'a4': 32, 'b4': 33, 'c4': 34, 'd4': 35, 'e4': 36, 'f4': 37, 'g4': 38, 'h4': 39,
                       'a3': 40, 'b3': 41, 'c3': 42, 'd3': 43, 'e3': 44, 'f3': 45, 'g3': 46, 'h3': 47,
                       'a2': 48, 'b2': 49, 'c2': 50, 'd2': 51, 'e2': 52, 'f2': 53, 'g2': 54, 'h2': 55,
                       'a1': 56, 'b1': 57, 'c1': 58, 'd1': 59, 'e1': 60, 'f1': 61, 'g1': 62, 'h1': 63}

        T = self.coords.copy()
        for key, value in T.items():
            self.coords[value] = key

        self.etat = [
            Tour(), Cavalier(), Fou(), Reine(), Roi(), Fou(), Cavalier(), Tour(),
            Pion(), Pion(), Pion(), Pion(), Pion(), Pion(), Pion(), Pion(),
            Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(),
            Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(),
            Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(),
            Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(), Vide(),
            Pion(), Pion(), Pion(), Pion(), Pion(), Pion(), Pion(), Pion(),
            Tour(), Cavalier(), Fou(), Reine(), Roi(), Fou(), Cavalier(), Tour()]

        for i, piece in enumerate(self.etat):
            piece.coord = self.coords[i]
            if i < 16:
                piece.couleur = 'w' if white_up else 'b'
            elif i > 47:
                piece.couleur = 'b' if white_up else 'w'

        self.tab120 = [
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, 0, 1, 2, 3, 4, 5, 6, 7, -1,
            -1, 8, 9, 10, 11, 12, 13, 14, 15, -1,
            -1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
            -1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
            -1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
            -1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
            -1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
            -1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

        self.tab64 = [
            21, 22, 23, 24, 25, 26, 27, 28,
            31, 32, 33, 34, 35, 36, 37, 38,
            41, 42, 43, 44, 45, 46, 47, 48,
            51, 52, 53, 54, 55, 56, 57, 58,
            61, 62, 63, 64, 65, 66, 67, 68,
            71, 72, 73, 74, 75, 76, 77, 78,
            81, 82, 83, 84, 85, 86, 87, 88,
            91, 92, 93, 94, 95, 96, 97, 98]

        self.w = 'up' if white_up else 'down'

        self.qj = 'w'  # "qui joue", aux blancs de commencer

        self.t = 1  # n° du tour

        self.h = {}  # historique

        self.dc = []

        self.en_passant = False

    def liste_coups(self):
        liste_coups = []
        for liste in list(self.h.values()):
            for el in liste:
                if el != '':
                    liste_coups.append(el)
        return liste_coups

    def dernier_coup(self):
        if len(self.h) >= 1:
            return self.liste_coups()[-1]

    def cases_accessibles(self, piece): # cases a priori accessibles selon le vecteur dpl de la piece
        """ incomplet: cas de la prise en passant du pion """
        dpl = piece.deplacements() # vecteur déplacement
        CA = [] # liste des coups possibles

        i = self.tab64[self.coords[piece.coord]] # valeur correspondant à la position de la piece dans tab64
        for k in dpl: # vecteur élémentaire
            s = self.tab120[i + k]

            if s == -1:  # sortie de plateau
                continue
            else:
                if piece.nom()[1] not in ('n', 'p', 'k'):
                    l = k
                    while s != -1:  # tant qu'on reste sur le plateau
                        if self.etat[s].val != 0:  # si pièce rencontree
                            if self.etat[s].couleur != piece.couleur:
                                CA.append(self.coords[s])  # pièce prenable si d'une autre couleur
                            break # on s'arrête quand une pièce est prise
                        else:  # sinon toute case vide est accessible
                            CA.append(self.coords[s])
                            k += l
                            s = self.tab120[i + k]

                elif piece.nom()[1] in ('n', 'k'):  # Pour cavalier/roi, CA se limite a priori à dpl
                    # (hors cases déjà occupées par une pièce du même camp)
                    if self.etat[s].couleur != piece.couleur:
                            CA.append(self.coords[s])
                    if piece.nom()[1] == 'k' and k in (-1, 1): # a priori roques possibles
                        if (piece.coord == 'e1' and piece.couleur == 'w') or \
                                (piece.coord == 'e8' and piece.couleur == 'b'):
                            s2 = self.tab120[i + 2*k]
                            if s2 != -1 and self.etat[s2].val == 0:
                                CA.append(self.coords[s2])


                else:  # cas du pion
                    if k in (9, 11, -9, -11):  # cas où le pion est susceptible de manger une pièce
                        if (self.etat[s].val != 0) and (self.etat[s].couleur != piece.couleur):
                            if (k >= 0 and piece.couleur == 'b') or (k <= 0 and piece.couleur == 'w'):
                                CA.append(self.coords[s])

                        # cas de la prise en passant
                        dernier_coup = self.dernier_coup()
                        liste_coups = self.liste_coups()

                        cd, cg = '', ''
                        if self.tab120[i+1] != -1:
                            cd = self.coords[self.tab120[i+1]] # case à droite
                        if self.tab120[i-1] != -1:
                            cg = self.coords[self.tab120[i-1]] # case à gauche

                        if k in (9, 11) and piece.couleur == 'b':
                            if 'wp' + self.coords[s] not in liste_coups:
                                if (k == 9 and dernier_coup == 'wp' + cg) or (k == 11 and dernier_coup == 'wp' + cd):
                                    CA.append(self.coords[s])

                        elif k in (-9, -11) and piece.couleur == 'w':
                            if 'bp' + self.coords[s] not in liste_coups:
                                if (k == -9 and dernier_coup == 'bp' + cd) or (k == -11 and dernier_coup == 'bp' + cg):
                                    CA.append(self.coords[s])


                    else: # si déplacement d'une ou deux cases verticalement
                        if self.etat[s].val == 0:
                            if k in (-20, 20):  # cas où le pion peut avancer de deux cases
                                if piece.coord[1] in ('2', '7'):
                                # possible si le pion est à sa position initiale
                                    CA.append(self.coords[s])
                            else:
                                if (k == 10 and piece.couleur == 'b') or (k == -10 and piece.couleur == 'w'):
                                    CA.append(self.coords[s])

        return CA

    def cases_entre(self, p1, p2):
        L = []

        same_color = False
        if p1.couleur == p2.couleur: # pour renvoyer cases entre deux pièces de même couleur
            same_color = True
            color0 = p1.couleur
            p1.couleur = 'b' if p2.couleur == 'w' else 'w'

        CA1, CA2 = self.cases_accessibles(p1), self.cases_accessibles(p2)

        if (p1.coord in CA2) or (p2.coord in CA1):

            if p1.coord in CA2:
                pi, pj = p1, p2
            elif p2.coord in CA1:
                pi, pj = p2, p1

            dpl = pj.deplacements()
            i = self.tab64[self.coords[pj.coord]]

            for k in dpl:
                l = 1
                s = self.tab120[i + k * l]
                while s != -1:
                    c = self.coords[s]
                    if c == pi.coord:
                        L = [self.coords[self.tab120[i + k * j]] for j in range(1, l)]
                        if same_color: p1.couleur = color0
                        return L
                    l += 1
                    s = self.tab120[i + k * l]

        if same_color: p1.couleur = color0 # redonne bonne couleur à p1

        return L

    def roi(self, camp):
        for piece in self.etat:
            if piece.val is None and piece.couleur == camp:
                return piece


    def echec(self, camp):
        roi = self.roi(camp)
        for piece in self.etat:
            if piece.couleur != roi.couleur and piece.val != 0:
                CA = self.cases_accessibles(piece)
                if roi.coord in CA:
                    return True, self.cases_entre(roi, piece) + [piece.coord]
        return False, []

    def deplacer(self, piece, coord): # coord au format 'a8'
        """ déplace piece à la position coord. mange toute piece présente sur coord """
        i, j = self.coords[piece.coord], self.coords[coord]
        self.dc.append([piece.coord, coord, self.etat[j].nom()])

        if piece.nom()[1] == 'p':

            en_passant = (self.etat[j].val == 0) and (abs(j-i) in [7, 9])

            if piece.coord[1] == '2' and piece.couleur == 'b':
                self.etat[j] = Reine()
                self.etat[j].couleur = 'b'
            elif piece.coord[1] == '7' and piece.couleur == 'w':
                self.etat[j] = Reine()
                self.etat[j].couleur = 'w'
            else:
                self.etat[j] = self.etat[i]

            if en_passant:
                self.en_passant = True
                if j-i in [-7, 9]:
                    self.etat[i+1] = Vide()

                elif j-i in [-9, 7]:
                    self.etat[i-1] = Vide()

            self.etat[i] = Vide()
            self.etat[i].coord = piece.coord
            self.etat[j].coord = coord

        elif piece.nom()[1] == 'k' and abs(j - i) == 2:  # cas du roque
            self.etat[j] = self.etat[i]
            self.etat[i] = Vide()
            self.etat[i].coord = piece.coord
            self.etat[j].coord = coord
            if j == i + 2:
                coord1, coord3 = self.etat[i + 1].coord, self.etat[i + 3].coord
                self.etat[i + 1] = self.etat[i + 3]
                self.etat[i + 3] = Vide()
                self.etat[i + 3].coord = coord3
                self.etat[i + 1].coord = coord1
            elif j == i - 2:
                coord1, coord4 = self.etat[i - 1].coord, self.etat[i - 4].coord
                self.etat[i - 1] = self.etat[i - 4]
                self.etat[i - 4] = Vide()
                self.etat[i - 4].coord = coord4
                self.etat[i - 1].coord = coord1

        else:
            self.etat[j] = self.etat[i]
            self.etat[i] = Vide()
            self.etat[i].coord = piece.coord
            self.etat[j].coord = coord

        if self.qj == 'w':
            self.h[self.t] = [piece.nom()+coord, '']

        else:
            self.h[self.t][1] = piece.nom() + coord
            self.t += 1

        self.qj = 'b' if self.qj == 'w' else 'w'

    def peut_roquer(self, camp):
        # retourne petit_roque, grand_roque (booleens)

        i = 0 if camp == 'w' else 1
        for key, value in self.h.items():
            if any(n in value[i] for n in [camp + 'k', camp + 'r']):
                # si le roi ou une tour a été bougé
                return False, False

        petit_roque, grand_roque = True, True

        if camp == 'w':
            if [self.etat[k].nom() for k in range(61, 63)] != 2 * ['Vide']:
                petit_roque = False
            if [self.etat[k].nom() for k in range(57, 60)] != 3 * ['Vide']:
                grand_roque = False

        elif camp == 'b':
            if [self.etat[k].nom() for k in range(5, 7)] != 2 * ['Vide']:
                petit_roque = False
            if [self.etat[k].nom() for k in range(1, 4)] != 3 * ['Vide']:
                grand_roque = False

        if (not petit_roque) and (not grand_roque):
            return False, False

        # petit_roque, grand_roque = True, True

        if camp == 'w':
            tour1, tour2, roi = self.etat[56], self.etat[63], self.etat[60]
        else:
            tour1, tour2, roi = self.etat[0], self.etat[7], self.etat[4]

        L1 = self.cases_entre(roi, tour1) + [roi.coord]
        L2 = self.cases_entre(roi, tour2) + [roi.coord]

        L = [L1, L2]
        #print(L)
        for i in range(len(L)):
            for case in L[i]:
                for piece in self.etat:
                    if piece.couleur != camp and case in self.cases_accessibles(piece):
                        if i == 0:
                            grand_roque = False
                        elif i == 1:
                            petit_roque = False

        return petit_roque, grand_roque

    def cases_vraiment_accessibles(self, piece):
        CVA = self.cases_accessibles(piece)

        if piece.val is None:
            petit_roque, grand_roque = self.peut_roquer(piece.couleur)
            L = ['g1', 'c1'] if piece.couleur == 'w' else ['g8', 'c8']
            if not petit_roque and L[0] in CVA:
                CVA.remove(L[0])
            if not grand_roque and L[1] in CVA:
                CVA.remove(L[1])

        CVA_test = CVA.copy()
        P2 = Plateau()
        etat0 = deepcopy(self.etat)

        for case in CVA_test:
            P2.etat = deepcopy(etat0)
            P2.deplacer(piece, case)
            if P2.echec(piece.couleur)[0]:
                CVA.remove(case)

        return CVA

    def petit_roque(self, camp):
        if self.peut_roquer(camp)[0]:
            roi = self.roi(camp)
            i = self.coords[roi.coord]
            j = i + 2
            coord = self.coords[j]
            self.deplacer(roi, coord)

    def grand_roque(self, camp):
        if self.peut_roquer(camp)[1]:
            roi = self.roi(camp)
            i = self.coords[roi.coord]
            j = i - 2
            coord = self.coords[j]
            self.deplacer(roi, coord)

    def mat(self):
        roi = self.roi(self.qj)
        echec, L = self.echec(roi.couleur)
        if echec and len(self.cases_vraiment_accessibles(roi)) == 0:
            for piece in self.etat:
                if piece.couleur == roi.couleur:
                    CVA = self.cases_vraiment_accessibles(piece)
                    for c in L:
                        if c in CVA:
                            return False
            return True
        return False

    def pat(self):
        # if len(self.cases_atteignables(self.qj)) == 0:
        if len(self.coups_possibles(self.qj)) == 0:
            return True
        return False

    def coup(self, piece, coord):
        a = ''
        if self.etat[self.coords[coord]].val != 0:
            a = 'x'
        else:
            i, j = self.coords[piece.coord], self.coords[coord]
            if piece.nom()[1] == 'p' and abs(j - i) in [7, 9]: # prise en passant
                a = 'x'
        nom = piece.nom()[1]
        if nom == 'p':
            if a == 'x':
                return piece.coord[0] + a + coord
            else:
                return coord
        elif nom == 'k':
            dx = self.coords[coord] - self.coords[piece.coord]
            if dx == 2:
                return 'O-O'
            elif dx == -2:
                return 'O-O-O'
            else:
                return nom.upper() + a + coord
        else:
            nom_complet = piece.nom()
            pieces_identiques = []
            for p in self.etat:
                if p.nom() == nom_complet and p.coord != piece.coord:
                    CVA = self.cases_vraiment_accessibles(p)
                    if coord in CVA:
                        pieces_identiques.append(p)
            n = len(pieces_identiques)
            if n == 0:
                return nom.upper() + a + coord
            elif n >= 1:
                for p in pieces_identiques:
                    if piece.coord[0] != p.coord[0]:
                        return nom.upper() + piece.coord[0] + a + coord
                    elif piece.coord[1] != p.coord[1]:
                        return nom.upper() + piece.coord[1] + a + coord
                return nom.upper() + piece.coord + a + coord

    # def coups_possibles(self, camp):
    #     CP = []
    #     for piece in self.etat:
    #         if piece.couleur == camp:
    #             CVA = self.cases_vraiment_accessibles(piece)
    #             for case in CVA:
    #                 CP.append(self.coup(piece, case))
    #     return CP

    def coups_possibles(self, camp):
        CP = []
        for piece in self.etat:
            if piece.couleur == camp:
                CVA = self.cases_vraiment_accessibles(piece)
                CP += [self.coup(piece, case) for case in CVA]
        return CP

    def faire_coup(self, camp, coup):
        # NAA : Notation algébrique abrégée anglaise
        # traduit coup NAA en déplacement pour la méthode déplacer
        # types de coups: e2 Nf3 Nef3 Nxf3 Rcxd3 exd5 O-O O-O-O

        coup = coup.replace('x', '')
        l = len(coup)

        for p in self.etat:
            if p.couleur == camp:
                # CVA = self.cases_vraiment_accessibles(p)
                CVA = self.cases_accessibles(p)

                if l == 2 and p.val == 1:
                    case = coup
                    if case in CVA:
                        self.deplacer(p, case)
                elif l == 3 and p.nom()[1].upper() == coup[0]:
                    case = coup[1:]
                    if case in CVA:
                        self.deplacer(p, case)
                elif l == 3 and coup[0].islower(): # cas du pion
                    case = coup[1:]
                    if p.coord[0] == coup[0] and case in CVA:
                        self.deplacer(p, case)
                elif l == 4 and p.nom()[1].upper() == coup[0] and (coup[1] in [p.coord[0], p.coord[1]]):
                    case = coup[2:]
                    if case in CVA:
                        self.deplacer(p, case)
                elif coup == "O-O":
                    self.petit_roque(camp)
                elif coup == "O-O-O":
                    self.grand_roque(camp)

    def annuler_coup(self):
        c0, c1, nom_p1 = self.dc[-1]

        if nom_p1 == 'Vide':
            nom_p1 = '-i'


        if self.etat[self.coords[c1]].nom()[1] == 'k' and abs(int(self.coords[c1]) - int(self.coords[c0])) == 2:
            dx = int(self.coords[c1]) - int(self.coords[c0])
            clr = self.etat[self.coords[c1]].couleur
            a = 60 if clr == 'w' else 4

            if dx == 2:

                self.etat[a + 3] = Tour()
                self.etat[a + 3].couleur = clr
                self.etat[a + 3].coord = self.coords[a + 3]

                self.etat[a] = Roi()
                self.etat[a].couleur = clr
                self.etat[a].coord = c0

                self.etat[a + 2] = Vide()
                self.etat[a + 2].coord = c1

                self.etat[a + 1] = Vide()
                self.etat[a + 1].coord = self.coords[a + 1]


            elif dx == -2:

                self.etat[a - 4] = Tour()
                self.etat[a - 4].couleur = clr
                self.etat[a - 4].coord = self.coords[a + 3]

                self.etat[a] = Roi()
                self.etat[a].couleur = clr
                self.etat[a].coord = c0

                self.etat[a - 2] = Vide()
                self.etat[a - 2].coord = c1

                self.etat[a - 1] = Vide()
                self.etat[a - 1].coord = self.coords[a - 1]

        else:
            for piece in [Tour(), Fou(), Cavalier(), Reine(), Roi(), Pion(), Vide()]:
                if piece.nom()[1] == nom_p1[1]:
                    p1 = piece
                    p1.couleur = nom_p1[0]
                    p1.coord = c1
            p0 = self.etat[self.coords[c1]]
            self.etat[self.coords[c0]] = p0
            self.etat[self.coords[c0]].coord = c0
            self.etat[self.coords[c1]] = p1

            if self.en_passant and p0.val == 1:
                self.etat[self.coords[c1[0] + c0[1]]] = Pion()
                self.etat[self.coords[c1[0] + c0[1]]].coord = c1[0] + c0[1]
                clr = 'w' if p0.couleur == 'b' else 'b'
                self.etat[self.coords[c1[0] + c0[1]]].couleur = clr
            self.en_passant = False

        self.dc.pop()

        key = len(self.h)
        value = self.h[key]

        if value[1] != '':
            value[1] = ''
            self.t -= 1
            self.qj = 'b'
        else:
            del self.h[key]
            self.qj = 'w'

if __name__ == "main" :
    P = Plateau()
    L = P.cases_accessibles(P.etat[P.coords["g1"]])
    print(L)