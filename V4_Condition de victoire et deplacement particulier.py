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

class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "king", 0)
        self.a_bouge = False

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        if plateau[arrivee[0]][arrivee[1]]  != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur()==self.getcouleur():
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

        if arrivee[1] == 7:  # Roque 
            tour = plateau[depart[0]][8]
            if isinstance(tour, Tour) and not tour.a_bouge:
                for i in range(6, 8):
                    if plateau[depart[0]][i] is not None:
                        return False
                return True
        elif arrivee[1] == 3:  # Franc Roque
            tour = plateau[depart[0]][1]
            if isinstance(tour, Tour) and not tour.a_bouge:
                for i in range(2, 5):
                    if plateau[depart[0]][i] is not None:
                        return False
                return True
        return False

class Reine(Piece):
    def __init__(self, couleur):
        super().__init__(couleur, "queen", 9)

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        # La reine peut se déplacer en ligne droite ou en diagonale
        dy = abs(depart[0] - arrivee[0])
        dx = abs(depart[1] - arrivee[1])
    
        if plateau[arrivee[0]][arrivee[1]]  != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur()==self.getcouleur():
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

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):

        if plateau[arrivee[0]][arrivee[1]]  != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur()==self.getcouleur():
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

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):

        if plateau[arrivee[0]][arrivee[1]]  != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur()==self.getcouleur():
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

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        if plateau[arrivee[0]][arrivee[1]]  != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur()==self.getcouleur():
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

    def mouvement_valide(self, depart, arrivee, piece_arrivee, plateau):
        if plateau[arrivee[0]][arrivee[1]]  != None:
            if plateau[arrivee[0]][arrivee[1]].getcouleur()==self.getcouleur():
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
                if piece_adverse.getType_piece()=='pion' and piece_adverse.deux_cases:
                    return True
        return False

class Plateau:
    def __init__(self):
        self.plateau = [[None] * 9 for _ in range(8)]
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
        self.plateau[0] = ['1 | ', Tour('blanc'), Cavalier('blanc'), Fou('blanc'), Reine('blanc'), Roi('blanc'), Fou('blanc'), Cavalier('blanc'), Tour('blanc')]
        self.plateau[1] = [Pion('blanc')] * 9
        # on place les pieces noires
        self.plateau[6] = [Pion('noir')] * 9
        self.plateau[7] = ['8 | ', Tour('noir'), Cavalier('noir'), Fou('noir'), Reine('noir'), Roi('noir'), Fou('noir'), Cavalier('noir'), Tour('noir')]
        # on affiche les autres noms de ligne
        self.plateau[1][0] = '2 | '
        self.plateau[2][0] = '3 | '
        self.plateau[3][0] = '4 | '
        self.plateau[4][0] = '5 | '
        self.plateau[5][0] = '6 | '
        self.plateau[6][0] = '7 | '

        # Vérification de l'initialisation
        self.afficher_positions_rois()

    # on affiche le plateau de jeu
    def afficher(self):
        if self.turn % 2 == 1:
            for ligne in reversed(self.plateau):
                print(' '.join([str(piece) if piece else '.' for piece in ligne]))
        else:
            for ligne in self.plateau:
                print(' '.join([str(piece) if piece else '.' for piece in ligne]))

        # on affiche les noms de colonne
        print('     _______________')
        print('     A B C D E F G H')

    # déplacement de la pièce
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
                        if arrivee[1] == 7:  # Roque 
                            self.plateau[depart[0]][6] = self.plateau[depart[0]][8]
                            self.plateau[depart[0]][8] = None
                        elif arrivee[1] == 3:  # Franc Roque 
                            self.plateau[depart[0]][4] = self.plateau[depart[0]][1]
                            self.plateau[depart[0]][1] = None
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
    def demander_mouvement(self):
        while True:
            try:
                # Demande la case de départ
                depart = input("Entrez la case de départ (ex: a2) : ")
                x1, y1 = self.convertir_case_vers_coord(depart)

                # Demande la case d'arrivée
                arrivee = input("Entrez la case d'arrivée (ex: a3) : ")
                x2, y2 = self.convertir_case_vers_coord(arrivee)

                # Déplace la pièce
                self.deplacer_piece((x1, y1), (x2, y2))
                break
            except ValueError:
                print("Entrée invalide. Essayez encore.")

    # Convertit une notation de case comme 'a2' en coordonnées de plateau.
    def convertir_case_vers_coord(self, case):
        lettre, chiffre = case
        y = int(chiffre) - 1
        x = ord(lettre) - ord('a') + 1  # Convertit la lettre en index (a -> 1, b -> 2, etc.)
        return y, x

    def est_en_echec(self, couleur):

        roi_position = self.afficher_positions_rois()[0] if couleur =='blanc' else self.afficher_positions_rois()[1]

        for i in range(8):
            for j in range(1, 9):
                piece = self.plateau[i][j]
                if piece and piece.getcouleur() != couleur:
                    if piece.peut_attaquer((i, j), roi_position, self.plateau):
                        return True
        return False

    # Vérifie si aucun mouvement légal n'est possible pour une couleur donnée
    def aucun_mouvement_legal(self, couleur):
        # Parcourir toutes les cases du plateau
        for i in range(8):
            for j in range(1, 9):
                piece = self.plateau[i][j]
                # Vérifier si la case contient une pièce de la couleur donnée
                if piece and piece.getcouleur() == couleur:
                    # Parcourir toutes les cases possibles d'arrivée
                    for x in range(8):
                        for y in range(1, 9):
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
        couleur_actuelle = 'blanc' if self.turn % 2 == 1 else 'noir'
        if self.est_en_echec(couleur_actuelle) and self.aucun_mouvement_legal(couleur_actuelle):
            print("ET MAT! Le joueur ", couleur_actuelle, " a perdu.")
            return True
        elif not self.est_en_echec(couleur_actuelle) and self.aucun_mouvement_legal(couleur_actuelle):
            print("Pat! La partie est nulle.")
            return True
        return False
    
    def afficher_positions_rois(self):
        roi_blanc_position = None
        roi_noir_position = None
        for i in range(8):
            for j in range(1, 9):
                piece = self.plateau[i][j]
                if piece and piece.getType_piece() == 'king':
                    if piece.getcouleur() == 'blanc':
                        roi_blanc_position = (i, j)
                    else:
                        roi_noir_position = (i, j)

        return (roi_blanc_position, roi_noir_position)

if __name__ == "__main__":
    plateau = Plateau()
    plateau.afficher()
    flag = True
    while flag:
        print('tour :', plateau.getturn())
        print('point blanc :', plateau.getPoint_blanc())
        print('point noir :', plateau.getPoint_noir())
        plateau.demander_mouvement()
        plateau.afficher()
        if plateau.est_en_echec('blanc' if plateau.getturn()%2==1 else 'noir'):
            print('Echec')
        if plateau.check_victoire():
            break
