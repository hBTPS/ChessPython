

self.coords = [
            'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
            'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
            'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
            'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
            'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
            'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
            'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
            'a1', 'b1', 'c1', 'd1', 'e1', 'f1' 'g1', 'h1']

def pos(self, coord):
    # return tuple(np.argwhere(self.coords == coord)[0])
        dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                'e': 4, 'f': 5, 'g': 6, 'h': 7}
        i, j = 8 - int(coord[1]), dict[coord[0]]
        return 8 * i + j

def pos(self, coord):
    # return tuple(np.argwhere(self.coords == coord)[0])
    dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
            'e': 4, 'f': 5, 'g': 6, 'h': 7}
    i, j = 8 - int(coord[1]), dict[coord[0]]
    return 8 * i + j

self.etat = ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr',
                     'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp',
                     None, None, None, None, None, None, None, None,
                     None, None, None, None, None, None, None, None,
                     None, None, None, None, None, None, None, None,
                     None, None, None, None, None, None, None, None,
                     'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp',
                     'br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br']

self.etat = [None for k in range(64)]
self.etat[:8] = ['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr']
self.etat[55:] = ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br']
self.etat[8:16] = 8 * ['wp']
self.etat[47:55] = 8 * ['bp']
if not white_up:
    self.etat[:8], self.etat[55:] = self.etat[55:], self.etat[:8]

P = Plateau()
P.deplacer(P.etat[4], 'a6')
P.deplacer(P.etat[2], 'a5')
P.deplacer(P.etat[59], 'a4')
# aligne roi et fou d'une même couleur et reine d'une autre couleur

print(P.echec(P.etat[16]))
P.deplacer(P.etat[24],'e3') # bouge fou
P.echec(P.etat[16]) # maintenant le roi est en échec par la reine

P = Plateau()
P.deplacer(P.etat[4], 'a6')
P.deplacer(P.etat[2], 'a5')
P.deplacer(P.etat[59], 'a4')
P.cases_vraiment_accessibles(P.etat[24]) # cases vraiment accessibles au fou

P = Plateau()
P.deplacer(P.etat[4], 'a6')
P.deplacer(P.etat[0], 'a5')
P.deplacer(P.etat[59], 'a4')
P.cases_vraiment_accessibles(P.etat[24]) # cases vraiment accessibles à la tour

P = Plateau()
P.deplacer(P.etat[4], 'a6')
P.deplacer(P.etat[2], 'a5')
P.deplacer(P.etat[59], 'a4')
P.deplacer(P.etat[24], 'b4')
P.echec(P.etat[16]) # vérifie que le roi est bien en échec

P = Plateau()
P.deplacer(P.etat[4], 'a6')
P.deplacer(P.etat[0], 'a5')
P.deplacer(P.etat[59], 'a4')
P.deplacer(P.etat[24], 'b4')
P.echec(P.etat[16]) # idem

P = Plateau()
P.cases_vraiment_accessibles(P.etat[1]) # vérifie que le cavalier n'a que 2 cases possibles au début

P = Plateau()
P.deplacer(P.etat[4], 'a5') # roi noir en a5
P.deplacer(P.etat[59], 'b5') # reine blanche en b5
P.deplacer(P.etat[57], 'c3') # cavalier blanc en c3
P.qj = 'b'
P.mat()

P = Plateau()
P.deplacer(P.etat[4], 'a5') # roi noir en a5
P.deplacer(P.etat[59], 'b5') # reine blanche en b5
P.coups_possibles('b')

# test cases_entre
P = Plateau()
P.deplacer(P.etat[1], 'b4')
P.deplacer(P.etat[0], 'f4')
P.cases_entre(P.etat[P.coords['b4']], P.etat[P.coords['f4']])

# test peut_roquer
P = Plateau()
P.deplacer(P.etat[1], 'c3')
P.deplacer(P.etat[2], 'd4')
P.deplacer(P.etat[3], 'e4')
print(P.peut_roquer('b'))

P = Plateau()
P.deplacer(P.etat[5], 'c3')
P.deplacer(P.etat[6], 'd4')
print(P.peut_roquer('b'))
print(P.coups_possibles('b'))

# test roque
P = Plateau()
P.deplacer(P.etat[5], 'c3')
P.deplacer(P.etat[6], 'd4')
P.deplacer(P.etat[4], 'g8')
print([p.nom() for p in P.etat[4:8]])

P = Plateau()
P.deplacer(P.etat[1], 'c3')
P.deplacer(P.etat[2], 'd4')
P.deplacer(P.etat[3], 'e4')
P.deplacer(P.etat[4], 'c8')
print([p.nom() for p in P.etat[:5]])

