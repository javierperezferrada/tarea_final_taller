# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compra_realizada.ui'
#
# Created: Mon Jul 14 11:35:53 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(654, 464)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_productos = QtGui.QTableView(Dialog)
        self.table_productos.setObjectName("table_productos")
        self.verticalLayout.addWidget(self.table_productos)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_agregar = QtGui.QPushButton(Dialog)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btn_agregar, self.table_productos)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Nueva Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Dialog", "Volver", None, QtGui.QApplication.UnicodeUTF8))

