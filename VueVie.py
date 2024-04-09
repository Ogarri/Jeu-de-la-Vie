import tkinter as tk
import JeuDeLaVie as jdv

class VueVie(tk.Tk):
    def __init__(self, lig, col):
        tk.Tk.__init__(self)
        self.__lig = lig
        self.__col = col
        self.__jeu = jdv.JeuDeLaVie(lig, col)
        self.__canvas = tk.Canvas(self, width=col*20, height=lig*20, bg='white')
        self.__button_next = tk.Button(self, text='Étape suivante', command=self.__etape)
        self.__button_next_auto = tk.Button(self, text='Démarrer', command=self.__demarrer)
        self.__button_clear = tk.Button(self, text='Effacer', command=self.__jeu.clear)
        self.__button_reset = tk.Button(self, text='Réinitialiser', command=self.__jeu.reset)
        self.__canvas.pack()
        self.__dessiner()
        self.bind('<Button-1>', self.__clic)
        self.bind('<Return>', self.__etape)
        self.__button_next.pack()
        self.__button_next_auto.pack()
        self.__button_clear.pack()
        self.__button_reset.pack()
    
    def __dessiner(self):
        self.__canvas.delete('all')
        for i in range(self.__lig):
            for j in range(self.__col):
                if self.__jeu.get_matrice[i][j] == 1:
                    self.__canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill='black')

    def __clic(self, event):
        i = event.y // 20
        j = event.x // 20
        self.__jeu.get_matrice[i][j] = 1 - self.__jeu.get_matrice[i][j]
        self.__dessiner()
    
    def __etape(self, event=None):
        self.__jeu.etape()
        self.__dessiner()
    
    def __demarrer(self):
        self.__button_next_auto.config(text='Arrêter', command=self.__arreter)
        self.__etape_auto()
    
    def __arreter(self):
        self.__button_next_auto.config(text='Démarrer', command=self.__demarrer)
        self.after_cancel(self.__id_after)
    
    def __etape_auto(self):
        self.__etape()
        self.__id_after = self.after(1000, self.__etape_auto)
