#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_dialog_ingreso import Ui_Dialog
import controller


class Form(QtGui.QDialog):
    def __init__(self, parent=None,id_p=None, cod=None, nom=None, des=None,
            mar=None, col=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.set_signals()
        self.cargar(cod, nom, des, mar, col)
        self.pk = id_p
        self.show()

    def cargar(self, cod, nom,des, mar, col):
        self.cod = cod
        self.nom = nom
        self.des = des
        self.mar = mar
        self.col = col
        self.ui.le_codigo.setText(cod)
        self.ui.le_nombre.setText(nom)
        self.ui.le_descripcion.setText(des)
        self.ui.le_marca.setText(mar)
        self.ui.le_color.setText(col)



    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.ui.btn_aceptar.clicked.connect(self.ingresar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def ingresar(self):
        cod = self.ui.le_codigo.text()
        nom = self.ui.le_nombre.text()
        des = self.ui.le_descripcion.text()
        mar = self.ui.le_marca.text()
        col = self.ui.le_color.text()
        if controller.editar_producto(self.pk, cod, nom, des, mar, col):
            self.reject()
