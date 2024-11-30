from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QFrame, QLabel, QMessageBox, QWidget
from PyQt5 import QtCore
from ui.fenetre_principale import Ui_MainWindow
from ui.premier_noeud_dialog import Premier_Noeud_Dialog
from ui.noeud_creation_dialog import Noeud_Creation_Dialog
from modules.classe_arbre import Arbre

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.resetTree.clicked.connect(self.reinitialiser_arbre)
        self.ui.pushButton.clicked.connect(self.ajouter_premier_noeud)

        self.arbre = None
        self.arbre_nom = None
        self.noeud_nom = None

        self.colonne_offset = 2000

        self.widgets_graphiques = []
        self.liens_a_dessiner = []

    def reinitialiser_arbre(self):
        """Réinitialise l'arbre en supprimant tout."""

        for widget in self.widgets_graphiques:
            widget.deleteLater()
        for lien in self.liens_a_dessiner:
            lien.deleteLater()
        self.widgets_graphiques.clear()
        self.liens_a_dessiner.clear()

        self.arbre = None
        self.arbre_nom = None
        self.noeud_nom = None

        self.ui.nom_arbre_placeholder.setText("N/A")  
        self.ui.hauteur_arbre_placeholder.setText("N/A")
        self.ui.taille_arbre_placeholder.setText("N/A")
        self.ui.lc_placeholder.setText("N/A")
        self.ui.lce_placeholder.setText("N/A")
        self.ui.lci_placeholder.setText("N/A")
        self.ui.pm_placeholder.setText("N/A")
        self.ui.pme_placeholder.setText("N/A")
        self.ui.pmi_placeholder.setText("N/A")

        self.ui.pushButton.show()
    
    def ajouter_premier_noeud(self):
        """Créer le premier nœud de l'arbre."""
        dialog = PremierNoeudCreationDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.arbre_nom = dialog.nom_arbre
            self.premier_noeud_nom = dialog.nom_noeud

            self.ui.pushButton.hide()

            self.arbre = Arbre(self.premier_noeud_nom)

            self.creer_noeud_graphiquement(self.arbre, 2, 0)

            self.ui.nom_arbre_placeholder.setText(f"{self.arbre_nom}")
            self.mettre_a_jour_labels()

    def creer_noeud_graphiquement(self, noeud, x, profondeur=0):
        """Créer un nœud graphique lié à un nœud logique."""

        frame = QFrame(self.ui.scrollAreaWidgetNoeuds)
        frame.setStyleSheet("""
                            QFrame {
                                background-color: orange;
                                border-radius: 10px;
                            }

                            QToolTip {
                                background-color: #333333;
                                color: #ffffff;
                                border: 1px solid #777777;
                                border-radius: 5px;
                                padding: 8px;
                                font-family: "Arial", sans-serif;
                                font-size: 12px;
                                max-width: 250px;
                            }

                            QToolTip::opaque {
                                background-color: rgba(0, 0, 0, 0.7);
                                border: none;
                            }

                            QToolTip::label {
                                padding: 0 4px;
                            }

                            """)
        frame.setFixedSize(100, 35)
        frame.setObjectName(f"frame_{noeud.racine.cle}")
        frame.setToolTip(f"Noeud: {noeud.racine.cle}\n • Profondeur: {profondeur}") 

        label = QLabel(frame)
        label.setText(noeud.racine.cle)
        label.setStyleSheet("color: white; font-weight: bold; font-size: 14px;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setGeometry(10, 10, frame.width() - 20, frame.height() - 20)

        bouton_gauche = QPushButton("+", self.ui.scrollAreaWidgetNoeuds)
        bouton_gauche.setFixedSize(25, 25)
        bouton_gauche.setStyleSheet("background-color: #45ff00; color: white; border-radius: 10px;")
        bouton_gauche.clicked.connect(lambda: self.ajouter_noeud(noeud, "gauche"))

        bouton_droit = QPushButton("+", self.ui.scrollAreaWidgetNoeuds)
        bouton_droit.setFixedSize(25, 25)
        bouton_droit.setStyleSheet("background-color: #45ff00; color: white; border-radius: 10px;")
        bouton_droit.clicked.connect(lambda: self.ajouter_noeud(noeud, "droit"))

        noeud.bouton_gauche = bouton_gauche
        noeud.bouton_droit = bouton_droit
        noeud.profondeur = profondeur

        self.widgets_graphiques.extend([frame, bouton_gauche, bouton_droit])

        colonne = int(x + self.colonne_offset)
        ligne = int(profondeur)

        self.ui.gridLayout_noeuds.addWidget(frame, ligne, colonne)
        self.ui.gridLayout_noeuds.addWidget(bouton_gauche, ligne + 1, colonne - 1)
        self.ui.gridLayout_noeuds.addWidget(bouton_droit, ligne + 1, colonne + 1)

        noeud.x = colonne
        noeud.y = ligne

        frame.show()
        bouton_gauche.show()
        bouton_droit.show()

    def ajouter_noeud(self, parent_noeud, direction):
        """Ajouter un nœud à gauche ou à droite, en maintenant l'organisation de l'arbre."""
        dialog = CreationDialog(self)
        if dialog.exec() == QDialog.Accepted:
            nom_noeud = dialog.nom_noeud

            if direction == "gauche":
                if parent_noeud.Sag is None:
                    parent_noeud.Sag = Arbre(nom_noeud)
                    enfant = parent_noeud.Sag
                    x_offset = -2 ** (5 - parent_noeud.profondeur)
                else:
                    QMessageBox.warning(self, "Erreur", "Le sous-arbre gauche existe déjà")
                    return
            else:
                if parent_noeud.Sad is None:
                    parent_noeud.Sad = Arbre(nom_noeud)
                    enfant = parent_noeud.Sad
                    x_offset = 2 ** (5 - parent_noeud.profondeur)
                else:
                    QMessageBox.warning(self, "Erreur", "Le sous-arbre droit existe déjà")
                    return

            x = parent_noeud.x + x_offset

            self.creer_noeud_graphiquement(enfant, x - self.colonne_offset, profondeur=parent_noeud.profondeur + 1)

            if direction == "gauche" and hasattr(parent_noeud, "bouton_gauche"):
                parent_noeud.bouton_gauche.hide()
            elif direction == "droit" and hasattr(parent_noeud, "bouton_droit"):
                parent_noeud.bouton_droit.hide()

            self.mettre_a_jour_labels()
            self.update()


    def mettre_a_jour_labels(self):
        dico_hauteur = self.arbre.Hauteur(self.arbre)
        
        lst_feuilles = self.arbre.LstFeuilles(self.arbre)
        lst_noeuds_internes = self.arbre.LstNoeudsInternes(self.arbre, lst_feuilles)
        
        hauteur_arbre = self.arbre.HauteurArbre(dico_hauteur, lst_feuilles)
        taille_arbre = self.arbre.Taille(self.arbre)
        lc = self.arbre.LC(dico_hauteur)
        lce = self.arbre.LCE(dico_hauteur, lst_feuilles)
        lci = self.arbre.LCI(dico_hauteur, lst_noeuds_internes)
        
        pm = self.arbre.PM(lc, self.arbre)
        pme = self.arbre.PME(lce, lst_feuilles)
        pmi = self.arbre.PMI(lci, lst_feuilles, self.arbre)
        
        self.ui.hauteur_arbre_placeholder.setText(str(hauteur_arbre))
        self.ui.taille_arbre_placeholder.setText(str(taille_arbre))
        self.ui.lc_placeholder.setText(str(lc))
        self.ui.lce_placeholder.setText(str(lce))
        self.ui.lci_placeholder.setText(str(lci))
        self.ui.pm_placeholder.setText(str(pm))
        self.ui.pme_placeholder.setText(str(pme))
        self.ui.pmi_placeholder.setText(str(pmi))


class PremierNoeudCreationDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Premier_Noeud_Dialog()
        self.ui.setupUi(self)

        self.ui.confirm.clicked.connect(self.accept_action)

    def accept_action(self):
        self.nom_arbre = self.ui.nom_arbre_creation.toPlainText().strip()
        self.nom_noeud = self.ui.nom_noeu_creation.toPlainText().strip()

        if self.nom_arbre and self.nom_noeud:
            self.accept()

class CreationDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = Noeud_Creation_Dialog()
        self.ui.setupUi(self)

        self.nom_noeud = ""

        self.ui.confirm.clicked.connect(self.accept_action)

    def accept_action(self):
        self.nom_noeud = self.ui.nom_noeu_creation.toPlainText().strip()

        if self.nom_noeud:
            self.accept()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
