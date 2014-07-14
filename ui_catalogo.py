# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catalogo.ui'
#
# Created: Sun Jul 13 13:55:21 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Productos(object):
    def setupUi(self, Productos):
        Productos.setObjectName("Productos")
        Productos.resize(751, 562)
        self.gridLayout = QtGui.QGridLayout(Productos)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_productos = QtGui.QTableView(Productos)
        self.table_productos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_productos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_productos.setObjectName("table_productos")
        self.verticalLayout.addWidget(self.table_productos)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancelar = QtGui.QPushButton(Productos)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout.addWidget(self.btn_cancelar)
        self.btn_detalle = QtGui.QPushButton(Productos)
        self.btn_detalle.setObjectName("btn_detalle")
        self.horizontalLayout.addWidget(self.btn_detalle)
        self.btn_finalizar = QtGui.QPushButton(Productos)
        self.btn_finalizar.setObjectName("btn_finalizar")
        self.horizontalLayout.addWidget(self.btn_finalizar)
        spacerItem = QtGui.QSpacerItem(148, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_nuevo = QtGui.QPushButton(Productos)
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.horizontalLayout.addWidget(self.btn_nuevo)
        self.btn_agregar = QtGui.QPushButton(Productos)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Productos)
        QtCore.QMetaObject.connectSlotsByName(Productos)
        Productos.setTabOrder(self.btn_cancelar, self.btn_detalle)
        Productos.setTabOrder(self.btn_detalle, self.btn_finalizar)
        Productos.setTabOrder(self.btn_finalizar, self.btn_nuevo)
        Productos.setTabOrder(self.btn_nuevo, self.btn_agregar)
        Productos.setTabOrder(self.btn_agregar, self.table_productos)

    def retranslateUi(self, Productos):
        Productos.setWindowTitle(QtGui.QApplication.translate("Productos", "Agregar Productos a su nueva Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Productos", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_detalle.setText(QtGui.QApplication.translate("Productos", "Ver Detalle", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_finalizar.setText(QtGui.QApplication.translate("Productos", "Finalizar Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevo.setText(QtGui.QApplication.translate("Productos", "Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Productos", "Agregar", None, QtGui.QApplication.UnicodeUTF8))

