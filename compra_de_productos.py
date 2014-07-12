# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Compra_de_productos.ui'
#
# Created: Sat Jul 12 07:33:50 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui


class Ui_Compra_de_productos(object):

    def __init__(self):
        super(Ui_Compra_de_productos, self).__init__()

    def setupUi(self, Compra_de_productos):
        Compra_de_productos.setObjectName("Compra_de_productos")
        Compra_de_productos.resize(713, 593)
        self.centralwidget = QtGui.QWidget(Compra_de_productos)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.qline_buscar = QtGui.QLineEdit(self.centralwidget)
        self.qline_buscar.setObjectName("qline_buscar")
        self.horizontalLayout_5.addWidget(self.qline_buscar)
        self.btn_buscar = QtGui.QPushButton(self.centralwidget)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_5.addWidget(self.btn_buscar)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.tabla_buscar = QtGui.QTableWidget(self.centralwidget)
        self.tabla_buscar.setObjectName("tabla_buscar")
        self.tabla_buscar.setColumnCount(0)
        self.tabla_buscar.setRowCount(0)
        self.verticalLayout_7.addWidget(self.tabla_buscar)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
        QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_agrega_carro = QtGui.QPushButton(self.centralwidget)
        self.btn_agrega_carro.setObjectName("btn_agrega_carro")
        self.horizontalLayout_4.addWidget(self.btn_agrega_carro)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
        QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum,
        QtGui.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabla_compra = QtGui.QTableWidget(self.centralwidget)
        self.tabla_compra.setObjectName("tabla_compra")
        self.tabla_compra.setColumnCount(0)
        self.tabla_compra.setRowCount(0)
        self.horizontalLayout_3.addWidget(self.tabla_compra)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_editar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
        QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy)
        self.btn_editar.setObjectName("btn_editar")
        self.verticalLayout_4.addWidget(self.btn_editar)
        self.btn_eliminar = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum,
        QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.btn_eliminar.sizePolicy().hasHeightForWidth())
        self.btn_eliminar.setSizePolicy(sizePolicy)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.verticalLayout_4.addWidget(self.btn_eliminar)
        spacerItem3 = QtGui.QSpacerItem(20, 40,
        QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.total = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
        QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.total.sizePolicy().hasHeightForWidth())
        self.total.setSizePolicy(sizePolicy)
        self.total.setObjectName("total")
        self.verticalLayout_4.addWidget(self.total)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cancelar_compra = QtGui.QPushButton(self.centralwidget)
        self.btn_cancelar_compra.setObjectName("btn_cancelar_compra")
        self.horizontalLayout_2.addWidget(self.btn_cancelar_compra)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
        QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_comprar = QtGui.QPushButton(self.centralwidget)
        self.btn_comprar.setObjectName("btn_comprar")
        self.horizontalLayout_2.addWidget(self.btn_comprar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        Compra_de_productos.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Compra_de_productos)
        self.statusbar.setObjectName("statusbar")
        Compra_de_productos.setStatusBar(self.statusbar)

        self.retranslateUi(Compra_de_productos)
        QtCore.QMetaObject.connectSlotsByName(Compra_de_productos)

    def retranslateUi(self, Compra_de_productos):
        Compra_de_productos.setWindowTitle(QtGui.QApplication.translate(
            "Compra_de_productos", "Compra de productos", None,
            QtGui.QApplication.UnicodeUTF8))
        self.qline_buscar.setPlaceholderText(QtGui.QApplication.translate(
            "Compra_de_productos",
            "Ingresa el codigo o nombre del producto a buscar",
            None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate(
            "Compra_de_productos", "Buscar", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_agrega_carro.setText(QtGui.QApplication.translate(
            "Compra_de_productos", "Agregar al carro", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate(
            "Compra_de_productos", "  Editar producto ", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate(
            "Compra_de_productos", "Eliminar del carro", None,
            QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Compra_de_productos",
        "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.total.setPlaceholderText(QtGui.QApplication.translate(
            "Compra_de_productos", "Total de compra", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar_compra.setText(QtGui.QApplication.translate(
            "Compra_de_productos", "Cancelar compra", None,
            QtGui.QApplication.UnicodeUTF8))
        self.btn_comprar.setText(QtGui.QApplication.translate(
            "Compra_de_productos", "Guardar compra", None,
            QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_Compra_de_productos()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())