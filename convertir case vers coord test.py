def convertir_case_vers_coord(case):
        lettre, chiffre = case
        y= int(chiffre)  # Inverse la notation des lignes, car la ligne 8 est la première
        x = ord(lettre) - ord('a')+1  # Convertie la lettre en index (a -> 0, b -> 1, etc.)
        return y,x 

print(convertir_case_vers_coord('a2'))