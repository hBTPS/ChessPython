import unittest
from Plateau import *
from Pieces import *

class TestPlateau(unittest.TestCase):
    """ Teste les méthodes de Plateau """

    def test_deplacer(self):
        P = Plateau()
        tour = P.etat[0]
        P.deplacer(tour, 'a6')
        self.assertEqual(P.etat[0].val, 0)
        self.assertEqual(P.etat[P.coords['a6']].val, 5)

    def test_cases_accessibles(self):
        P = Plateau()
        fou = P.etat[2]
        self.assertEqual(len(P.cases_accessibles(fou)), 0)

        P.deplacer(fou, 'a3')
        self.assertEqual(len(P.cases_accessibles(fou)), 4)

    def test_cases_vraiment_accessibles(self):
        P = Plateau()
        P.deplacer(P.etat[4], 'a6')
        P.deplacer(P.etat[0], 'a5')
        P.deplacer(P.etat[59], 'a4')
        # On aligne un roi blanc, une tour blanche et une reine noire sur la même colonne

        tour = P.etat[24]
        CA = P.cases_accessibles(tour)
        # A priori, la tour a accès à une ligne et une colonne (hors cases occupées par le même camp)
        CVA = P.cases_vraiment_accessibles(tour)
        # Or déplacer la tour met la reine en échec, donc la seule case accessible à la tour est a4
        self.assertNotEqual(CA, CVA)
        self.assertEqual(CVA, ['a4'])

    def test_echec(self):
        # Met un roi et une reine sur la même colonne sans pièces entre les deux:
        # la reine met directement le roi en échec
        P = Plateau()
        P.deplacer(P.etat[4], 'a6')
        P.deplacer(P.etat[59], 'a4')
        roi = P.etat[16]
        self.assertTrue(P.echec(roi))

    def test_roque(self):
        P = Plateau()
        P.etat[5] = P.etat[6] = Vide()
        P.etat[1] = P.etat[2] = P.etat[3] = Vide()
        self.assertTrue(P.peut_roquer('b')[0] and P.peut_roquer('b')[1])

        P.deplacer(P.etat[4], 'f8')
        self.assertFalse(P.peut_roquer('b')[0])

        P.deplacer(P.etat[P.coords['f8']], 'e8')
        self.assertFalse(P.peut_roquer('b')[0] or P.peut_roquer('b')[1])


class TestPieces(unittest.TestCase):
    """ Teste les méthodes de Pieces """

    def test_var(self):
        pion, roi, vide = Pion(), Roi(), Vide()
        self.assertEqual(pion.val, 1)
        self.assertEqual(roi.val, None)
        self.assertEqual(vide.val, 0)

        self.assertEqual(pion.coord, roi.coord, vide.coord)
        self.assertEqual(pion.coord, 'a1')
        self.assertEqual(pion.couleur, roi.couleur, vide.couleur)
        self.assertEqual(pion.couleur, '-')

    def test_type(self):
        p = Pion()
        self.assertIsInstance(p, ABC)


if __name__ == '__main__':
    unittest.main()
