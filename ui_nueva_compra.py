# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nueva_compra.ui'
#
# Created: Sun Jul 13 00:43:19 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 283)
        self.btn_ingresar = QtGui.QPushButton(Dialog)
        self.btn_ingresar.setGeometry(QtCore.QRect(210, 230, 98, 27))
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.btn_cancelar = QtGui.QPushButton(Dialog)
        self.btn_cancelar.setGeometry(QtCore.QRect(100, 230, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_fecha = QtGui.QLineEdit(self.layoutWidget)
        self.le_fecha.setObjectName("le_fecha")
        self.gridLayout.addWidget(self.le_fecha, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.le_proveedor = QtGui.QLineEdit(self.layoutWidget)
        self.le_proveedor.setObjectName("le_proveedor")
        self.gridLayout.addWidget(self.le_proveedor, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_factura = QtGui.QLineEdit(self.layoutWidget)
        self.le_factura.setObjectName("le_factura")
        self.gridLayout.addWidget(self.le_factura, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.le_descripcion = QtGui.QLineEdit(self.layoutWidget)
        self.le_descripcion.setObjectName("le_descripcion")
        self.gridLayout.addWidget(self.le_descripcion, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Nueva Compra", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "N° Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Descripción", None, QtGui.QApplication.UnicodeUTF8))

