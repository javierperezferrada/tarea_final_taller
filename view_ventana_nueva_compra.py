#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_ventana_compra import Ui_Nueva_Compra
import view_catalogo
import controller

class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Nueva_Compra()
        self.ui.setupUi(self)
        self.set_signals()
        self.show()

    def set_signals(self):
        self.ui.btn_agregar_producto.clicked.connect(self.mostrar_productos)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def mostrar_productos(self):
        form = view_catalogo.Form()
        form.rejected.connect(self.load_productos)
        form.exec_()

    def cancelar(self):
        self.reject()

