import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True

#initialisation de l'image de l'échiquier et des pièces
echequier = pygame.image.load("image/echequier.PNG")
pion_noir = pygame.image.load("piece/pion noir.png")
pion_blanc = pygame.image.load("piece/pion blanc.png")
tour_noir = pygame.image.load("piece/tour noir.png")
tour_blanc = pygame.image.load("piece/tour blanc.png")
cavalier_noir = pygame.image.load("piece/cavalier noir.png")
cavalier_blanc = pygame.image.load("piece/cavalier blanc.png")
fou_blanc = pygame.image.load("piece/fou blanc.png")
fou_noir = pygame.image.load("piece/fou noir.png")
reine_noir = pygame.image.load("piece/reine noir.png")
reine_blanc = pygame.image.load("piece/reine blanc.png")
roi_noir = pygame.image.load("piece/roi noir.png")
roi_blanc = pygame.image.load("piece/roi blanc.png")

#Assignations des cases à une zone rectangulaire du plateau
a8 = pygame.Rect(0, 0, 100, 100)
b8 = pygame.Rect(100, 0, 100, 100)
c8 = pygame.Rect(200, 0, 100, 100)
d8 = pygame.Rect(300, 0, 100, 100)
e8 = pygame.Rect(400, 0, 100, 100)
f8 = pygame.Rect(500, 0, 100, 100)
g8 = pygame.Rect(600, 0, 100, 100)
h8 = pygame.Rect(700, 0, 100, 100)

a7 = pygame.Rect(0, 100, 100, 100)
b7 = pygame.Rect(100, 100, 100, 100)
c7 = pygame.Rect(200, 100, 100, 100)
d7 = pygame.Rect(300, 100, 100, 100)
e7 = pygame.Rect(400, 100, 100, 100)
f7 = pygame.Rect(500, 100, 100, 100)
g7 = pygame.Rect(600, 100, 100, 100)
h7 = pygame.Rect(700, 100, 100, 100)

a6 = pygame.Rect(0, 200, 100, 100)
b6 = pygame.Rect(100, 200, 100, 100)
c6 = pygame.Rect(200, 200, 100, 100)
d6 = pygame.Rect(300, 200, 100, 100)
e6 = pygame.Rect(400, 200, 100, 100)
f6 = pygame.Rect(500, 200, 100, 100)
g6 = pygame.Rect(600, 200, 100, 100)
h6 = pygame.Rect(700, 200, 100, 100)

a5 = pygame.Rect(0, 300, 100, 100)
b5 = pygame.Rect(100, 300, 100, 100)
c5 = pygame.Rect(200, 300, 100, 100)
d5 = pygame.Rect(300, 300, 100, 100)
e5 = pygame.Rect(400, 300, 100, 100)
f5 = pygame.Rect(500, 300, 100, 100)
g5 = pygame.Rect(600, 300, 100, 100)
h5 = pygame.Rect(700, 300, 100, 100)

a4 = pygame.Rect(0, 400, 100, 100)
b4 = pygame.Rect(100, 400, 100, 100)
c4 = pygame.Rect(200, 400, 100, 100)
d4 = pygame.Rect(300, 400, 100, 100)
e4 = pygame.Rect(400, 400, 100, 100)
f4 = pygame.Rect(500, 400, 100, 100)
g4 = pygame.Rect(600, 400, 100, 100)
h4 = pygame.Rect(700, 400, 100, 100)

a3 = pygame.Rect(0,500, 100, 100)
b3 = pygame.Rect(100,500, 100, 100)
c3 = pygame.Rect(200, 500, 100, 100)
d3 = pygame.Rect(300, 500, 100, 100)
e3 = pygame.Rect(400, 500, 100, 100)
f3 = pygame.Rect(500, 500, 100, 100)
g3 = pygame.Rect(600, 500, 100, 100)
h3 = pygame.Rect(700, 500, 100, 100)

