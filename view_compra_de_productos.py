#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_compra_de_productos import Ui_Compra_de_productos
from model import Producto


class Compradeproductos(QtGui.QDialog):
    table_columns_pro = (
        (u"Codigo", 200),
        (u"Nombre", 100),
        (u"Descripción", 200),
        (u"Marca", 100),
        (u"Color", 75))

    table_columns_venta = (
        (u"Codigo", 200),
        (u"Nombre", 100),
        (u"Marca", 100),
        (u"Cantidad", 100),
        (u"Precio unitario", 100),
        (u"Total", 150))

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Compra_de_productos()
        self.ui.setupUi(self)
        self.load_productos()
        self.load_tabla_venta()
        self.set_signals()
        self.show()

    def load_productos(self):
        productos = Producto.all()
        rows = len(productos)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns_pro))
        self.ui.tabla_buscar.setModel(model)
        self.ui.tabla_buscar.horizontalHeader().setResizeMode(
            0, self.ui.tabla_buscar.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns_pro):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.tabla_buscar.setColumnWidth(col, h[1])

        for i, data in enumerate(productos):
            row = [data[1], data[2], data[3], data[4], data[5]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index, field)
            #Parametros ocultos
            model.item(i).mov = data
            model.item(i).pk = data[0]

    def load_tabla_venta(self):
        productos = Producto.all()
        rows = len(productos)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns_venta))
        self.ui.tabla_compra.setModel(model)
        self.ui.tabla_compra.horizontalHeader().setResizeMode(
            0, self.ui.tabla_compra.horizontalHeader().Stretch)

    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.ui.btn_buscar.clicked.connect(self.buscar_pro)
        self.ui.btn_agrega_carro.clicked.connect(self.agregar_al_carro)
        self.ui.btn_editar.clicked.connect(self.editar_del_carro)
        self.ui.btn_eliminar.clicked.connect(self.eliminar_del_carro)
        self.ui.btn_comprar.clicked.connect(self.comprar_ya)
        self.ui.btn_cancelar_compra.clicked.connect(self.cancelar_compra)
        self.ui.table_productos.clicked.connect(self.select)

    def buscar_pro():
        None

    def agregar_al_carro():
        None

    def editar_del_carro():
        None

    def eliminar_del_carro():
        None

    def comprar_ya():
        None

    def cancelar_compra():
        None

    def select():
        None

