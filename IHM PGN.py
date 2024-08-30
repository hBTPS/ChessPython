import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Plateau import *
from PGN_parser import *

path = 'PGN games\\OwnGame2.pgn'
d = pgn_to_dict(path)
COUPS = [d[tour][i] for tour in d for i in [0, 1]]
etats, n = [deepcopy(Plateau().etat)], 0


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Window
        self.setWindowTitle("Chess")
        self.setGeometry(200, 100, 1500, 1000)
        self.setFixedSize(self.size())

        self.w, self.h = 1000, self.height()
        self.wc, self.hc = int(self.w/8), int(self.h/8)

        # Canvas
        self.label = QLabel()
        canvas = QPixmap(self.size())
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        # Buttons
        L = ['<', '>']
        for a in L:
            button = QPushButton(a, self)
            button.setStyleSheet('font: bold 20px;')
            button.setFixedSize(130, 90)
            button.pressed.connect(lambda val=a: self.button_pressed(val))
            if a == '>':
                button.move(1300, 500)
            else:
                button.move(1100, 500)

    def button_pressed(self, a):
        global P, etats, n
        l = len(COUPS) + int(COUPS[-1][1] != '')
        if a == '>' and n <= l:
            P.faire_coup(P.qj, COUPS[n])
            n += 1
            etats.append(deepcopy(P.etat))
            self.update()
        elif a == '<' and 1 <= n:
            P.annuler_coup()
            n -= 1
            P.etat = etats[n]
            self.update()

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

        folder_path = 'C:\\Users\\Hadrien\\Documents\\ENSTA\\UE 4.2 Traitement et communication des donnees\\Conception logicielle\\Chess\\Chess pieces\\'
        for x in range(8):
            for y in range(8):
                piece_path = folder_path + plateau.etat[8 * x + y].nom() + '.png'

                pixmap = QPixmap(piece_path)
                pixmap = pixmap.scaled(self.hc, self.wc, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                painter.drawPixmap(y * self.wc, x * self.hc, pixmap)

    def paintEvent(self, e):
        global P
        painter = QPainter(self.label.pixmap())
        self.draw_layout(painter, P)
        painter.end()


P = Plateau()
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()