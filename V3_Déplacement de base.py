flag=True
turn=0
class Piece:
    def __init__(self, couleur, type_piece, valeur):
        self.couleur = couleur
        self.type_piece = type_piece
        self.valeur=valeur
        self.case_autorise=[]

    def __str__(self):
        if self.couleur == 'blanc':
            return self.type_piece[0].upper()
        else :
            return self.type_piece[0].lower()

    def getcouleur(self):
        return self.couleur
    def getValeur(self):
        return self.valeur
    def getType_piece (self):
        return self.type_piece


class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "king",0)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # Le roi se déplace d'une case dans toutes les directions
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])
        return dx <= 1 and dy <= 1


class Reine(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "queen",9)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # La reine peut se déplacer en ligne droite ou en diagonale
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])
        return dx == dy or depart[0] == arrivee[0] or depart[1] == arrivee[1]


class Fou(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "bishop",3)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # Le fou se déplace en diagonale
        return abs(depart[0] - arrivee[0]) == abs(depart[1] - arrivee[1])


class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "cavalier",3)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # Le cavalier se déplace en "L" (2 cases dans une direction et 1 dans l'autre)
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "tower",5)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # La tour se déplace en ligne droite (horizontale ou verticale) + vérification si pas de pièce entre l'arrivé et la fin
        return depart[0] == arrivee[0] or depart[1] == arrivee[1]



class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "pion",1)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
    # Le pion se déplace d'une case vers l'avant et prend en diagonal avant
        #avance si blanc, recule si noir
        if self.couleur == 'blanc':
            direction = 1
        else :
            direction = -1

        # Premier déplacement de deux case posible si premier déplacement
        if self.couleur=='blanc'and depart[0]==1:
            if piece_arrivee != None:
                dx = abs(depart[1]-arrivee[1])
            else:
                dx = depart[1] - arrivee[1]
            return dx == 0 or dx == 1
        elif self.couleur=='noir' and depart[0]==6:
            if piece_arrivee != None:
                dx = abs(depart[1]-arrivee[1])
            else:
                dx = depart[1] - arrivee[1]
            return dx == 0 or dx == 1

        #prise en diagonale
        if piece_arrivee != None:
            dx = abs(depart[1]-arrivee[1])
        else:
            dx = False

        dy = arrivee[0]- depart[0]
        return (dx == 0 and dy == direction) or (dx == 1 and dy==direction)

class Plateau:
    def __init__(self):
        self.plateau = [[None] * 9 for _ in range(8)]
        self.initialiser_plateau()
        self.turn=1
        self.point_blanc=0
        self.point_noir=0
    def getturn(self):
        return self.turn
    def getPoint_blanc(self):
        return self.point_blanc
    def getPoint_noir(self):
        return self.point_noir
    def getplateau(self):
        return self.plateau

#création du plateau de jeu
    def initialiser_plateau(self):
        # on place les piece blanche
        self.plateau[0] = ['1 / ',Tour('blanc'), Cavalier('blanc'), Fou('blanc'), Reine('blanc'), Roi('blanc'), Fou('blanc'), Cavalier('blanc'), Tour('blanc')]
        self.plateau[1] = [Pion('blanc')] * 9
        # on place les piece noir
        self.plateau[6] = [Pion('noir')] * 9
        self.plateau[7] = ['8 / ',Tour('noir'), Cavalier('noir'), Fou('noir'), Reine('noir'), Roi('noir'), Fou('noir'), Cavalier('noir'), Tour('noir')]
        # on affiche les autre nom de ligne
        self.plateau[1][0]='2 / '
        self.plateau[2][0]='3 / '
        self.plateau[3][0]='4 / '
        self.plateau[4][0]='5 / '
        self.plateau[5][0]='6 / '
        self.plateau[6][0]='7 / '


# on affiche le plateau de jeu
    def afficher(self):
        if self.turn % 2 == 1:
            for ligne in reversed(self.plateau):
                print(' '.join([str(piece) if piece else '.' for piece in ligne]))
            # on affiche les nom de cologne
            print ('     _______________')
            print ('     A B C D E F G H')
        else:
            for ligne in self.plateau:
                print(' '.join([str(piece) if piece else '.' for piece in ligne]))
            # on affiche les nom de cologne
            print ('     _______________')
            print ('     A B C D E F G H')


# déplacement de la pièce
    def deplacer_piece(self, depart, arrivee):
        piece = self.plateau[depart[0]][depart[1]]
        piece_arrivee= self.plateau[arrivee[0]][arrivee[1]]
        plateau = self.plateau
        #on vérifie si on choisit bien une pièce à déplacer
        if piece!=None:
            #on ne peux jouer que ses propres pièces et pas celles de l'adversaire
            if (piece.getcouleur() == 'blanc' and self.getturn()%2==1) or (piece.getcouleur() == 'noir' and self.getturn()%2==0):
                # on regarde si on prend une pièce adverse ou pas
                if piece_arrivee==None:
                    #on regarde si le mouvement est valide
                    if piece and piece.mouvement_valide(depart, arrivee, piece_arrivee, plateau):
                        self.plateau[arrivee[0]][arrivee[1]] = piece
                        self.plateau[depart[0]][depart[1]] = None
                        self.turn = self.turn+1
                    else:
                        print("Mouvement invalide")
                else:
                    # on ne peux pas manger une pièce de sa couleur
                    if piece.getcouleur()==piece_arrivee.getcouleur():
                        print('Vous ne pouvez pas prendre une pièce de votre couleur.')
                    else:
                        # on regarde si le mouvement est valide si je mange
                        if piece and piece.mouvement_valide(depart, arrivee, piece_arrivee, plateau):
                            #compteur de point
                            if piece_arrivee.getcouleur()=='blanc':
                                self.point_noir += piece_arrivee.getValeur()
                            else:
                                self.point_blanc += piece_arrivee.getValeur()
                            #déplacement
                            self.plateau[arrivee[0]][arrivee[1]] = piece
                            self.plateau[depart[0]][depart[1]] = None
                            self.turn = self.turn+1
                        else:
                            print("Mouvement invalide")
            else:
                print('Cette pièce ne vous appartient pas')
        else:
            print("Vous n'avez pas sélectionné de pièce")




    #demande de la case
    def demander_mouvement(self):
        while True:
            try:
                # Demande la case de départ
                depart = input("Entrez la case de départ (ex: a2) : ")
                if depart == 'q':
                    flag=None
                    break
                else:
                    x1, y1 = self.convertir_case_vers_coord(depart)

                # Demande la case d'arrivée
                arrivee = input("Entrez la case d'arrivée (ex: a3) : ")
                if arrivee == 'q':
                    flag=None
                    break
                else:
                    x2, y2 = self.convertir_case_vers_coord(arrivee)

                # Déplace la pièce
                self.deplacer_piece((x1, y1), (x2, y2))
                break
            except ValueError:
                print("Entrée invalide. Essayez encore.")

    #Convertit une notation de case comme 'a2' en coordonnées de plateau.
    def convertir_case_vers_coord(self, case):
        lettre, chiffre = case
        y = int(chiffre)-1
        x = ord(lettre) - ord('a')+1  # Convertie la lettre en index (a -> 0, b -> 1, etc.)
        return y,x


if __name__ == "__main__":
    plateau = Plateau()
    plateau.afficher()
    while flag==True:
        if flag != True:
            break
 
        print('tour :',plateau.getturn())
        print('point blanc :', plateau.getPoint_blanc())
        print('point noir :', plateau.getPoint_noir())
        plateau.demander_mouvement()
        plateau.afficher()
