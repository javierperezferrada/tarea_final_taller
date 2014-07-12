#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from Registro_de_compras.ui import Ui_MainWindow
from model import Producto


class view_registro_de_compras(QtGui.QDialog):
    table_columns_pro = (
        (u"Codigo", 150),
        (u"Fecha", 100),
        (u"Proveedor", 100),
        (u"N° Factura", 100),
        (u"Descripcion", 200))

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_compras()
        self.set_signals()
        self.show()

    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.ui.btn_buscar.clicked.connect(self.buscar_compra)
        self.ui.btn_editar.clicked.connect(self.editar_compra)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_compra)
        self.ui.btn_salir.clicked.connect(self.salir)
        self.ui.tabla_de_compras.clicked.connect(self.select)

    def buscar_compra():
        None

    def editar_compra():
        None

    def eliminar_compra():
        None

    def salir():
        None

    def select():
        None