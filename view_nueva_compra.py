#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_nueva_compra import Ui_Dialog
import controller
import view_catalogo

class Form(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.set_signals()
        self.show()

    def set_signals(self):
        self.ui.btn_ingresar.clicked.connect(self.ingresar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def ingresar(self):
        fecha = self.ui.le_fecha.text()
        proveedor = self.ui.le_proveedor.text()
        numero_factura = self.ui.le_factura.text()
        descripcion = self.ui.le_descripcion.text()
        if controller.crear_compra(fecha, proveedor, numero_factura, descripcion):
            id_compra = controller.get_last_compra()
            form = view_catalogo.Form(self, id_compra[0])
            form.rejected.connect(self.reject)
            form.exec_()
