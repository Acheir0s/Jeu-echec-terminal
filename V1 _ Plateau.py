class Plateau:
    def __init__(self):
        self.plateau = [[None] * 9 for _ in range(8)]
        self.initialiser_plateau()

#création du plateau de jeu
    def initialiser_plateau(self):
        self.plateau[0][0]='A / '
        self.plateau[1][0]='B / '
        self.plateau[2][0]='C / '
        self.plateau[3][0]='D / '
        self.plateau[4][0]='E / '
        self.plateau[5][0]='F / '
        self.plateau[6][0]='G / '
        self.plateau[7][0]='H / '
        
        
# on affiche le plateau de jeu
    def afficher(self):
        for ligne in reversed(self.plateau):
            print(' '.join([str(piece) if piece else '.' for piece in ligne]))
        # on affiche les nom de cologne
        print ('     _______________')
        print ('     1 2 3 4 5 6 7 8')

plateau=Plateau()
plateau.afficher()
