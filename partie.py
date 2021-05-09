__authors__ = "Rim Elouragini"
__date__ = "05/01/2020"

"""Ce fichier permet de définir la classe Partie permettant de jouer au jeu Tic-Tac-Toe """

from plateau import Plateau
from joueur import Joueur
from random import randrange
class Partie:
    """
    Classe modélisant une partie du jeu Tic-Tac-Toe utilisant
    un plateau et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        plateau (Plateau): Le plateau du jeu contenant les 9 cases.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None)
        nb_parties_nulles (int): Le nombre de parties nulles (aucun joueur n'a gagné).
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Tic-Tac-Toe.
        """
        self.plateau = Plateau()  # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []  # La liste des deux joueurs (initialement une liste vide).
        # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
        # Pendant le jeu et à chaque tour d'un joueur,
        # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        """
        Permet de démarrer la partie en commençant par l'affichage de ce texte:

        Bienvenue au jeu Tic Tac Toe.
        ---------------Menu---------------
        1- Jouer avec l'ordinateur.
        2- Jouter avec une autre personne.
        0- Quitter.
        -----------------------------------
        Entrez s.v.p. un nombre entre 0 et 2:?



        Cette méthode doit donc utiliser la méthode saisir_nombre().

        Elle doit par la suite demander à l'utilisateur les noms des joueurs.

        Veuillez utiliser 'Colosse' comme nom pour l'ordinateur.

        Il faut créer des instances de la classe Joueur et les ajouter à la liste joueurs.

        Il faut utiliser entre autres ces méthodes:

            *- demander_forme_pion(): pour demander au premier joueur la forme de son pion (X ou O).
              (Pas besoin de demander à l'autre joueur ou à l'ordinateur cela, car on peut le déduire).

            *- plateau.non_plein(): afin d'arrêter le jeu si le plateau est plein (partie nulle).

            *- tour(): afin d'exécuter le tour du joueur courant.

            *- plateau.est_gagnant(): afin de savoir si un joueur a gagné et donc arrêter le jeu.

        Il faut alterner entre le premier joueur et le deuxième joueur à chaque appel de tour()
        en utilisant l'attribut joueur_courant. DANS LA LISTE DES JOUEURS

        Après la fin de chaque partie, il faut afficher les statistiques sur le jeu.
        Voici un exemple:

        Partie terminée! Le joueur gagnant est: Colosse
        Parties gagnées par Mondher : 2
        Parties gagnées par Colosse : 1
        Parties nulles: 1
        Voulez-vous recommencer (O,N)?

        Il ne faut pas oublier d'initialiser le plateau avant de recommencer le jeu.
        Si l'utilisateur ne veut plus recommencer, il faut afficher ce message:
        ***Merci et au revoir !***
        """

        # pass*********************************************************************************************************
        print(
            "Bienvenue au jeu Tic Tac Toe.\n ---------------Menu--------------- \n 1- Jouer avec l'ordinateur.\n 2- Jouer avec une autre personne.\n 0- Quitter.")
        print("-----------------------------------\n Entrez s.v.p. un nombre entre 0 et 2: ")
        f = False
        q = True
        n = self.saisir_nombre(0, 2)
        if n == 1:
            jr = input("Entrez votre nom S.V.P: ")
            p = self.demander_forme_pion()
            j1 = Joueur(jr, "Personne", p)
            if p == "X":
                po = "O"
            else:
                po = "X"
            ord = Joueur("Colosse", "Ordinateur", po)
            self.joueurs.append(j1)
            self.joueurs.append(ord)
            self.joueur_courant =self.joueurs[randrange(1)]


        elif n == 2:
            nj1 = input("Le joueur Numero 1 Entrez votre nom S.V.P: ")
            h = self.demander_forme_pion()
            nj2 = input("Le joueur Numero 2 Entrez votre nom S.V.P: ")
            j1 = Joueur(nj1, "Personne", h)
            if h == "X":
                po = "O"
            else:
                po = "X"
            j2 = Joueur(nj2, "Personne", po)
            self.joueurs.append(j1)
            self.joueurs.append(j2)
            self.joueur_courant =self.joueurs[randrange(1)]
        else:
            print("-----------------------------------------------------")
            print("*** Merci et au revoir ***")
            exit()
        while q:
            self.plateau.initialiser()
            f = False
            print(self.plateau)
            print('\n')
            while self.plateau.non_plein() and not f:

                self.tour(n)

                if self.plateau.est_gagnant(self.joueur_courant.pion):
                    f = True
                    self.joueur_courant.nb_parties_gagnees += 1
                if not f:
                    if self.joueur_courant == self.joueurs[0]:
                        self.joueur_courant = self.joueurs[1]
                    else:
                        self.joueur_courant = self.joueurs[0]

            if not self.plateau.non_plein():
                print("-----------------------------------------------------")
                print("Partie terminée! Aucun joueur n'a gangné ")
                if not f:
                    self.nb_parties_nulles += 1

            if f:
                print("-----------------------------------------------------")
                print("Partie terminée! Le joueur gagnant est: ", self.joueur_courant.nom)
                if self.joueur_courant == self.joueurs[0]:
                    self.joueur_courant = self.joueurs[1]
                else:
                    self.joueur_courant = self.joueurs[0]
            print("Parties gagnées par", self.joueurs[0].nom, ": ", self.joueurs[0].nb_parties_gagnees)
            print("Parties gagnées par", self.joueurs[1].nom, ": ", self.joueurs[1].nb_parties_gagnees)
            print("Parties nulles:", self.nb_parties_nulles, "\n")
            print("Voulez-vous recommencer (O,N)?")
            r = input()
            if r == "O" or r == "o":
                q = True
            else:
                q = False
                print("-----------------------------------------------------")
                print("*** Merci et au revoir ! ***")


    def saisir_nombre(self, nb_min, nb_max):
        """
        Permet de demander à l'utilisateur un nombre et doit le valider.
        Ce nombre doit être une valeur entre nb_min et nb_max.
        Vous devez utiliser la méthode isnumeric() afin de vous assurer que l'utilisateur entre
        une valeur numérique et non pas une chaîne de caractères.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Args:
            nb_min (int): Un entier représentant le minimum du nombre à entrer.
            nb_max (int): Un entier représentant le maximum du nombre à entrer.

        Returns:
            int: Le nombre saisi par l'utilisateur après validation.
        """
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."

        # pass************************************************************************************************
        n = input()
        while not n.isnumeric() or not (int(n) >= nb_min and int(n) <= nb_max):
            if not n.isnumeric():
                print("La valeur à entrer doit étre numreique! ")
                print(" Entrez s.v.p. un nombre entre {} et {}:".format(nb_min, nb_max))
                n = input()
            else:
                print("le nombre à entrer doit étre  entre {} et {} !".format(nb_min, nb_max))
                print(" Entrez s.v.p. un nombre entre {} et {}:".format(nb_min, nb_max))
                n = input()

        return int(n)

    def demander_forme_pion(self):
        """
        Permet de demander à l'utilisateur un caractère et doit le valider.
        Ce caractère doit être soit 'O' soit 'X'.
        Veuillez consulter l'exemple d'exécution du jeu mentionné dans l'énoncé du TP
        afin de savoir quoi afficher à l'utilisateur.

        Returns:
            string: Le catactère saisi par l'utilisateur après validation.
        """

        # pass*****************************************************************************************************

        p = input("Selectionnez S.V.P la forme de votre pion(X,O): ")
        while not (p in ["O", "X"]):
            print(" le Pion  doit être soit 'O' soit 'X'! ")
            p = input("Selectionnez S.V.P la forme de votre pion(X,O): ")
        return p

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().


        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        # pass***************************************************************************************************

        if choix == 1:
            if self.joueur_courant.type == "Ordinateur":
                print("C'est maintenant le tour de ", self.joueur_courant.nom, '!')

                if self.joueur_courant.pion == "X":
                    p = "O"
                else:
                    p = "X"
                l, c = self.plateau.choisir_prochaine_case(p)
                self.plateau.selectionner_case(l, c, self.joueur_courant.pion)
            else:
                l, c = self.demander_postion()

                self.plateau.selectionner_case(l, c, self.joueur_courant.pion)
        else:
            l, c = self.demander_postion()
            self.plateau.selectionner_case(l, c, self.joueur_courant.pion)
        print(self.plateau)



    def demander_postion(self):
        """
        Permet de demander à l'utilisateur les coordonnées de la case qu'il veut jouer.
        Cette méthode doit valider ces coordonnées (ligne,colonne).
        Voici un exemple de ce qu'il faut afficher afin de demander cette position:

        Mondher : Entrez s.v.p. les coordonnées de la case à utiliser:
        Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:? 0
        Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:? 0

        Il faut utiliser la méthode saisir_nombre() et position_valide().

        Returns:
            (int,int):  Une paire d'entiers représentant les
                        coordonnées (ligne, colonne) de la case choisie.
        """
        # pass********************************************************************************************************

        print(self.joueur_courant.nom, ": Entrez s.v.p. les coordonnées de la case à utiliser:")
        print("Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:")
        l = self.saisir_nombre(0, 2)
        print("Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:")
        c = self.saisir_nombre(0, 2)
        while not self.plateau.position_valide(l, c):
            print("Position invalide, choissisez une autre case! ")
            print("Numéro de la ligne:Entrez s.v.p. un nombre entre 0 et 2:")
            l = self.saisir_nombre(0, 2)
            print("Numéro de la colonne:Entrez s.v.p. un nombre entre 0 et 2:")
            c = self.saisir_nombre(0, 2)
        return l, c


if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()
