class Piece:
    def __init__(self, couleur, type_piece):
        self.couleur = couleur

    def __str__(self):
        if self.couleur == 'blanc': 
            return self.type_piece[0].upper() 
        else :
            return self.type_piece[0].lower() 
        
    def getcouleur(self):
        return self.couleur

class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "king",)

class Reine(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "queen")
    
class Fou(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "bishop")

class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "cavalier")

class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "tower")

class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "pion")

class Plateau:
    def __init__(self):
        self.plateau = [[None] * 9 for _ in range(8)]
        self.initialiser_plateau()


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


if __name__ == "__main__":
    plateau = Plateau()
    plateau.afficher()
