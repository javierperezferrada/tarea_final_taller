# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Editar_producto.ui'
#
# Created: Sat Jul 12 12:31:08 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Editar_producto_win(object):
    def __init__(self, parent=None, Id=None,
        codigo=None, nombre=None, descripcion=None, marca=None,
        color=None):
        self.setupUi(self)
        self.Id = Id
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.color = color
        self.marca = marca
        self.qline_codigo.setText(codigo)
        self.qline_nombre.setText(nombre)
        self.qline_descripcion.setText(descripcion)
        self.qline_marca.setText(marca)
        self.qline_color.setText(color)
        self.btn_cancelar.clicked.connect(self.cancelar_clicked)
        self.btn_aceptar.clicked.connect(self.aceptar_clicked)

    def setupUi(self, Editar_producto_win):
        Editar_producto_win.setObjectName("Editar_producto_win")
        Editar_producto_win.resize(363, 294)
        self.centralwidget = QtGui.QWidget(Editar_producto_win)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.qline_codigo = QtGui.QLineEdit(self.centralwidget)
        self.qline_codigo.setObjectName("qline_codigo")
        self.horizontalLayout.addWidget(self.qline_codigo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.qline_nombre = QtGui.QLineEdit(self.centralwidget)
        self.qline_nombre.setObjectName("qline_nombre")
        self.horizontalLayout_2.addWidget(self.qline_nombre)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.qline_descripcion = QtGui.QLineEdit(self.centralwidget)
        self.qline_descripcion.setObjectName("qline_descripcion")
        self.horizontalLayout_3.addWidget(self.qline_descripcion)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.qline_marca = QtGui.QLineEdit(self.centralwidget)
        self.qline_marca.setObjectName("qline_marca")
        self.horizontalLayout_4.addWidget(self.qline_marca)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.qline_color = QtGui.QLineEdit(self.centralwidget)
        self.qline_color.setObjectName("qline_color")
        self.horizontalLayout_5.addWidget(self.qline_color)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40,
        QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_cancelar = QtGui.QPushButton(self.centralwidget)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.horizontalLayout_6.addWidget(self.btn_cancelar)
        spacerItem1 = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.btn_aceptar = QtGui.QPushButton(self.centralwidget)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.horizontalLayout_6.addWidget(self.btn_aceptar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        Editar_producto_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Editar_producto_win)
        QtCore.QMetaObject.connectSlotsByName(Editar_producto_win)

    def retranslateUi(self, Editar_producto_win):
        Editar_producto_win.setWindowTitle(QtGui.QApplication.translate(
            "Editar_producto_win",
            "Editar Producto", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Codigo:", None,
            QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Nombre:", None,
            QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Descripcion:", None,
            QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Marca:", None,
            QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Color:", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Cancelar", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate(
            "Editar_producto_win", "Aceptar", None,
            QtGui.QApplication.UnicodeUTF8))

    def aceptar_clicked(self):
        None
        ###################### MODIFICAR ACAAA ###################

    def cancelar_clicked(self):
        self.reject()

