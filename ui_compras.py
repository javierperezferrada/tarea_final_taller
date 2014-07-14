# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compras.ui'
#
# Created: Sun Jul 13 13:46:50 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(665, 445)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_compras = QtGui.QTableView(Dialog)
        self.table_compras.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_compras.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_compras.setObjectName("table_compras")
        self.gridLayout_2.addWidget(self.table_compras, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_eliminar = QtGui.QPushButton(Dialog)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout.addWidget(self.btn_eliminar, 0, 2, 1, 1)
        self.btn_cancelar = QtGui.QPushButton(Dialog)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.gridLayout.addWidget(self.btn_cancelar, 0, 3, 1, 1)
        self.btn_editar = QtGui.QPushButton(Dialog)
        self.btn_editar.setObjectName("btn_editar")
        self.gridLayout.addWidget(self.btn_editar, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btn_cancelar, self.btn_editar)
        Dialog.setTabOrder(self.btn_editar, self.btn_eliminar)
        Dialog.setTabOrder(self.btn_eliminar, self.table_compras)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Compras", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Dialog", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))