a2 = pygame.Rect(0, 600, 100, 100)
b2 = pygame.Rect(100, 600, 100, 100)
c2 = pygame.Rect(200, 600, 100, 100)
d2 = pygame.Rect(300, 600, 100, 100)
e2 = pygame.Rect(400, 600, 100, 100)
f2 = pygame.Rect(500, 600, 100, 100)
g2 = pygame.Rect(600, 600, 100, 100)
h2 = pygame.Rect(700, 600, 100, 100)

a1 = pygame.Rect(0, 700, 100, 100)
b1 = pygame.Rect(100, 700, 100, 100)
c1 = pygame.Rect(200, 700, 100, 100)
d1 = pygame.Rect(300, 700, 100, 100)
e1 = pygame.Rect(400, 700, 100, 100)
f1 = pygame.Rect(500, 700, 100, 100)
g1 = pygame.Rect(600, 700, 100, 100)
h1 = pygame.Rect(700, 700, 100, 100)

# Liste des rectangles pour faciliter la vérification des clics
rectangles = {
    'a8': a8, 'b8': b8, 'c8': c8, 'd8': d8, 'e8': e8, 'f8': f8, 'g8': g8, 'h8': h8,
    'a7': a7, 'b7': b7, 'c7': c7, 'd7': d7, 'e7': e7, 'f7': f7, 'g7': g7, 'h7': h7,
    'a6': a6, 'b6': b6, 'c6': c6, 'd6': d6, 'e6': e6, 'f6': f6, 'g6': g6, 'h6': h6,
    'a5': a5, 'b5': b5, 'c5': c5, 'd5': d5, 'e5': e5, 'f5': f5, 'g5': g5, 'h5': h5,
    'a4': a4, 'b4': b4, 'c4': c4, 'd4': d4, 'e4': e4, 'f4': f4, 'g4': g4, 'h4': h4,
    'a3': a3, 'b3': b3, 'c3': c3, 'd3': d3, 'e3': e3, 'f3': f3, 'g3': g3, 'h3': h3,
    'a2': a2, 'b2': b2, 'c2': c2, 'd2': d2, 'e2': e2, 'f2': f2, 'g2': g2, 'h2': h2,
    'a1': a1, 'b1': b1, 'c1': c1, 'd1': d1, 'e1': e1, 'f1': f1, 'g1': g1, 'h1': h1
}


class Piece:
    def __init__(self, couleur, type_piece, valeur):
        self.couleur = couleur
        self.type_piece = type_piece
        self.valeur = valeur
        self.case_autorise = []


    def __str__(self):
        # pièce blanche en MAJUSCULE
        if self.couleur == 'blanc':
            return self.type_piece[0].upper()
        # pièce noire en minuscule
        else:
            return self.type_piece[0].lower()

    # obtient Couleur
    def getcouleur(self):
        return self.couleur

    # obtient Valeur
    def getValeur(self):
        return self.valeur

    # obtient Le type de pièce
    def getType_piece(self):
        return self.type_piece

    def peut_attaquer(self, depart, arrivee, plateau):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

    def getImage(self):
        return self.image


class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "king", 0)
        self.a_bouge = False
        self.image = roi_blanc if self.getcouleur() == 'blanc' else roi_noir

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        if plateau[arrivee[0]][arrivee[1]] != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur() == self.getcouleur():
                return False

        # Le roi se déplace d'une case dans toutes les directions
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])
        return dx <= 1 and dy <= 1

    def peut_attaquer(self, depart, arrivee, plateau):
        return self.mouvement_valide(depart, arrivee, None, plateau)

    def peut_roquer(self, depart, arrivee, plateau):
        if self.a_bouge:
            return False

        if arrivee[1] == 6:  # Roque
            tour = plateau[depart[0]][7]
            if isinstance(tour, Tour) and not tour.a_bouge:
                for i in range(5, 7):
                    if plateau[depart[0]][i] is not None:
                        return False
                return True
        elif arrivee[1] == 2:  # Grand Roque
            tour = plateau[depart[0]][0]
            if isinstance(tour, Tour) and not tour.a_bouge:
                for i in range(1, 4):
                    if plateau[depart[0]][i] is not None:
                        return False
                return True
        return False


