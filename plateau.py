__authors__ = "Rim Elouragini"
__date__ = "05/01/2020"

"""
ce fichier permet de définir la classe Plateau permettant de jouer au jeu Tic-Tac-Toe
"""

from random import randrange
from case import Case
from joueur import Joueur

class Plateau:
    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de casess. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
    """



    def __init__(self):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Méthode fournie permettant d'initialiser le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def __str__(self):
        """Méthode spéciale fournie indiquant à Python comment représenter une instance de Plateau
        sous la forme d'une chaîne de caractères. Permet donc d'afficher le plateau du jeu
        à l'écran en faisant par exemple:
        p1 = Plateau()
        print(p1)
        Donc, lorsque vous affichez un objet, Python invoque automatiquement la méthode __str__
        Voici un exemple d'affichage:
         +-0-+-1-+-2-+
        0|   | X | X |
         +---+---+---+
        1| O | O | X |
         +---+---+---+
        2|   |   | O |
         +---+---+---+

        Returns:
            string: Retourne la chaîne de caractères à afficher.
        """
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s

    def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        #pass*******************************************************************************************************
        f=False
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cases[(i, j)].est_vide():
                    f=True
                    break
        return f


    def position_valide(self, ligne, colonne):
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."

        #pass**********************************************************************************************************
        return self.cases[(ligne,colonne)].est_vide()

    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        # pass**********************************************************************************************************
        self.cases[(ligne, colonne)].contenu=pion


    def est_gagnant(self, pion):

        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """


        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

       # pass*****************************************************************************************************

        h = False
        k = False
        n = False
        for i in range(0, 3):
            j = 0
            f = False
            while j < 3:
                if self.cases[(i, j)].est_pion(pion):
                    f = True
                    j = j + 1
                else:
                    f = False
                    break
            if f:
                break

        if not f:
            for i in range(0, 3):
                j = 0
                h = False
                while j < 3:
                    if self.cases[(j, i)].est_pion(pion):
                        h = True
                        j = j + 1
                    else:
                        h = False
                        break
                if h:
                    break

        if not h:
            for i in range(0, 3):
                for j in range(0, 3):
                    if (i == j):
                        if self.cases[(i, j)].est_pion(pion):
                            k = True
                        else:
                            k = False
                            break
                if not k:
                    break

        if not k:
            j = 2
            i = 0
            while j > -1:
                if self.cases[(i, j)].est_pion(pion):
                    n = True
                    j = j - 1
                    i = i + 1
                else:
                    n = False
                    break

        if f or k or h or n:
            return True
        else:
            return False
       #***************************************************************************************************************

    def choisir_prochaine_case(self, pion):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.
        L'algorithme que vous allez concevoir permettant de faire jouer l'ordinateur
        n'a pas besoin d'être optimal. Cela permettra à l'adversaire de gagner de temps en temps.
        Il faut par contre essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'adversaire pour que ce dernier ne gagne pas facilement.
        Il faut aussi essayer de mettre le pion de l'ordinateur dans une ligne, une colonne
        ou une diagonale contenant deux pions de l'ordinateur pour que ce dernier puisse gagner.
        Vous pouvez utiliser ici la fonction randrange() du module random.
        Par exemple: randrange(1,10) vous retourne une valeur entre 1 et 9 au hasard.

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        # pass**********************************************************************************************************
        if pion == "X":
            po = "O"
        else:
            po = "X"
        l, c = self.verif_bonne_pos(po)
        if (l,c) == (-1,-1):
            l, c = self.verif_bonne_pos(pion)
            if (l, c) == (-1, -1):
                l = randrange(3)
                c = randrange(3)
                while not self.position_valide(l, c):
                    l = randrange(3)
                    c = randrange(3)
        return (l, c)



    def verif_bonne_pos(self, pion):
        
        f = False
        h = False
        k = False
        g = False
        l, c = -1, -1

        for i in range(0, 3):
            if self.cases[(i, 0)].est_pion(pion) and self.cases[(i, 1)].est_pion(pion) and self.cases[(i, 2)].est_vide():
                l = i
                c = 2
                f = True
                break
            elif self.cases[(i, 1)].est_pion(pion) and self.cases[(i, 2)].est_pion(pion) and self.cases[(i, 0)].est_vide():
                l = i
                c = 0
                f = True
                break
            elif self.cases[(i, 0)].est_pion(pion) and self.cases[(i, 2)].est_pion(pion) and self.cases[(i, 1)].est_vide():
                l = i
                c = 1
                f = True
                break

        if not f:
            for i in range(0, 3):
                if self.cases[(0, i)].est_pion(pion) and self.cases[(1, i)].est_pion(pion) and self.cases[(2, i)].est_vide():
                    l = 2
                    c = i
                    h = True
                    break
                elif self.cases[(1, i)].contenu == self.cases[(2, i)].contenu == pion and self.cases[(0, i)].est_vide():
                    l = 0
                    c = i
                    h = True
                    break
                elif self.cases[(0, i)].est_pion(pion) and self.cases[(2, i)].est_pion(pion) and self.cases[(1, i)].est_vide():
                    l = 1
                    c = i
                    h = True
                    break

        if not h and not f:
            if self.cases[(0, 0)].est_pion(pion) and self.cases[(1, 1)].est_pion(pion) and self.cases[(2, 2)].est_vide():
                l = 2
                c = 2
                k = True

            elif self.cases[(1, 1)].est_pion(pion) and self.cases[(2, 2)].est_pion(pion)  and self.cases[(0, 0)].est_vide():
                l = 0
                c = 0
                k = True

            elif self.cases[(0, 0)].est_pion(pion) and self.cases[(2, 2)].est_pion(pion)  and self.cases[(1, 1)].est_vide():
                l = 1
                c = 1
                k = True


        if not h and not f and not k:
            if self.cases[(0, 2)].est_pion(pion) and self.cases[(1, 1)].est_pion(pion)  and self.cases[(2, 0)].est_vide():
                l = 2
                c = 0
                g = True
            elif self.cases[(1, 1)].est_pion(pion) and self.cases[(2, 0)].est_pion(pion) and pion and self.cases[(0, 2)].est_vide():
                l = 0
                c = 2
                g = True

            elif self.cases[(0, 2)].est_pion(pion) and self.cases[(2, 0)].est_pion(pion) and self.cases[(1, 1)].est_vide():
                l = 1
                c = 1
                g = True

        if not h and not f and not k and not g:
            (l,c)=(-1,-1)
        return (l, c)

            


