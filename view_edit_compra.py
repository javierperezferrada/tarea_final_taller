#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_nueva_compra import Ui_Dialog
import controller

class Form(QtGui.QDialog):
    def __init__(self, parent=None,id_c=None, fecha=None, prov=None, fact=None,
            desc=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.set_signals()
        self.cargar(fecha, prov, fact, desc)
        self.pk = id_c
        self.show()

    def cargar(self, fecha, prov,fact, desc):
        self.fecha = fecha
        self.prov = prov
        self.fact = fact
        self.desc = desc
        self.ui.le_fecha.setText(fecha)
        self.ui.le_proveedor.setText(prov)
        self.ui.le_factura.setText(str(fact))
        self.ui.le_descripcion.setText(desc)




    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.ui.btn_ingresar.clicked.connect(self.ingresar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def ingresar(self):
        fecha = self.ui.le_fecha.text()
        prov = self.ui.le_proveedor.text()
        fact = self.ui.le_factura.text()
        desc = self.ui.le_descripcion.text()

        if controller.editar_compra(self.pk, fecha, prov, fact, desc):
            self.reject()