class Reine(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "queen", 9)
        self.image = reine_blanc if self.getcouleur() == 'blanc' else reine_noir

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # La reine peut se déplacer en ligne droite ou en diagonale
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])

        if plateau[arrivee[0]][arrivee[1]] != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur() == self.getcouleur():
                return False

        if dx == dy or depart[0] == arrivee[0] or depart[1] == arrivee[1]:
            # Vérifier s'il y a des pièces entre le départ et l'arrivée
            if dx == dy:  # Mouvement diagonal
                dir_x = 1 if arrivee[1] > depart[1] else -1
                dir_y = 1 if arrivee[0] > depart[0] else -1
                for i in range(1, dx):
                    if plateau[depart[0] + i * dir_y][depart[1] + i * dir_x] is not None:
                        return False
            elif depart[0] == arrivee[0]:  # Mouvement horizontal
                dir_x = 1 if arrivee[1] > depart[1] else -1
                for i in range(1, dx):
                    if plateau[depart[0]][depart[1] + i * dir_x] is not None:
                        return False
            elif depart[1] == arrivee[1]:  # Mouvement vertical
                dir_y = 1 if arrivee[0] > depart[0] else -1
                for i in range(1, dy):
                    if plateau[depart[0] + i * dir_y][depart[1]] is not None:
                        return False
            return True
        return False

    def peut_attaquer(self, depart, arrivee, plateau):
        return self.mouvement_valide(depart, arrivee, None, plateau)


class Fou(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "bishop", 3)
        self.image = fou_blanc if self.getcouleur() == 'blanc' else fou_noir

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):

        if plateau[arrivee[0]][arrivee[1]] != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur() == self.getcouleur():
                return False

        # Le fou se déplace en diagonale
        if abs(depart[0] - arrivee[0]) == abs(depart[1] - arrivee[1]):
            # Vérifier s'il y a des pièces entre le départ et l'arrivée
            dy = abs(depart[0] - arrivee[0])
            dir_x = 1 if arrivee[1] > depart[1] else -1
            dir_y = 1 if arrivee[0] > depart[0] else -1
            for i in range(1, dy):
                if plateau[depart[0] + i * dir_y][depart[1] + i * dir_x] is not None:
                    return False
            return True
        return False

    def peut_attaquer(self, depart, arrivee, plateau):
        return self.mouvement_valide(depart, arrivee, None, plateau)


class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "cavalier", 3)
        self.image = cavalier_blanc if self.getcouleur() == 'blanc' else cavalier_noir

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):

        if plateau[arrivee[0]][arrivee[1]] != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur() == self.getcouleur():
                return False

        # Le cavalier se déplace en "L" (2 cases dans une direction et 1 dans l'autre)
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    def peut_attaquer(self, depart, arrivee, plateau):
        return self.mouvement_valide(depart, arrivee, None, plateau)


class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "tower", 5)
        self.a_bouge = False
        self.image = tour_blanc if self.getcouleur() == 'blanc' else tour_noir

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        if plateau[arrivee[0]][arrivee[1]] != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur() == self.getcouleur():
                return False

        # La tour se déplace en ligne droite (horizontale ou verticale)
        if depart[0] == arrivee[0]:
            # Mouvement horizontal
            step = 1 if arrivee[1] > depart[1] else -1
            for col in range(depart[1] + step, arrivee[1], step):
                if plateau[depart[0]][col] is not None:
                    return False
        elif depart[1] == arrivee[1]:
            # Mouvement vertical
            step = 1 if arrivee[0] > depart[0] else -1
            for lig in range(depart[0] + step, arrivee[0], step):
                if plateau[lig][depart[1]] is not None:
                    return False
        else:
            return False
        return True

    def peut_attaquer(self, depart, arrivee, plateau):
        return self.mouvement_valide(depart, arrivee, None, plateau)


