from modules.classe_noeud import Noeud

class Arbre():
    def __init__(self, cle=None):
        if cle is not None:
            self.racine = Noeud(cle)
            self.Sag = None
            self.Sad = None
        else:
            self.racine = None
            self.Sag = None
            self.Sad = None

    def __repr__(self):
        if self.racine is None:
            return "NIL"
        return f"({self.racine}, {self.Sag}, {self.Sad})"

    def est_vide(self):
        return self.racine is None
        
    def RepresentationArbre(self, prefix=""):
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
        if arbre is None:
            return 0
        else:
            return 1 + self.Taille(arbre.Sag) + self.Taille(arbre.Sad)
                
    def LstFeuilles(self, arbre):
        liste = []
        if arbre is None:
            return liste

        if arbre.Sag is None and arbre.Sad is None:
            liste.append(str(arbre.racine))
        else:
            if arbre.Sag is not None:
                liste.extend(self.LstFeuilles(arbre.Sag))
            if arbre.Sad is not None:
                liste.extend(self.LstFeuilles(arbre.Sad))
        return liste

    def LstNoeudsInternes(self, arbre, lst_feuilles):
        liste = []
        if arbre is None:
            return liste

        if arbre.Sag is not None or arbre.Sad is not None:
            if arbre.racine not in lst_feuilles:
                liste.append(str(arbre.racine))
        
        if arbre.Sag is not None:
            liste.extend(self.LstNoeudsInternes(arbre.Sag, lst_feuilles))
        if arbre.Sad is not None:
            liste.extend(self.LstNoeudsInternes(arbre.Sad, lst_feuilles))
        
        return liste
    
    def HauteurArbre(self, dico_hauteur, lst_feuilles = []):
        return dico_hauteur[max(dico_hauteur)]

    def LC(self, dico_hauteur):
        longueur = 0
        for i in dico_hauteur:
            longueur += dico_hauteur[i]
        return longueur

    def LCE(self, dico_hauteur, lst_feuilles):
        longueur = 0
        liste_noeud = list(dico_hauteur.keys())
        for feuille in lst_feuilles:
            if feuille in liste_noeud:
                longueur += dico_hauteur[feuille] 
        return longueur
    
    def LCI(self, dico_hauteur, lst_noeuds_internes):
        longueur = 0
        for noeud in lst_noeuds_internes:
            if noeud in dico_hauteur:
                longueur += dico_hauteur[noeud]
        return longueur
    
    def PM(self, lc, arbre):
        profondeur = lc/self.Taille(arbre)
        return round(profondeur, 2)
    
    def PME(self, lce,lst_feuilles):
        profondeur = lce/len(lst_feuilles)
        return round(profondeur, 2)

    def PMI(self, lci,lst_feuilles, arbre):
        if (self.Taille(arbre) - len(lst_feuilles)) == 0:
            return 0
        profondeur = lci/(self.Taille(arbre) - len(lst_feuilles))
        return round(profondeur, 2)
    