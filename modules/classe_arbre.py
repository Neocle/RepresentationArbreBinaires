from modules.classe_noeud import Noeud

class Arbre():
    """
    Représente un arbre binaire
    """
    
    def __init__(self, cle=None):
        """
        Initialise un arbre avec ou sans racine
        
        Args:
            cle: La clé de la racine de l'arbre
        """
        if cle is not None:
            self.racine = Noeud(cle)
            self.Sag = None
            self.Sad = None
        else:
            self.racine = None
            self.Sag = None
            self.Sad = None

    def __repr__(self):
        """
        Représente l'arbre sous forme de charactères
        
        Returns:
            str: La représentation de l'arbre
        """
        if self.racine is None:
            return "NIL"
        return f"({self.racine}, {self.Sag}, {self.Sad})"

    def est_vide(self):
        """
        Vérifie si l'arbre est vide
        
        Returns:
            bool: True si l'arbre est vide et False sinon
        """
        return self.racine is None
        
    def RepresentationArbre(self, prefix=""):
        """
        Affiche la structure de l'arbre
        
        Args:
            prefix (str): Le prefixe pour l'affichage de l'arbre
        """
        if self.est_vide():
            return
        print(f"{prefix}{self.racine.cle}")
        if self.Sad:
            self.Sad.RepresentationArbre(prefix + "   ")
        else:
            print(f"{prefix}   🍁")
        if self.Sag:
            self.Sag.RepresentationArbre(prefix + "   ")
        else:
            print(f"{prefix}   🍁")

    def Hauteur(self, arbre):
        """
        Calcule la hauteur de l'arbre
        
        Args:
            arbre (Arbre): L'arbre pour lequel on calcule la hauteur
        
        Returns:
            dict: Dictionnaire des hauteurs de chaque nœud
        """
        if arbre.est_vide():
            return {}
        
        dictionnaire = {}
        pile = [(self, 0)]

        while pile:
            sous_arbre, hauteur = pile.pop()
            if sous_arbre and sous_arbre.racine:
                dictionnaire[sous_arbre.racine.cle] = hauteur
                if sous_arbre.Sad:
                    pile.append((sous_arbre.Sad, hauteur + 1))
                if sous_arbre.Sag:
                    pile.append((sous_arbre.Sag, hauteur + 1))

        return dictionnaire
    
    def Taille(self, arbre):
        """
        Calcule la taille de l'arbre
        
        Args:
            arbre (Arbre): L'arbre pour lequel on calcule la taille
        
        Returns:
            int: La taille de l'arbre
        """
        if arbre is None:
            return 0
        return 1 + self.Taille(arbre.Sag) + self.Taille(arbre.Sad)
                
    def LstFeuilles(self, arbre):
        """
        Récupère la liste des feuilles de l'arbre
        
        Args:
            arbre (Arbre): L'arbre pour lequel on récupère les feuilles
        
        Returns:
            list: Liste des clés des feuilles de l'arbre
        """
        liste = []
        if arbre is None:
            return liste

        if arbre.Sag is None and arbre.Sad is None:
            liste.append(str(arbre.racine))
        else:
            if arbre.Sag:
                liste.extend(self.LstFeuilles(arbre.Sag))
            if arbre.Sad:
                liste.extend(self.LstFeuilles(arbre.Sad))
        return liste

    def LstNoeudsInternes(self, arbre, lst_feuilles):
        """
        Récupère les nœuds internes de l'arbre
        
        Args:
            arbre (Arbre): L'arbre
            lst_feuilles (list): Liste des feuilles
        
        Returns:
            list: Liste des nœuds internes
        """
        liste = []
        if arbre is None:
            return liste

        if arbre.Sag or arbre.Sad:
            if arbre.racine not in lst_feuilles:
                liste.append(str(arbre.racine))
        
        if arbre.Sag:
            liste.extend(self.LstNoeudsInternes(arbre.Sag, lst_feuilles))
        if arbre.Sad:
            liste.extend(self.LstNoeudsInternes(arbre.Sad, lst_feuilles))
        
        return liste
    
    def HauteurArbre(self, dico_hauteur, lst_feuilles=[]):
        """
        Calcule la hauteur totale de l'arbre
        
        Args:
            dico_hauteur (dict): Dictionnaire des hauteurs des nœuds
        
        Returns:
            int: Hauteur maximale de l'arbre
        """
        return dico_hauteur[max(dico_hauteur)]

    def LC(self, dico_hauteur):
        """
        Calcule la longueur des hauteurs des nœuds
    
        Args:
            dico_hauteur (dict): Dictionnaire des hauteurs des nœuds
        
        Returns:
            int: Longueur des hauteurs
        """
        longueur = 0
        for i in dico_hauteur:
            longueur += dico_hauteur[i]
        return longueur

    def LCE(self, dico_hauteur, lst_feuilles):
        """
        Calcule la longueur des hauteurs des feuilles
        
        Args:
            dico_hauteur (dict): Dictionnaire des hauteurs des nœuds
            lst_feuilles (list): Liste des feuilles de l'arbre
        
        Returns:
            int: Longueur des hauteurs des feuilles
        """
        longueur = 0
        liste_noeud = list(dico_hauteur.keys())
        for feuille in lst_feuilles:
            if feuille in liste_noeud:
                longueur += dico_hauteur[feuille]
        return longueur
    
    def LCI(self, dico_hauteur, lst_noeuds_internes):
        """
        Calcule la longueur des hauteurs des nœuds internes
        
        Args:
            dico_hauteur (dict): Dictionnaire des hauteurs des nœuds
            lst_noeuds_internes (list): Liste des nœuds internes
        
        Returns
            int: Longueur des hauteurs des nœuds internes
        """
        longueur = 0
        for noeud in lst_noeuds_internes:
            if noeud in dico_hauteur:
                longueur += dico_hauteur[noeud]
        return longueur
    
    def PM(self, lc, arbre):
        """
        Calcule la profondeur moyenne de l'arbre
        
        Args:
            lc (int): Longueur des hauteurs des nœuds
            arbre (Arbre): L'arbre pour lequel on calcule la profondeur
        
        Returns:
            float: La profondeur moyenne de l'arbre
        """
        profondeur = lc / self.Taille(arbre)
        return round(profondeur, 2)

    def PME(self, lce, lst_feuilles):
        """
        Calcule la profondeur moyenne des feuilles
        
        Args:
            lce (int): Longueur des hauteurs des feuilles
            lst_feuilles (list): Liste des feuilles de l'arbre
        
        Returns:
            float: La profondeur moyenne des feuilles
        """
        profondeur = lce / len(lst_feuilles)
        return round(profondeur, 2)

    def PMI(self, lci, lst_feuilles, arbre):
        """
        Calcule la profondeur moyenne des nœuds internes
        
        Args:
            lci (int): Longueur des hauteurs des nœuds internes
            lst_feuilles (list): Liste des feuilles de l'arbre
            arbre (Arbre): L'arbre pour lequel on calcule la profndeur
        
        Returns:
            float: La profondeur moyenne des nœuds internes
        """
        if (self.Taille(arbre) - len(lst_feuilles)) == 0:
            return 0
        profondeur = lci / (self.Taille(arbre) - len(lst_feuilles))
        return round(profondeur, 2)
