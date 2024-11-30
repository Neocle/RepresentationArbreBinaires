class Noeud:
    def __init__(self, cle):
        """Cree un nœud avec une cle donnee"""
        self.cle = cle
    def __repr__(self):
        return str(self.cle)