class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "pion", 1)
        self.deux_cases = False
        self.image = pion_blanc if self.getcouleur() == 'blanc' else pion_noir

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        if plateau[arrivee[0]][arrivee[1]] != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur() == self.getcouleur():
                return False

        # Déterminer la direction de déplacement
        if self.couleur == 'blanc':
            direction = 1
            rang_initial = 1
        else:
            direction = -1
            rang_initial = 6

        dy = arrivee[0] - depart[0]
        dx = abs(depart[1] - arrivee[1])

        # Déplacement d'une case vers l'avant
        if dy == direction and dx == 0 and piece_arrivee is None:
            return True

        # Déplacement de deux cases vers l'avant (premier mouvement)
        if depart[0] == rang_initial and dy == 2 * direction and dx == 0 and piece_arrivee is None:
            # Vérifier qu'il n'y a pas de pièce entre les deux cases
            if plateau[depart[0] + direction][depart[1]] is None:
                self.deux_cases = True
                return True

        # Prise en diagonale
        if dy == direction and dx == 1 and piece_arrivee is not None and piece_arrivee.getcouleur() != self.couleur:
            return True

        # Prise en passant
        if dy == direction and dx == 1 and piece_arrivee is None:
            if self.peut_prendre_en_passant(depart, arrivee, plateau):
                return True

        return False

    def peut_attaquer(self, depart, arrivee, plateau):
        if self.couleur == 'blanc':
            direction = 1
        else:
            direction = -1

        dy = arrivee[0] - depart[0]
        dx = abs(depart[1] - arrivee[1])

        return dy == direction and dx == 1

    def peut_prendre_en_passant(self, depart, arrivee, plateau):
        if (self.couleur == 'blanc' and depart[0] == 4) or self.couleur == 'noir' and depart[0] == 3:
            if plateau[depart[0]][arrivee[1]] is not None:
                piece_adverse = plateau[depart[0]][arrivee[1]]
                if piece_adverse.getType_piece() == 'pion' and piece_adverse.deux_cases:
                    return True
        return False

