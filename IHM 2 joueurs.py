import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Plateau import *

L, i = [], 0
coups, cases, etats = [], [], [deepcopy(Plateau().etat)]
echec = [False, ""]
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
folder_path = 'C:\\Users\\Hadrien\\Documents\\ENSTA\\UE 4.2 Traitement et communication des donnees\\Conception logicielle\\Chess\\Chess pieces\\'

class MainWindow(QMainWindow):
    """ Sous-classe de la classe PyQt QMainWindow.
    On y construit une fenêtre et des méthodes d'affichage d'objets désirés"""

    def __init__(self, *args, **kwargs):
        """ Constructeur: hérité de MainWindow. On y définit les paramètres de la fenêtre
        (titre, taille, position) et on la remplit d'un canvas, sur lequel il sera possible
        de 'peindre' avec un QPainter """

        super(MainWindow, self).__init__(*args, **kwargs)

        # Window
        self.setWindowTitle("Chess")
        self.setGeometry(300, 100, 1400, 1000)
        self.setFixedSize(self.size())

        self.w, self.h = 1000, self.height()
        self.wc, self.hc = int(self.w/8), int(self.h/8)

        # Canvas
        self.label = QLabel()
        canvas = QPixmap(self.size())
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def draw_layout(self, painter, plateau):
        """ Méthode principale
        Variables d'entrée: painter, plateau
        self.draw_layout est déclenchée sur paintEvent
        On y définit tout ce que l'on souhaite afficher (en l'occurence l'état du
        plateau au moment où on appelle cette méthode) """

        global L, coups, cases, echec, abc, folder_path

        # Background layout
        green, beige = QColor('#779952'), QColor('#edeed1')
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 1:
                    painter.setBrush(green)
                    painter.setPen(green)
                else:
                    painter.setBrush(beige)
                    painter.setPen(beige)

                painter.drawRect(x * self.wc, y * self.hc, self.wc, self.hc)

        for y in range(1, 9):
            if y % 2 == 1:
                painter.setPen(green)
            else:
                painter.setPen(beige)
            painter.setFont(QFont("Arial", 15))
            painter.drawText(0, y * self.hc - 100, str(9 - y))

        for x in range(8):
            if x % 2 == 1:
                painter.setPen(green)
            else:
                painter.setPen(beige)
            painter.setFont(QFont("Arial", 15))
            painter.drawText(105 + x * self.wc, self.h - 5, abc[x])

        try:
            light_yellow = QColor("#ffff66")
            dark_yellow = QColor("#cccc00")

            for p in cases:
                if (p[0] + p[1]) % 2 == 0:
                    painter.setBrush(light_yellow)
                    painter.setPen(light_yellow)
                else:
                    painter.setBrush(dark_yellow)
                    painter.setPen(dark_yellow)
                painter.drawRect(p[1] * self.wc, p[0] * self.hc, self.wc, self.hc)

        except Exception as e:
            print(e)

        if echec[0]:
            orange, red = QColor("#ffa500"), QColor("#ff0000")
            color = orange
            if P.mat():
                color = red
            x, y = echec[1]
            painter.setBrush(color)
            painter.setPen(color)
            painter.drawRect(x * self.wc, y * self.hc, self.wc, self.hc)
            echec = [False, ""]

        for x in range(8):
            for y in range(8):
                piece_path = folder_path + plateau.etat[8 * x + y].nom() + '.png'

                pixmap = QPixmap(piece_path)
                pixmap = pixmap.scaled(self.hc, self.wc, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                painter.drawPixmap(y * self.wc, x * self.hc, pixmap)

        gris = QColor('#4b4847')
        painter.setBrush(gris)
        painter.setPen(gris)
        painter.drawRect(1000, 0, 400, 1000)

        try:
            white = QColor('#FFFFFF')
            painter.setPen(white)
            painter.setFont(QFont("Arial", 12))
            for i, coup in enumerate(coups):
                if i >= 68:
                    painter.drawText(1265, 28 + 28*(i-68), f"{i+1}: {coup}")
                elif i >= 34:
                    painter.drawText(1135, 28 + 28*(i-34), f"{i+1}: {coup}")
                else:
                    painter.drawText(1005, 28 + 28*i, f"{i+1}: {coup}")

        except Exception as e:
            print(e)

    def case(self, p):
        """ p est un un clic
        Retourne la case du damier 8x8 contenant p """

        x, y = p.y(), p.x()
        return int(x/self.wc), int(y/self.hc)

    def mousePressEvent(self, e):
        """ Déclenchée par un évènement e (un clic)
        Apelle paintEvent sur self.update() """

        global P, L, cases

        x, y = self.case(e.pos())
        L.append([x, y])

        if len(cases) <= 1:
            cases = [[x, y]]
        else:
            cases = cases[:2] + [[x, y]]
        self.update()

        if len(L) == 1:
            piece = P.etat[8 * x + y]
            if piece.couleur != P.qj and piece.nom() != 'Vide':
                L = []
            else:
                CVA = P.cases_vraiment_accessibles(piece)
                if len(CVA) == 0:
                    L = []

        elif len(L) == 2:
            x1, y1 = L[0]
            x2, y2 = L[1]
            piece = P.etat[8 * x1 + y1]
            if not piece.couleur == P.etat[8 * x2 + y2].couleur:
                case = P.coords[8 * x2 + y2]
                print(P.cases_vraiment_accessibles(piece))
                if case in P.cases_vraiment_accessibles(piece):
                    global coups, etats, echec, i
                    coups.append(P.coup(piece, case))
                    P.deplacer(piece, case)
                    etats.append(deepcopy(P.etat))
                    i += 1
                    cases = L.copy()
                    if P.echec(P.qj)[0]:
                        echec[0] = True
                        roi = P.roi(P.qj)
                        coord_roi = P.coords[roi.coord]
                        echec[1] = coord_roi % 8, coord_roi // 8
                    self.update()
                L = []
            else: # cas où on clique 2 fois de suite sur une piece de la même couleur
                L = L[1:]

    def keyPressEvent(self, e):
        """ Déclenchée par un évènement e (une touche du clavier)
        Apelle paintEvent sur self.update() """
        global cases, i
        if e.key() == Qt.Key_Left and i >= 1:
            i -= 1
            P.etat = etats[i]
            cases = [cases[0]]
        if e.key() == Qt.Key_Right and 0 <= i < len(etats) - 1:
            i += 1
            P.etat = etats[i]
            cases = [cases[0]]
        self.update()

    def paintEvent(self, e):
        """ Déclenchée par self.update() (évènement e)
        Appelle la méthode draw_layout afin d'actualiser la fenêtre pour prendre
        en compte les changements du plateau opérés dans mousePressEvent """
        global P
        painter = QPainter(self.label.pixmap())
        self.draw_layout(painter, P)
        painter.end()


P = Plateau()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
