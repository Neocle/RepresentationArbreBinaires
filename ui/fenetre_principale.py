# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetre_principale.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGridLayout, QScrollArea, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('./images/icon.webp'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1067, 609)
        MainWindow.setStyleSheet("background-color: white\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -30, 291, 661))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #eafaf1; \n"
"    border: 2px solid black;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()

        self.scrollArea_noeuds = QScrollArea(self.centralwidget)
        self.scrollArea_noeuds.setGeometry(QtCore.QRect(300, 20, 700, 500))  # Position et taille
        self.scrollArea_noeuds.setStyleSheet("* { border: none; background-color: rgba(0, 0, 0, 0); }")
        self.scrollArea_noeuds.setWidgetResizable(True)
        self.scrollArea_noeuds.setObjectName("scrollArea_noeuds")

        self.scrollAreaWidgetNoeuds = QWidget()
        self.scrollAreaWidgetNoeuds.setObjectName("scrollAreaWidgetNoeuds")
        self.gridLayout_noeuds = QGridLayout(self.scrollAreaWidgetNoeuds)
        self.gridLayout_noeuds.setObjectName("gridLayout_noeuds")

        self.scrollArea_noeuds.setWidget(self.scrollAreaWidgetNoeuds)
        MainWindow.setCentralWidget(self.centralwidget)

        self.resetTree = QtWidgets.QPushButton(self.frame)
        self.resetTree.setGeometry(QtCore.QRect(30, 560, 241, 51))
        self.resetTree.setStyleSheet("QPushButton {\n"
"    background-color: #e74c3c;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c0392b; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #a93226;\n"
"    border: 2px solid #922b21; \n"
"}\n"
"")
        self.resetTree.setObjectName("resetTree")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 30, 291, 331))
        self.scrollArea.setStyleSheet("\n"
        "* { \n"
        "    border: none;\n"
        "    background-color: rgba(0,0,0,0);\n"
        "}"
        "")
        self.scrollArea.verticalScrollBar().setStyleSheet("""
        QScrollBar:vertical {
        border: none;
        background-color: rgba(0,0,0,0);
        width: 10px; 
        margin: 0px; 
        }

        QScrollBar::handle:vertical {
        background: #888; 
        min-height: 20px;
        border-radius: 5px;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        border: none;
        background: none;
        height: 0px;
        }
        """)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 261, 670))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.nom_arbre_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nom_arbre_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.nom_arbre_placeholder.setObjectName("nom_arbre_placeholder")
        self.gridLayout.addWidget(self.nom_arbre_placeholder, 1, 0, 1, 1)
        self.taille_arbre_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.taille_arbre_label.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.taille_arbre_label.setObjectName("taille_arbre_label")
        self.gridLayout.addWidget(self.taille_arbre_label, 4, 0, 1, 1)
        self.taille_arbre_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.taille_arbre_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.taille_arbre_placeholder.setObjectName("taille_arbre_placeholder")
        self.gridLayout.addWidget(self.taille_arbre_placeholder, 5, 0, 1, 1)
        self.nom_arbre_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nom_arbre_label.setMinimumSize(QtCore.QSize(236, 37))
        self.nom_arbre_label.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.nom_arbre_label.setObjectName("nom_arbre_label")
        self.gridLayout.addWidget(self.nom_arbre_label, 0, 0, 1, 1)
        self.pme_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pme_label.setStyleSheet("font-size: 10px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.pme_label.setObjectName("pme_label")
        self.gridLayout.addWidget(self.pme_label, 17, 0, 1, 1)
        self.pmi_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pmi_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.pmi_placeholder.setObjectName("pmi_placeholder")
        self.gridLayout.addWidget(self.pmi_placeholder, 20, 0, 1, 1)
        self.pm_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pm_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.pm_placeholder.setObjectName("pm_placeholder")
        self.gridLayout.addWidget(self.pm_placeholder, 16, 0, 1, 1)
        self.pm_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pm_label.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.pm_label.setObjectName("pm_label")
        self.gridLayout.addWidget(self.pm_label, 15, 0, 1, 1)
        self.pme_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pme_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.pme_placeholder.setObjectName("pme_placeholder")
        self.gridLayout.addWidget(self.pme_placeholder, 18, 0, 1, 1)
        self.hauteur_arbre_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hauteur_arbre_label.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.hauteur_arbre_label.setObjectName("hauteur_arbre_label")
        self.gridLayout.addWidget(self.hauteur_arbre_label, 6, 0, 1, 1)
        self.hauteur_arbre_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hauteur_arbre_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.hauteur_arbre_placeholder.setObjectName("hauteur_arbre_placeholder")
        self.gridLayout.addWidget(self.hauteur_arbre_placeholder, 8, 0, 1, 1)
        self.lci_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lci_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.lci_placeholder.setObjectName("lci_placeholder")
        self.gridLayout.addWidget(self.lci_placeholder, 14, 0, 1, 1)
        self.lce_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lce_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.lce_placeholder.setObjectName("lce_placeholder")
        self.gridLayout.addWidget(self.lce_placeholder, 12, 0, 1, 1)
        self.lc_placeholder = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lc_placeholder.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.lc_placeholder.setObjectName("lc_placeholder")
        self.gridLayout.addWidget(self.lc_placeholder, 10, 0, 1, 1)
        self.lce_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lce_label.setStyleSheet("font-size: 10px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.lce_label.setObjectName("lce_label")
        self.gridLayout.addWidget(self.lce_label, 11, 0, 1, 1)
        self.lc_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lc_label.setStyleSheet("font-size: 12px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.lc_label.setObjectName("lc_label")
        self.gridLayout.addWidget(self.lc_label, 9, 0, 1, 1)
        self.lci_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lci_label.setStyleSheet("font-size: 10px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.lci_label.setObjectName("lci_label")
        self.gridLayout.addWidget(self.lci_label, 13, 0, 1, 1)
        self.pmi_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.pmi_label.setStyleSheet("font-size: 10px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.pmi_label.setObjectName("pmi_label")
        self.gridLayout.addWidget(self.pmi_label, 19, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(90, 380, 118, 3))
        self.line.setStyleSheet("border: 2px solid black")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 50, 151, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #45ff00;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #34c200; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2ea802;\n"
"    border: 2px solid #2c9e02; \n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arbres Binaires"))
        self.resetTree.setText(_translate("MainWindow", "Reset l\'arbre"))
        self.nom_arbre_placeholder.setText(_translate("MainWindow", "N/A"))
        self.taille_arbre_label.setText(_translate("MainWindow", "Taille (nb de noeuds)"))
        self.taille_arbre_placeholder.setText(_translate("MainWindow", "N/A"))
        self.nom_arbre_label.setText(_translate("MainWindow", "Nom"))
        self.pme_label.setText(_translate("MainWindow", "Profondeur moyenne externe"))
        self.pmi_placeholder.setText(_translate("MainWindow", "N/A"))
        self.pm_placeholder.setText(_translate("MainWindow", "N/A"))
        self.pm_label.setText(_translate("MainWindow", "Profondeur moyenne"))
        self.pme_placeholder.setText(_translate("MainWindow", "N/A"))
        self.hauteur_arbre_label.setText(_translate("MainWindow", "Hauteur"))
        self.hauteur_arbre_placeholder.setText(_translate("MainWindow", "N/A"))
        self.lci_placeholder.setText(_translate("MainWindow", "N/A"))
        self.lce_placeholder.setText(_translate("MainWindow", "N/A"))
        self.lc_placeholder.setText(_translate("MainWindow", "N/A"))
        self.lce_label.setText(_translate("MainWindow", "Longueur de cheminement externe"))
        self.lc_label.setText(_translate("MainWindow", "Longueur de cheminement"))
        self.lci_label.setText(_translate("MainWindow", "Longueur de cheminement interne"))
        self.pmi_label.setText(_translate("MainWindow", "Profondeur moyenne interne"))
        self.pushButton.setText(_translate("MainWindow", "Ajouter Noeud"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