class Plateau:
    def __init__(self):
        self.plateau = [[None] * 9 for _ in range(8)]
        self.case = [[a1, a2, a3, a4, a5, a6, a7, a8],
                    [b1, b2, b3, b4, b5, b6, b7, b8],
                    [c1, c2, c3, c4, c5, c6, c7, c8],
                    [d1, d2, d3, d4, d5, d6, d7, d8],
                    [e1, e2, e3, e4, e5, e6, e7, e8],
                    [f1, f2, f3, f4, f5, f6, f7, f8],
                    [g1, g2, g3, g4, g5, g6, g7, g8],
                    [h1, h2, h3, h4, h5, h6, h7, h8]]
        self.initialiser_plateau()
        self.turn = 1
        self.point_blanc = 0
        self.point_noir = 0

    def getturn(self):
        return self.turn

    def getPoint_blanc(self):
        return self.point_blanc

    def getPoint_noir(self):
        return self.point_noir

    def getplateau(self):
        return self.plateau
    

    # création du plateau de jeu
    def initialiser_plateau(self):
        # on place les pieces blanches
        self.plateau[0] = [Tour('blanc'), Cavalier('blanc'), Fou('blanc'), Reine('blanc'), Roi('blanc'), Fou('blanc'), Cavalier('blanc'), Tour('blanc')]
        self.plateau[1] = [Pion('blanc')] * 8
        # on place les pieces noires
        self.plateau[6] = [Pion('noir')] * 8
        self.plateau[7] = [Tour('noir'), Cavalier('noir'), Fou('noir'), Reine('noir'), Roi('noir'), Fou('noir'), Cavalier('noir'), Tour('noir')]


    def afficher(self, screen):
        # Dessiner les pièces sur le plateau
        if self.turn % 2 == 1:
            screen.blit(pygame.image.load("image/echequier.PNG"), (0, 0))
            for i in range(8):
                for j in range(8):
                    piece = self.plateau[j][i]
                    if piece:
                        rect = self.case[i][j]
                        x = rect.topleft[0] 
                        y = rect.topleft[1] 
                        if piece.getType_piece() == 'pion':
                            x += 10
                        screen.blit(piece.getImage(), (x,y))
        else:
            screen.blit(pygame.image.load("image/echequier cote noir.PNG"), (0, 0))
            for i in range(8):
                for j in range(8):
                    piece = self.plateau[j][i]
                    if piece:
                        rect = self.case[i][j]
                        x = 700-rect.topleft[0]+5
                        y = 700-rect.topleft[1]
                        screen.blit(piece.getImage(), (x,y))

    def deplacer_piece(self, depart, arrivee):
        piece = self.plateau[depart[0]][depart[1]]
        piece_arrivee = self.plateau[arrivee[0]][arrivee[1]]
        plateau = self.plateau

        # on vérifie si on choisit bien une pièce à déplacer
        if piece is not None:
            # on ne peut jouer que ses propres pièces et pas celles de l'adversaire
            couleur = 'blanc' if self.getturn() % 2 == 1 else 'noir'
            if piece.getcouleur() == couleur:
                #on regarde si quand on déplace la piece on met notre roi en echec
                self.plateau[arrivee[0]][arrivee[1]] = piece
                self.plateau[depart[0]][depart[1]] = None
                if not self.est_en_echec(couleur):
                    self.plateau[depart[0]][depart[1]]= piece
                    self.plateau[arrivee[0]][arrivee[1]] = piece_arrivee
                    # Vérification du roque
                    if piece.getType_piece()=='king' and piece.peut_roquer(depart, arrivee, plateau):
                        if arrivee[1] == 6:  # Roque
                            self.plateau[depart[0]][5] = self.plateau[depart[0]][7]
                            self.plateau[depart[0]][7] = None
                        elif arrivee[1] == 2:  # Grand Roque
                            self.plateau[depart[0]][3] = self.plateau[depart[0]][0]
                            self.plateau[depart[0]][0] = None
                        piece.a_bouge = True
                        self.plateau[arrivee[0]][arrivee[1]] = piece
                        self.plateau[depart[0]][depart[1]] = None
                        self.turn += 1
                        return

                    # promotion du pion
                    if piece.getcouleur() == 'blanc' and arrivee[0] == 7 and piece.getType_piece() == 'pion':
                        transformation = 'ok'
                        # on regarde quelle pièce on veut avoir
                        while transformation not in ['Reine', 'Cavalier', 'Fou', 'Tour']:
                            transformation = input('En quelle pièce voulez-vous transformer votre pion (ex: Reine, Cavalier, etc) ')
                            # on change la pièce en Reine
                            if transformation == 'Reine':
                                piece = Reine('blanc')
                                self.plateau[arrivee[0]][arrivee[1]] = piece
                                self.plateau[depart[0]][depart[1]] = None
                                self.turn += 1
                                break
                            # on change la pièce en Cavalier
                            elif transformation == 'Cavalier':
                                piece = Cavalier('blanc')
                                self.plateau[arrivee[0]][arrivee[1]] = piece
                                self.plateau[depart[0]][depart[1]] = None
                                self.turn += 1
                                break
                            # on change la pièce en Fou
                            elif transformation == 'Fou':
                                piece = Fou('blanc')
                                self.plateau[arrivee[0]][arrivee[1]] = piece
                                self.plateau[depart[0]][depart[1]] = None
                                self.turn += 1
                                break
                            # on change la pièce en Tour
                            elif transformation == 'Tour':
                                piece = Tour('blanc')
                                self.plateau[arrivee[0]][arrivee[1]] = piece
                                self.plateau[depart[0]][depart[1]] = None
                                self.turn += 1
                                break
                            else:
                                print("Cette transformation n'est pas valide")
                    else:
                        # on regarde si on prend une pièce adverse ou pas
                        if piece_arrivee is None:
                            # Prise en passant
                            if piece.getType_piece()=='pion' and piece.peut_prendre_en_passant(depart, arrivee, plateau):
                                if piece.getcouleur() == 'blanc':
                                    self.plateau[arrivee[0] - 1][arrivee[1]] = None
                                else:
                                    self.plateau[arrivee[0] + 1][arrivee[1]] = None
                                self.plateau[arrivee[0]][arrivee[1]] = piece
                                self.plateau[depart[0]][depart[1]] = None
                                self.turn += 1
                                piece.deux_cases = False
                                return
                            # on regarde si le mouvement est valide
                            if piece and piece.mouvement_valide(depart, arrivee, piece_arrivee, plateau):
                                self.plateau[arrivee[0]][arrivee[1]] = piece
                                self.plateau[depart[0]][depart[1]] = None
                                self.turn += 1
                            else:
                                print("Mouvement invalide")
                        else:
                            # on ne peut pas manger une pièce de sa couleur
                            if piece.getcouleur() == piece_arrivee.getcouleur():
                                print('Vous ne pouvez pas prendre une pièce de votre couleur.')
                            else:
                                # on regarde si le mouvement est valide si je mange
                                if piece and piece.mouvement_valide(depart, arrivee, piece_arrivee, plateau):
                                    # compteur de points
                                    if piece_arrivee.getcouleur() == 'blanc':
                                        self.point_noir += piece_arrivee.getValeur()
                                    else:
                                        self.point_blanc += piece_arrivee.getValeur()
                                    # déplacement
                                    self.plateau[arrivee[0]][arrivee[1]] = piece
                                    self.plateau[depart[0]][depart[1]] = None
                                    self.turn += 1
                                else:
                                    print("Mouvement invalide")
                else:
                    self.plateau[depart[0]][depart[1]]= piece
                    self.plateau[arrivee[0]][arrivee[1]] = piece_arrivee
                    print('Mouvement illégale')
            else:
                print('Cette pièce ne vous appartient pas')
        else:
            print("Vous n'avez pas sélectionné de pièce")

    # demande de la case
    def demander_mouvement(self,depart,arrivee):
        try:
            # Demande la case de départ
            x1, y1 = self.convertir_case_vers_coord(depart)
            x2, y2 = self.convertir_case_vers_coord(arrivee)
            self.deplacer_piece((x1, y1), (x2, y2))
        except ValueError:
            print("Entrée invalide. Essayez encore.")

    # Convertit une notation de case comme 'a2' en coordonnées de plateau.
    def convertir_case_vers_coord(self, case):
        lettre, chiffre = case
        y = int(chiffre) - 1
        x = ord(lettre) - ord('a')  # Convertit la lettre en index (a -> 1, b -> 2, etc.)
        return y, x

    def est_en_echec(self, couleur):

        for i in range(8):
            for j in range(8):
                # Récupère la pièce à la position actuelle.
                piece = self.plateau[i][j]
                
                # Si une pièce est présente et que c'est un roi...
                if piece and piece.getType_piece() == 'king':
                    # Vérifie si c'est le roi blanc et sauvegarde sa position.
                    if piece.getcouleur() == 'blanc':
                        roi_blanc_position = (i, j)
                    # Sinon, sauvegarde la position du roi noir.
                    else:
                        roi_noir_position = (i, j)
        roi_position = roi_blanc_position if couleur == 'blanc' else roi_noir_position
        
        for i in range(8):
            for j in range(8):
                piece = self.plateau[i][j]
                if piece and piece.getcouleur() != couleur:
                    if piece.peut_attaquer((i, j), roi_position, self.plateau):
                        return True
        return False

    # Vérifie si aucun mouvement légal n'est possible pour une couleur donnée
    def aucun_mouvement_legal(self, couleur):
        # Parcourir toutes les cases du plateau
        for i in range(8):
            for j in range(8):
                piece = self.plateau[i][j]
                # Vérifier si la case contient une pièce de la couleur donnée
                if piece and piece.getcouleur() == couleur:
                    # Parcourir toutes les cases possibles d'arrivée
                    for x in range(8):
                        for y in range(8):
                            # Vérifier si le mouvement de la pièce vers la case d'arrivée est valide
                            if piece.mouvement_valide((i, j), (x, y), self.plateau[x][y], self.plateau):
                                # Sauvegarder la pièce présente sur la case d'arrivée
                                temp_piece = self.plateau[x][y]
                                # Effectuer le mouvement de la pièce
                                self.plateau[x][y] = piece
                                self.plateau[i][j] = None
                                # Vérifier si le mouvement met le roi en échec
                                if not self.est_en_echec(couleur):
                                    # Si le mouvement ne met pas le roi en échec, annuler le mouvement
                                    self.plateau[i][j] = piece
                                    self.plateau[x][y] = temp_piece
                                    # Retourner False car il existe au moins un mouvement légal
                                    return False
                                # Annuler le mouvement si le roi est en échec
                                self.plateau[i][j] = piece
                                self.plateau[x][y] = temp_piece
        # Retourner True si aucun mouvement légal n'est possible
        return True