# Test coups_possibles

P = Plateau()
P.deplacer(P.etat[0], 'a3')
P.deplacer(P.etat[7], 'd3')
P.coups_possibles('b')

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for x in range(8):
    for y in range(8):
        w = QLabel()

        if (x + y) % 2 == 1:
            w.setStyleSheet('background-color: #779952')
        else:
            w.setStyleSheet('background-color: #edeed1')

        if (y == 0) and (x == 7):
            w.setText(str(8 - x))
            w.setFont(QFont('Arial', 15))
            w.setAlignment(Qt.AlignTop | Qt.AlignLeft)
            layout.addWidget(w, x, y)

            w2 = QLabel()
            w2.setText(columns[y])
            w2.setFont(QFont('Arial', 15))
            w2.setAlignment(Qt.AlignBottom | Qt.AlignRight)
            layout.addWidget(w2, x, y)

            continue

        if y == 0:
            w.setText(str(8 - x))
            w.setFont(QFont('Arial', 15))
            w.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        if x == 7:
            w.setText(columns[y])
            w.setFont(QFont('Arial', 15))
            w.setAlignment(Qt.AlignBottom | Qt.AlignRight)

        layout.addWidget(w, x, y)

P = Plateau()
P.deplacer(P.etat[1], 'c4')
P.deplacer(P.etat[2], 'c5')
P.deplacer(P.etat[3], 'd4')
P.deplacer(P.etat[5], 'e4')
P.deplacer(P.etat[6], 'e5')
P.peut_roquer('b')
P.petit_roque('b')
print([P.etat[k].nom() for k in range(8)])

# class Color(QWidget):
#
#     def __init__(self, color, *args, **kwargs):
#         super(Color, self).__init__(*args, **kwargs)
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)

# h = QHBoxLayout() # column name
        # L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # for i in range(8):
        #     wi = QLabel(L[i])
        #     wi.setStyleSheet('font: bold 20px')
        #     wi.setAlignment(Qt.AlignBottom | Qt.AlignRight)
        #     h.addWidget(wi)
        # layout.addLayout(h.layout(), 7, 0, 1, 0)

path = "C:\\Users\\Hadrien\\Documents\\ENSTA 1A\\UE 2.4 Projet\\PGN games\\OwnGame2.pgn"

def show_game():
    app = QApplication(sys.argv)
    window = MainWindow()

    P = Plateau()
    window.afficher_etat(P)
    window.show()
    app.exec_()

    d = pgn_to_dict(path)

    for tour in d:
        print(d[tour][0])
        P.faire_coup(P.qj, d[tour][0])
        window.afficher_etat(P)
        window.show()
        app.exec_()

        print(d[tour][1])
        P.faire_coup(P.qj, d[tour][1])
        window.afficher_etat(P)
        window.show()
        app.exec_()


app = QApplication(sys.argv)
window = MainWindow()
P = Plateau()
window.afficher_etat(P)
window.show()
app.exec_()

if piece.nom()[1] == 'k' and abs(j - i) > 1:  # cas du roque
    self.etat[j] = self.etat[i]
    self.etat[i] = Vide()
    self.etat[i].coord = piece.coord
    self.etat[j].coord = coord
    if j >= i:
        coord1, coord3 = self.etat[i + 1].coord, self.etat[i + 3].coord
        self.etat[i + 1] = self.etat[i + 3]
        self.etat[i + 3] = Vide()
        self.etat[i + 3].coord = coord3
        self.etat[i + 1].coord = coord1
    else:
        coord1, coord4 = self.etat[i - 1].coord, self.etat[i - 4].coord
        self.etat[i - 1] = self.etat[i - 4]
        self.etat[i - 4] = Vide()
        self.etat[i - 4].coord = coord4
        self.etat[i - 1].coord = coord1

P = Plateau()
P.deplacer(P.etat[51], 'd4')
P.deplacer(P.etat[12], 'e5')
meilleur_coup(P, 'w', 2)

P = Plateau()
P.deplacer(P.etat[51], 'd4')
P.deplacer(P.etat[12], 'e5')
P.faire_coup(P.etat[35], 'd5')
P.etat[27]

