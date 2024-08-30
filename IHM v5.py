import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Plateau import *
L = []
folder_path = 'C:\\Users\\Hadrien\\Documents\\ENSTA\\UE 4.2 Traitement et communication des donnees\\Conception logicielle\\Chess\\Chess pieces\\'

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Window
        self.setWindowTitle("Chess")
        self.setGeometry(500, 100, 1000, 1000)
        self.setFixedSize(self.size())

        self.w, self.h = self.width(), self.height()
        self.wc, self.hc = int(self.w/8), int(self.h/8)

        # Canvas
        self.label = QLabel()
        canvas = QPixmap(self.size())
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

    def draw_layout(self, painter, plateau):
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

        global folder_path
        for x in range(8):
            for y in range(8):
                piece_path = folder_path + plateau.etat[8 * x + y].nom() + '.png'

                pixmap = QPixmap(piece_path)
                pixmap = pixmap.scaled(self.hc, self.wc, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                painter.drawPixmap(y * self.wc, x * self.hc, pixmap)

    def case(self, p):
        x, y = p.y(), p.x()
        return int(x/self.wc), int(y/self.hc)

    def mousePressEvent(self, e):
        global P, L
        x, y = self.case(e.pos())
        L.append([x, y])

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
                if case in P.cases_vraiment_accessibles(piece):
                    if not(piece.nom()[1] == 'k' and P.echec(P.qj)[0] and abs(y2 - y1) == 2):
                        P.deplacer(piece, case)
                        self.update()
                L = []
            else: # cas où on clique 2 fois de suite sur une piece de la même couleur
                L = L[1:]

    def paintEvent(self, e):
        global P, L
        painter = QPainter(self.label.pixmap())
        self.draw_layout(painter, P)
        painter.end()


P = Plateau()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()