def check_victoire(self):
        # Détermine la couleur actuelle en fonction du nombre de tours joués.
        couleur_actuelle = 'blanc' if self.turn % 2 == 1 else 'noir'
        
        # Vérifie si le joueur actuel est en échec et n'a aucun mouvement légal.
        if self.est_en_echec(couleur_actuelle) and self.aucun_mouvement_legal(couleur_actuelle):
            # Si c'est le cas, annonce que le joueur a perdu la partie.
            print("ET MAT! Le joueur ", couleur_actuelle, " a perdu.")
            return True
        
        # Vérifie si le joueur actuel n'est pas en échec mais n'a aucun mouvement légal.
        elif not self.est_en_echec(couleur_actuelle) and self.aucun_mouvement_legal(couleur_actuelle):
            # Si c'est le cas, annonce que la partie est nulle.
            print("Pat! La partie est nulle.")
            return True
        
        # Si aucune des conditions ci-dessus n'est remplie, la partie continue.
        return False

def obtenir_positions_rois(self):
        # Initialise les positions des rois comme étant None au début.
        roi_blanc_position = None
        roi_noir_position = None
        
        # Parcourt toutes les cases du plateau (8x8).
        for i in range(8):
            for j in range(8):
                # Récupère la pièce à la position actuelle.
                piece = self.plateau[i][j]
                
                # Si une pièce est présente et que c'est un roi...
                if piece and piece.getType_piece() == 'king':
                    # Vérifie si c'est le roi blanc et sauvegarde sa position.
                    if piece.getcouleur() == 'blanc':
                        roi_blanc_position = (i, j)
                    # Sinon, sauvegarde la position du roi noir.
                    else:
                        roi_noir_position = (i, j)
        
        # Retourne un tuple contenant les positions des deux rois.
        return (roi_blanc_position, roi_noir_position)