def reset(etat0, etat1):
    etat0, etat1 = np.array(etat0), np.array(etat1)
    p0 = np.array([etat0[k].val for k in range(len(etat0))])
    p1 = np.array([etat1[k].val for k in range(len(etat1))])
    for i in range(len((p0 != p1))):
        if (p0 != p1)[i]:
            nom = etat0[i].nom()[1]
            if nom == 'n':
                etat1[i] = Cavalier()
            elif nom == 'b':
                etat1[i] = Fou()
            elif nom == 'q':
                etat1[i] = Reine()
            elif nom == 'k':
                etat1[i] = Roi()
            elif nom == 'r':
                etat1[i] = Tour()
            elif nom == 'p':
                etat1[i] = Pion()
            elif nom == 'i':
                etat1[i] = Vide()

P = Plateau()
etat0 = deepcopy(P.etat)
P.deplacer(P.etat[0], 'c5')
reset(etat0, P)

# if piece.nom()[1] == 'k' and self.echec(piece.couleur)[0]:
            #     if abs(int(self.coords[case]) - int(self.coords[piece.coord])) == 2:
            #         CVA.remove(case)
            #         continue


# def cases_vraiment_accessibles(self, piece):
#     CVA = self.cases_accessibles(piece)
#     CVA_copy = CVA.copy()
#
#     etat0 = self.etat.copy()
#
#     for case in CVA_copy:
#
#         if piece.nom()[1] == 'k' and abs(int(self.coords[case]) - int(self.coords[piece.coord])) == 2:
#             camp = piece.couleur
#             i = int(camp != 'w')
#             if self.echec(camp)[0] or any(n in value[i] for value in self.h.values() for n in [camp + 'k', camp + 'r']):
#                 CVA.remove(case)
#                 continue
#
#         P = Plateau()
#         P.etat = deepcopy(etat0)
#         P.deplacer(piece, case)
#
#         if P.echec(piece.couleur)[0]:
#             CVA.remove(case)
#
#     return CVA
#
#
# def peut_roquer(self, camp):
#     # retourne petit_roque, grand_roque (booleens)
#     if self.echec(camp)[0]:
#         return False, False
#
#     i = 0 if camp == 'w' else 1
#     for key, value in self.h.items():
#         if any(n in value[i] for n in [camp + 'k', camp + 'r']):
#             # si le roi ou une tour a été bougé
#             return False, False
#
#     petit_roque, grand_roque = False, False
#
#     if camp == 'w':
#         tour1, tour2, roi = self.etat[56], self.etat[63], self.etat[60]
#     else:
#         tour1, tour2, roi = self.etat[0], self.etat[7], self.etat[4]
#
#     L1 = self.cases_entre(roi, tour1)[1:]
#     L2 = self.cases_entre(roi, tour2)
#
#     if all(k in self.cases_vraiment_accessibles(roi) for k in L2) and len(L2) == 2:
#         petit_roque = True
#     if all(k in self.cases_vraiment_accessibles(roi) for k in L1) and len(L1) == 2:
#         grand_roque = True
#
#     return petit_roque, grand_roque

P = Plateau()
P.deplacer(P.etat[1], 'c4')
P.deplacer(P.etat[2], 'c5')
P.deplacer(P.etat[3], 'd4')
P.deplacer(P.etat[5], 'e4')
P.deplacer(P.etat[6], 'e5')

P.deplacer(P.etat[4], 'g8')
P.annuler_coup('e8', 'g8', 'Vide')

P = Plateau()
P.deplacer(P.etat[51], 'd4')
P.deplacer(P.etat[12], 'e5')
P.faire_coup('w', 'd5')
P.etat[27]

P = Plateau()
P.deplacer(P.etat[51], 'd4')
P.deplacer(P.etat[12], 'e5')
P.faire_coup('w', 'dxe5')
print(P.etat[28].nom(), P.etat[28].val)
P.annuler_coup()
print(P.etat[28].nom(), P.etat[28].val)

P = Plateau()
P.deplacer(P.etat[1], 'c4')
P.deplacer(P.etat[2], 'c5')
P.deplacer(P.etat[3], 'd4')
P.deplacer(P.etat[5], 'e4')
P.deplacer(P.etat[6], 'e5')
P.faire_coup('b', 'O-O')
print(P.etat[4:8])
P.annuler_coup()
print(P.etat[4:8])


P = Plateau()
P.deplacer(P.etat[4], 'c5')
P.deplacer(P.etat[59], 'c6')
print(P.echec('b')[0])
print(P.coups_possibles('b'))
print(P.coups_possibles('w'))

P = Plateau()
P.deplacer(P.etat[13], 'f5')
P.deplacer(P.etat[4], 'f7')
P.annuler_coup()
P.roi('b').coord

P = Plateau()
P.deplacer(P.etat[P.coords['c2']], 'c3')
print(P.etat[P.coords['c2']].val, P.etat[P.coords['c3']].val)
P.annuler_coup()
print(P.etat[P.coords['c2']].val, P.etat[P.coords['c3']].val)

