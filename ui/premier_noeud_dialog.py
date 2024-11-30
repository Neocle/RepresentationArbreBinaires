# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'premier_noeud_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Premier_Noeud_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('./images/icon.webp'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 300)
        Dialog.setStyleSheet("    background-color: #eafaf1; ")
        self.taille_arbre_label_2 = QtWidgets.QLabel(Dialog)
        self.taille_arbre_label_2.setGeometry(QtCore.QRect(60, 20, 291, 51))
        self.taille_arbre_label_2.setStyleSheet("QLabel {\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    background-color: rgba(0,0,0,0);\n"
"    border: none;\n"
"}")
        self.taille_arbre_label_2.setObjectName("taille_arbre_label_2")
        self.confirm = QtWidgets.QPushButton(Dialog)
        self.confirm.setGeometry(QtCore.QRect(130, 230, 151, 41))
        self.confirm.setStyleSheet("QPushButton {\n"
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
        self.confirm.setObjectName("confirm")
        self.nom_noeu_creation = QtWidgets.QTextEdit(Dialog)
        self.nom_noeu_creation.setGeometry(QtCore.QRect(80, 180, 251, 41))
        self.nom_noeu_creation.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.nom_noeu_creation.setText("")
        self.nom_noeu_creation.setObjectName("nom_noeu_creation")
        self.nom_noeud_creation_label = QtWidgets.QLabel(Dialog)
        self.nom_noeud_creation_label.setGeometry(QtCore.QRect(90, 150, 243, 37))
        self.nom_noeud_creation_label.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.nom_noeud_creation_label.setObjectName("nom_noeud_creation_label")
        self.nom_arbre_creation = QtWidgets.QTextEdit(Dialog)
        self.nom_arbre_creation.setGeometry(QtCore.QRect(80, 110, 251, 41))
        self.nom_arbre_creation.setStyleSheet("QLabel {\n"
"    color: black; /* Text color matching the poker table green for a cohesive look */\n"
"    background-color: white; /* Light background color for contrast */\n"
"    border: 1px solid #B0C4DE; /* Light gray-blue border */\n"
"    border-radius: 6px; /* Rounded corners for a modern look */\n"
"    padding: 4px 8px; /* Padding for spacing */\n"
"    font-size: 14px; /* Font size */\n"
"    text-align:center;\n"
"}")
        self.nom_arbre_creation.setText("")
        self.nom_arbre_creation.setObjectName("nom_arbre_creation")
        self.nom_arbre_creation_label = QtWidgets.QLabel(Dialog)
        self.nom_arbre_creation_label.setGeometry(QtCore.QRect(90, 80, 243, 37))
        self.nom_arbre_creation_label.setStyleSheet("font-size: 14px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.nom_arbre_creation_label.setObjectName("nom_arbre_creation_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Creation Premier Noeud"))
        self.taille_arbre_label_2.setText(_translate("Dialog", "Creation Premier Noeud"))
        self.confirm.setText(_translate("Dialog", "Confirmer"))
        self.nom_noeud_creation_label.setText(_translate("Dialog", "NOM noeud : "))
        self.nom_arbre_creation_label.setText(_translate("Dialog", "NOM arbre : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Premier_Noeud_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
