# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detalle.ui'
#
# Created: Sat Jul 12 20:39:58 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(241, 136)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 66, 17))
        self.label_2.setObjectName("label_2")
        self.le_precio = QtGui.QLineEdit(Dialog)
        self.le_precio.setGeometry(QtCore.QRect(120, 20, 113, 27))
        self.le_precio.setObjectName("le_precio")
        self.le_cantidad = QtGui.QLineEdit(Dialog)
        self.le_cantidad.setGeometry(QtCore.QRect(120, 50, 113, 27))
        self.le_cantidad.setObjectName("le_cantidad")
        self.btn_aceptar = QtGui.QPushButton(Dialog)
        self.btn_aceptar.setGeometry(QtCore.QRect(130, 90, 98, 27))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.btn_cancelar = QtGui.QPushButton(Dialog)
        self.btn_cancelar.setGeometry(QtCore.QRect(20, 90, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Precio Unitario", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

