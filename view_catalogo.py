#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_catalogo import Ui_Productos
from model import Producto, Compra
import controller
import view_detalle
import view_vent_ingreso_producto
import view_compra_realizada

class Form(QtGui.QDialog):
    def __init__(self, parent=None, id_compra=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Productos()
        self.ui.setupUi(self)
        self.load_productos()
        self.guardar_id(id_compra)
        self.set_signals()
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
        self.ui.btn_cancelar.clicked.connect(self.cancelar)
        self.ui.btn_nuevo.clicked.connect(self.nuevo)
        self.ui.btn_finalizar.clicked.connect(self.finalizar)
        self.ui.btn_detalle.clicked.connect(self.detalle)

    def detalle(self):
        form = view_compra_realizada.Form(self, self.id_compra)
        form.rejected.connect(self.load_productos)
        form.exec_()

    def finalizar(self):
        self.reject()

    def nuevo(self):
        form = view_vent_ingreso_producto.Form()
        form.rejected.connect(self.load_productos)
        form.exec_()

    def cancelar(self):
        self.reject()

    def agregar(self):
        model = self.ui.table_productos.model()
        index = self.ui.table_productos.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            id_producto = model.item(index.row()).pk
            cod = model.item(index.row()).prod[1]
            nom = model.item(index.row()).prod[2]
            des = model.item(index.row()).prod[3]
            mar = model.item(index.row()).prod[4]
            col = model.item(index.row()).prod[5]
            form = view_detalle.Form(self, self.id_compra, id_producto)
            form.rejected.connect(self.load_productos)
            form.exec_()
            self.load_productos()


    def load_productos(self):
        # Método que carga la tabla productos en la Ventana.
        productos = Producto.all()
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
