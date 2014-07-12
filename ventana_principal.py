# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana_principal.ui'
#
# Created: Fri Jul 11 18:20:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!
import sys
from model import Producto
from PySide import QtCore, QtGui


class Ui_MainWindow(object):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtbuscar = QtGui.QLineEdit(self.centralwidget)
        self.txtbuscar.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.txtbuscar)
        self.btn_buscar = QtGui.QPushButton(self.centralwidget)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabla_productos = QtGui.QTableWidget(self.centralwidget)
        self.tabla_productos.setObjectName("tabla de productos")
        self.verticalLayout_2.addWidget(self.tabla_productos)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_nuevacompra = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.btn_nuevacompra.setFont(font)
        self.btn_nuevacompra.setObjectName("btn_nuevacompra")
        self.horizontalLayout_4.addWidget(self.btn_nuevacompra)
        self.btn_compras = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.btn_compras.setFont(font)
        self.btn_compras.setObjectName("btn_compras")
        self.horizontalLayout_4.addWidget(self.btn_compras)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_eliminar = QtGui.QPushButton(self.centralwidget)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_3.addWidget(self.btn_eliminar)
        spacerItem4 = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.btn_editar = QtGui.QPushButton(self.centralwidget)
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout_3.addWidget(self.btn_editar)
        spacerItem5 = QtGui.QSpacerItem(40, 20,
        QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.btn_agregar = QtGui.QPushButton(self.centralwidget)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout_3.addWidget(self.btn_agregar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tabla_productos.setColumnCount(5)
        self.tabla_productos.setColumnWidth(0, 80)
        self.tabla_productos.setColumnWidth(1, 120)
        self.tabla_productos.setColumnWidth(2, 220)
        self.tabla_productos.setColumnWidth(3, 210)
        self.tabla_productos.setColumnWidth(4, 150)
        self.tabla_productos.setHorizontalHeaderLabels(['Codigo',
        'Nombre', 'Descripcion', 'Marca', 'Color'])
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.cargar_tabla(Producto.all())
        self.btn_buscar.clicked.connect(self.buscar_clicked)
        self.btn_eliminar.clicked.connect(self.eliminar_clicked)
        self.btn_editar.clicked.connect(self.editar_clicked)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow",
        "Tabla con productos", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("MainWindow",
        "               Buscar                 ", None,
        QtGui.QApplication.UnicodeUTF8))
        self.btn_nuevacompra.setText(QtGui.QApplication.translate("MainWindow",
        "Nueva compra", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_compras.setText(QtGui.QApplication.translate("MainWindow",
        "Compras", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("MainWindow",
        "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("MainWindow",
        "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("MainWindow",
        "Agregar", None, QtGui.QApplication.UnicodeUTF8))
###############################################################################

    def eliminar_clicked(self):
        index = self.tabla_productos.currentIndex()
        print index.row()
        if (index.row() != -1):
            self.tabla_productos.removeRow(index.row())
            ########################## IMPORTANTE #############################
            ################# NO ELIMINA DE LA BASE DE DATOS ##################
        else:
            print "Aaaaaaaaaaaaaaaaaaaaaaa"
            QtGui.QMessageBox.question(None, 'Error!!',
            'No has seleccionado fila a eliminar')

    def editar_clicked(self):
        index = self.tabla_productos.currentIndex()
        print index.row()
        if (index.row() != -1):
            None
            ################### Falta editar en nueva ventana #################
            ########################## IMPORTANTE #############################
            ################# NO ELIMINA DE LA BASE DE DATOS ##################
        else:
            print "Aaaaaaaaaaaaaaaaaaaaaaa"
            QtGui.QMessageBox.question(None, 'Error!!',
            'No has seleccionado fila a editar')

    def agregar_clicked(self):
        None

    def nueva_compra(self):
        None

    def ver_compras(self):
        None

    def buscar_clicked(self):
        temptext = str(self.txtbuscar.text().strip())
        # Para quitar los espacios
        print temptext
        print type(temptext)
        if temptext == "":  # el qlineedit esta vacio
            self.cargar_tabla(Producto.all())
        else:  # el qlineedit contiene un string
            self.cargar_tabla(Producto.all(temptext))
            print "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

    def cargar_tabla(self, consulta):
        txtcellcod = []
        txtcellnom = []
        txtcelldes = []
        txtcellmar = []
        txtcellcol = []
        c = 0  # segundo contador para colocar daos
        f = 0  # primer contador para recopilar numero de filas necesarias
        for pro in consulta:
            txtcellcod.append(QtGui.QTableWidgetItem())
            txtcellnom.append(QtGui.QTableWidgetItem())
            txtcelldes.append(QtGui.QTableWidgetItem())
            txtcellmar.append(QtGui.QTableWidgetItem())
            txtcellcol.append(QtGui.QTableWidgetItem())
            txtcellcod[f].setText(pro[1])
            txtcellnom[f].setText(pro[2])
            txtcelldes[f].setText(pro[3])
            txtcellmar[f].setText(pro[4])
            txtcellcol[f].setText(pro[5])
            f = f + 1
        self.tabla_productos.setRowCount(f)
        for pro in consulta:
            self.tabla_productos.setItem(c, 0, txtcellcod[c])
            self.tabla_productos.setItem(c, 1, txtcellnom[c])
            self.tabla_productos.setItem(c, 2, txtcelldes[c])
            self.tabla_productos.setItem(c, 3, txtcellmar[c])
            self.tabla_productos.setItem(c, 4, txtcellcol[c])
            c = c + 1


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())