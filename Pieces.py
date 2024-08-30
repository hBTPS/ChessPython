from abc import ABC, abstractmethod
import numpy as np

# Axel et Hadrien

class Piece(ABC):

    def __init__(self, val=0, coord='a1', couleur='-'):
        self.val = val
        self.coord = coord
        self.couleur = couleur

    @abstractmethod
    def deplacements(self):
        """ A instancier dans les classes filles """
        ...

    def deplacer(self, coord):
        """ Place la pièce aux coordonnées i,j = coord """
        self.coord = coord


class Pion(Piece):

    def __init__(self):
        super().__init__(val=1)

    def nom(self):
        return self.couleur + 'p'

    def deplacements(self):
        return np.array([9, 10, 11, 20, -9, -10, -11, -20])


class Tour(Piece):

    def __init__(self):
        super().__init__(val=5)

    def nom(self):
        return self.couleur + 'r'

    def deplacements(self):
        return np.array([-10, 10, -1, 1])


class Cavalier(Piece):

    def __init__(self):
        super().__init__(val=3)

    def nom(self):
        return self.couleur + 'n'

    def deplacements(self):
        return np.array([-12, -21, -19, -8, 12, 21, 19, 8])


class Fou(Piece):

    def __init__(self):
        super().__init__(val=3)

    def nom(self):
        return self.couleur + 'b'

    def deplacements(self):
        return np.array([-11, -9, 11, 9])


class Reine(Piece):

    def __init__(self):
        super().__init__(val=9)

    def nom(self):
        return self.couleur + 'q'

    def deplacements(self):
        return np.array([-11, -9, 11, 9, -10, 10, -1, 1])


class Roi(Piece):

    def __init__(self):
        super().__init__(val=None)

    def nom(self):
        return self.couleur + 'k'

    def deplacements(self):
        return np.array([-11, -9, 11, 9, -10, 10, -1, 1])


class Vide(Piece):

    def __init__(self):
        super().__init__(val=0)

    def nom(self):
        return 'Vide'

    def deplacements(self):
        return []