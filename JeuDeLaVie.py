import random

class JeuDeLaVie():
    def __init__(self, lig, col):
        self.__lig = lig
        self.__col = col
        self.__matrice = [[(random.randint(0, 1)) for _ in range(self.__lig)] for _ in range(self.__col)]
        self.__historique = []

    @property
    def get_lig(self):
        return self.__lig
    
    @property
    def get_col(self):
        return self.__col
    
    @property
    def get_matrice(self):
        return self.__matrice

    @property
    def get_historique(self):
        return self.__historique
    
    def nb_voisines_vivantes(self, i, j):
        count = 0
        for x in range(max(0, i-1), min(self.__lig, i+2)):
            for y in range(max(0, j-1), min(self.__col, j+2)):
                if (x, y) != (i, j) and self.__matrice[x][y] == 1:
                    count += 1
        return count
    
    def etape(self):
        self.__historique.append(self.__matrice)
        new_matrice = [[0 for _ in range(self.__lig)] for _ in range(self.__col)]
        for i in range(self.__lig):
            for j in range(self.__col):
                if self.__matrice[i][j] == 1:
                    if self.nb_voisines_vivantes(i, j) in [2, 3]:
                        new_matrice[i][j] = 1
                else:
                    if self.nb_voisines_vivantes(i, j) == 3:
                        new_matrice[i][j] = 1
        self.__matrice = new_matrice
    
    def clear(self):
        self.__matrice = [[0 for _ in range(self.__lig)] for _ in range(self.__col)]
        self.__historique = []
    
    def reset(self):
        self.__matrice = [[(random.randint(0, 1)) for _ in range(self.__lig)] for _ in range(self.__col)]
        self.__historique = []

    def etape_precedente(self):
        if self.__historique:
            self.__matrice = self.__historique.pop()
