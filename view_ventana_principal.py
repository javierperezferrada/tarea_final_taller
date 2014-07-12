#!/usr/bin/python
# ­*­ coding: utf­8 ­*­
import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
from ventana_principal import Ui_MainWindow
import controller
from model import Producto

class VentanaPrincipal(QtGui.QMainWindow):
    table_columns = (
        (u"Codigo", 200),
        (u"Nombre", 100),
        (u"Descripción", 200),
        (u"Marca", 100),
        (u"Color", 75))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_productos()
        self.set_signals()
        self.show()

    def set_signals(self):
        #en esta funcion se definen todos los tratamientos de señales.
        self.ui.btn_editar.clicked.connect(self.editar)
        self.ui.btn_agregar.clicked.connect(self.agregar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)
        self.ui.table_productos.clicked.connect(self.select)

    def load_productos(self):
        # Método que carga la tabla productos en la Ventana.
        productos = Producto.all()
        rows = len(productos)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
        self.ui.table_productos.setModel(model)
        self.ui.table_productos.horizontalHeader().setResizeMode(
            0, self.ui.table_productos.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            model.setHeaderData(col, QtCore.Qt.Horizontal, h[0])
            self.ui.table_productos.setColumnWidth(col, h[1])

        for i, data in enumerate(productos):
            row = [data[1], data[2], data[3], data[4], data[5]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore.QModelIndex())
                model.setData(index, field)
            #Parametros ocultos
            model.item(i).mov = data
            model.item(i).pk = data[0]

    def editar():
        None


    def eliminar():
        None


    def agregar():
        None


    def select():
        None




if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = VentanaPrincipal()
    sys.exit(app.exec_())