# [<Pieces.Tour at 0x21ca253d160>,
#  <Pieces.Cavalier at 0x21ca253d1c0>,
#  <Pieces.Fou at 0x21ca253d220>,
#  <Pieces.Reine at 0x21ca253d250>,
#  <Pieces.Roi at 0x21ca253d2e0>,
#  <Pieces.Fou at 0x21ca253d340>,
#  <Pieces.Cavalier at 0x21ca253d3a0>,
#  <Pieces.Pion at 0x21ca251cfa0>,
#  <Pieces.Pion at 0x21ca253d460>,
#  <Pieces.Pion at 0x21ca253d4c0>,
#  <Pieces.Pion at 0x21ca253d550>,
#  <Pieces.Pion at 0x21ca253d5b0>,
#  <Pieces.Pion at 0x21ca253d610>,
#  <Pieces.Vide at 0x21ca251cc70>,
#  <Pieces.Vide at 0x21ca253d820>,
#  <Pieces.Vide at 0x21ca251c250>,
#  <Pieces.Vide at 0x21ca253d910>,
#  <Pieces.Vide at 0x21ca253daf0>,
#  <Pieces.Vide at 0x21ca253d7c0>,
#  <Pieces.Vide at 0x21ca253d940>,
#  <Pieces.Vide at 0x21ca253d400>,
#  <Pieces.Vide at 0x21ca251cd60>,
#  <Pieces.Vide at 0x21ca251cdc0>,
#  <Pieces.Vide at 0x21ca253db80>,
#  <Pieces.Vide at 0x21ca253d880>,
#  <Pieces.Vide at 0x21ca251b3a0>,
#  <Pieces.Vide at 0x21ca253deb0>,
#  <Pieces.Vide at 0x21ca253dee0>,
#  <Pieces.Vide at 0x21ca251ccd0>,
#  <Pieces.Vide at 0x21ca251c1f0>,
#  <Pieces.Vide at 0x21ca251c640>,
#  <Pieces.Vide at 0x21ca253df70>,
#  <Pieces.Pion at 0x21ca251c3a0>,
#  <Pieces.Pion at 0x21ca251c400>,
#  <Pieces.Vide at 0x21ca253da90>,
#  <Pieces.Vide at 0x21ca251c0d0>,
#  <Pieces.Vide at 0x21ca251cd00>,
#  <Pieces.Vide at 0x21ca251cc10>,
#  <Pieces.Vide at 0x21ca251ceb0>,
#  <Pieces.Vide at 0x21ca251ca30>,
#  <Pieces.Vide at 0x21ca253dd30>,
#  <Pieces.Vide at 0x21ca253d700>,
#  <Pieces.Pion at 0x21ca251c460>,
#  <Pieces.Vide at 0x21ca251b220>,
#  <Pieces.Vide at 0x21ca251cf70>,
#  <Pieces.Vide at 0x21ca253dc70>,
#  <Pieces.Vide at 0x21ca251ce20>,
#  <Pieces.Vide at 0x21ca253dac0>,
#  <Pieces.Vide at 0x21ca251c130>,
#  <Pieces.Vide at 0x21ca253d850>,
#  <Pieces.Vide at 0x21ca253da60>,
#  <Pieces.Pion at 0x21ca251c4c0>,
#  <Pieces.Pion at 0x21ca251c520>,
#  <Pieces.Pion at 0x21ca251c580>,
#  <Pieces.Pion at 0x21ca251c5e0>,
#  <Pieces.Pion at 0x21ca251cca0>,
#  <Pieces.Tour at 0x21ca251c6a0>,
#  <Pieces.Cavalier at 0x21ca251c700>,
#  <Pieces.Fou at 0x21ca251c760>,
#  <Pieces.Reine at 0x21ca251c7c0>,
#  <Pieces.Roi at 0x21ca251c820>,
#  <Pieces.Fou at 0x21ca251c880>,
#  <Pieces.Cavalier at 0x21ca251c8e0>,
#  <Pieces.Tour at 0x21ca251c940>]

P = Plateau()
P.faire_coup('w', 'd4')
P.faire_coup('b', 'e5')
P.faire_coup('w', 'dxe5')
P.faire_coup('b', 'd5')
P.faire_coup('w', 'dxd6')
P.faire_coup('b', 'Qxd6')
# print('d6' in P.cases_vraiment_accessibles(P.etat[P.coords['d8']]))

# print(P.roi('b').coord)

