#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_detalle import Ui_Dialog
import controller


class Form(QtGui.QDialog):
    def __init__(self, parent=None, id_compra=None, id_producto=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.guardar_id(id_compra, id_producto)
        self.set_signals()
        self.show()

    def guardar_id(self, id_compra, id_producto):
        self.id_compra = id_compra
        self.id_producto = id_producto

    def set_signals(self):
        self.ui.btn_aceptar.clicked.connect(self.aceptar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def aceptar(self):
        precio = self.ui.le_precio.text()
        cantidad = self.ui.le_cantidad.text()
        if controller.crear_compra_has_producto(self.id_compra, self.id_producto, precio, cantidad):
            self.reject()

    def cancelar(self):
        self.reject()