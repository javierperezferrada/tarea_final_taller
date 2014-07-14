#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ui_compras import Ui_Dialog
import controller
from model import Compra
import view_edit_compra


class Form(QtGui.QDialog):
    table_columns = (
        (u"Fecha", 200),
        (u"Proveedor", 100),
        (u"N° Factura", 200),
        (u"Descripcion", 100))


    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.load_compras()
        self.set_signals()
        self.show()

    def load_compras(self):
        compras = Compra.all()
        rows = len(compras)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
        self.ui.table_compras.setModel(model)
        self.ui.table_compras.horizontalHeader().setResizeMode(
            0, self.ui.table_compras.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.table_compras.setColumnWidth(col, h[1])

        for i, data in enumerate(compras):
            row = [data[1], data[2], data[3], data[4]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index, field)
            #Parametros ocultos
            model.item(i).com = data
            model.item(i).pk = data[0]

    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.ui.btn_cancelar.clicked.connect(self.cancelar)
        self.ui.btn_editar.clicked.connect(self.editar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)

    def eliminar(self):
        model = self.ui.table_compras.model()
        index = self.ui.table_compras.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            id_compra = model.item(index.row()).pk

            c = Compra()
            c.id_compra = id_compra
            c.delete()
            self.load_compras()

    def editar(self):
        model = self.ui.table_compras.model()
        index = self.ui.table_compras.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            id_compra = model.item(index.row()).pk
            fecha = model.item(index.row()).com[1]
            prov = model.item(index.row()).com[2]
            fact = model.item(index.row()).com[3]
            desc = model.item(index.row()).com[4]
            form = view_edit_compra.Form(self, id_compra, fecha, prov, fact, desc)
            form.rejected.connect(self.load_compras)
            form.exec_()
            self.load_compras()

    def cancelar(self):
        self.reject()