# Dictionnaire pour inverser les cases
inversion_cases = {
    'a1': 'h8', 'b1': 'g8', 'c1': 'f8', 'd1': 'e8', 'e1': 'd8', 'f1': 'c8', 'g1': 'b8', 'h1': 'a8',
    'a2': 'h7', 'b2': 'g7', 'c2': 'f7', 'd2': 'e7', 'e2': 'd7', 'f2': 'c7', 'g2': 'b7', 'h2': 'a7',
    'a3': 'h6', 'b3': 'g6', 'c3': 'f6', 'd3': 'e6', 'e3': 'd6', 'f3': 'c6', 'g3': 'b6', 'h3': 'a6',
    'a4': 'h5', 'b4': 'g5', 'c4': 'f5', 'd4': 'e5', 'e4': 'd5', 'f4': 'c5', 'g4': 'b5', 'h4': 'a5',
    'a5': 'h4', 'b5': 'g4', 'c5': 'f4', 'd5': 'e4', 'e5': 'd4', 'f5': 'c4', 'g5': 'b4', 'h5': 'a4',
    'a6': 'h3', 'b6': 'g3', 'c6': 'f3', 'd6': 'e3', 'e6': 'd3', 'f6': 'c3', 'g6': 'b3', 'h6': 'a3',
    'a7': 'h2', 'b7': 'g2', 'c7': 'f2', 'd7': 'e2', 'e7': 'd2', 'f7': 'c2', 'g7': 'b2', 'h7': 'a2',
    'a8': 'h1', 'b8': 'g1', 'c8': 'f1', 'd8': 'e1', 'e8': 'd1', 'f8': 'c1', 'g8': 'b1', 'h8': 'a1'
}

