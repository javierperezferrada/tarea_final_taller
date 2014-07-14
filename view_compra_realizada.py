#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_compra_realizada import Ui_Dialog
from model import Producto
import controller

class Form(QtGui.QDialog):
    def __init__(self, parent=None, id_compra=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.guardar_id(id_compra)
        self.set_signals()
        self.load_productos()
        self.show()

    table_columns = (
    (u"Codigo", 200),
    (u"Nombre", 100),
    (u"Descripción", 200),
    (u"Marca", 100),
    (u"Color", 75))

    def guardar_id(self, id_compra):
        self.id_compra = id_compra

    def set_signals(self):
        self.ui.btn_agregar.clicked.connect(self.agregar)

    def load_productos(self):
        # Método que carga los productos ingresados a la nueva compra.
        print self.id_compra
        productos = Producto.productos(self.id_compra)
        rows = len(productos)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
        self.ui.table_productos.setModel(model)
        self.ui.table_productos.horizontalHeader().setResizeMode(
            0, self.ui.table_productos.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.table_productos.setColumnWidth(col, h[1])

        for i, data in enumerate(productos):
            row = [data[1], data[2], data[3], data[4], data[5]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index, field)
            #Parametros ocultos
            model.item(i).prod = data
            model.item(i).pk = data[0]

    def agregar(self):
        self.reject()

