# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_compra.ui'
#
# Created: Sat Jul 12 20:51:25 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Nueva_Compra(object):
    def setupUi(self, Nueva_Compra):
        Nueva_Compra.setObjectName("Nueva_Compra")
        Nueva_Compra.resize(546, 493)
        self.btn_agregar_producto = QtGui.QPushButton(Nueva_Compra)
        self.btn_agregar_producto.setGeometry(QtCore.QRect(390, 370, 141, 27))
        self.btn_agregar_producto.setObjectName("btn_agregar_producto")
        self.label = QtGui.QLabel(Nueva_Compra)
        self.label.setGeometry(QtCore.QRect(30, 120, 101, 17))
        self.label.setObjectName("label")
        self.table_productos = QtGui.QTableView(Nueva_Compra)
        self.table_productos.setGeometry(QtCore.QRect(20, 140, 511, 221))
        self.table_productos.setObjectName("table_productos")
        self.label_6 = QtGui.QLabel(Nueva_Compra)
        self.label_6.setGeometry(QtCore.QRect(30, 370, 101, 17))
        self.label_6.setObjectName("label_6")
        self.lbl_total = QtGui.QLabel(Nueva_Compra)
        self.lbl_total.setGeometry(QtCore.QRect(140, 370, 66, 17))
        self.lbl_total.setObjectName("lbl_total")
        self.btn_guardar = QtGui.QPushButton(Nueva_Compra)
        self.btn_guardar.setGeometry(QtCore.QRect(20, 450, 98, 27))
        self.btn_guardar.setObjectName("btn_guardar")
        self.btn_cancelar = QtGui.QPushButton(Nueva_Compra)
        self.btn_cancelar.setGeometry(QtCore.QRect(120, 450, 98, 27))
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.widget = QtGui.QWidget(Nueva_Compra)
        self.widget.setGeometry(QtCore.QRect(20, 10, 501, 71))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.le_fecha = QtGui.QLineEdit(self.widget)
        self.le_fecha.setObjectName("le_fecha")
        self.horizontalLayout.addWidget(self.le_fecha)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.le_proveedor = QtGui.QLineEdit(self.widget)
        self.le_proveedor.setObjectName("le_proveedor")
        self.horizontalLayout.addWidget(self.le_proveedor)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.le_factura = QtGui.QLineEdit(self.widget)
        self.le_factura.setObjectName("le_factura")
        self.horizontalLayout_2.addWidget(self.le_factura)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.le_descripcion = QtGui.QLineEdit(self.widget)
        self.le_descripcion.setObjectName("le_descripcion")
        self.horizontalLayout_2.addWidget(self.le_descripcion)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Nueva_Compra)
        QtCore.QMetaObject.connectSlotsByName(Nueva_Compra)

    def retranslateUi(self, Nueva_Compra):
        Nueva_Compra.setWindowTitle(QtGui.QApplication.translate("Nueva_Compra", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar_producto.setText(QtGui.QApplication.translate("Nueva_Compra", "Agregar Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Nueva_Compra", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Nueva_Compra", "Total Compra $", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_total.setText(QtGui.QApplication.translate("Nueva_Compra", "0.", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_guardar.setText(QtGui.QApplication.translate("Nueva_Compra", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Nueva_Compra", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Nueva_Compra", "Fecha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Nueva_Compra", "Proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Nueva_Compra", "Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Nueva_Compra", "Descripción", None, QtGui.QApplication.UnicodeUTF8))