# Boucle principale
running = True
clock = pygame.time.Clock()
plateau = Plateau()  # Initialisation du plateau

selected_piece = None  # Stocke la pièce sélectionnée
selected_rect = None   # Stocke la case de départ de la pièce sélectionnée

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for name, rect in rectangles.items():
                if rect.collidepoint(pos):
                    # Convertir la case cliquée en coordonnées
                    if plateau.getturn() % 2 == 0:
                        # Inverser les cases si c'est le tour des noirs
                        name = inversion_cases[name]
                    y, x = plateau.convertir_case_vers_coord(name)
                    piece = plateau.getplateau()[y][x]
                    # Vérifier si la pièce appartient au joueur dont c'est le tour
                    if piece and piece.getcouleur() == ('blanc' if plateau.getturn() % 2 == 1 else 'noir'):
                        selected_piece = piece
                        selected_rect = name
                        print(f"Pièce sélectionnée : {selected_piece} à {selected_rect}")
                        break

        if event.type == pygame.MOUSEBUTTONUP and selected_piece:
            pos = pygame.mouse.get_pos()
            for name, rect in rectangles.items():
                if rect.collidepoint(pos):
                    depart = selected_rect
                    arrivee = name
                    if plateau.getturn() % 2 == 0:
                        # Inverser les cases si c'est le tour des noirs
                        arrivee = inversion_cases[arrivee]
                    # Inverser les cases si c'est le tour des noirs
                    print(f"Déplacement de {depart} à {arrivee}")
                    if depart == arrivee and selected_piece.getType_piece() == 'king':
                        # Si le roi est sélectionné et que la case de départ est la même que la case d'arrivée
                        selected_piece = None
                        selected_rect = None
                        break
                    else:
                        # Déplacer la pièce
                        plateau.demander_mouvement(depart, arrivee)
                        selected_piece = None
                        selected_rect = None
                        break

        if event.type == pygame.MOUSEMOTION and selected_piece:
            pos = pygame.mouse.get_pos()
            # Affiche le plateau sans la pièce sélectionnée
            screen.fill((0, 0, 0))
            screen.blit(echequier, (0, 0))
            
            # Temporairement retirer la pièce de sa case d'origine
            y, x = plateau.convertir_case_vers_coord(selected_rect)
            piece_temp = plateau.getplateau()[y][x]
            plateau.getplateau()[y][x] = None  # Retirer temporairement la pièce

            plateau.afficher(screen)  # Afficher le plateau sans la pièce sélectionnée

            # Restaurer la pièce sur sa case d'origine
            plateau.getplateau()[y][x] = piece_temp

            # Afficher la pièce en suivant la souris
            screen.blit(selected_piece.getImage(), (pos[0] - 50, pos[1] - 50))
            pygame.display.flip()

    if not selected_piece:
        # Affichage normal si aucune pièce n'est sélectionnée
        screen.fill((0, 0, 0))
        screen.blit(echequier, (0, 0))
        plateau.afficher(screen)
        pygame.display.flip()

# Vérifie si une condition de victoire est remplie
if plateau.check_victoire():
    # Si c'est le tour des noirs (nombre de tours impair)
    if plateau.getturn() % 2 == 1:
        # Affiche un message de victoire pour les noirs
        screen.blit(pygame.image.load("image/message de victoire pour les noir.PNG"), (0, 0))
    else:
        # Sinon, affiche un message de victoire pour les blancs
        screen.blit(pygame.image.load("image/message de victoire pour les blanc.PNG"), (0, 0))
    # Met à jour l'affichage pour montrer le message
    pygame.display.flip()
    # Attend une seconde pour que le joueur puisse voir le message
    pygame.time.delay(1000)
    # Vérifie si une touche est pressée
    if event.type == pygame.KEYDOWN:
        # Si la touche "Échap" est pressée, arrête la boucle principale
        if event.key == pygame.K_ESCAPE:
            running = False

# Quitte pygame proprement lorsque la boucle principale est terminée
pygame.quit()