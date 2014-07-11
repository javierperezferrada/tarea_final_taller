# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vent_ingreso.ui'
#
# Created: Fri Jul 11 15:58:49 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 361, 271))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.le_codigo = QtGui.QLineEdit(self.widget)
        self.le_codigo.setObjectName("le_codigo")
        self.gridLayout.addWidget(self.le_codigo, 0, 1, 1, 1)
        self.le_nombre = QtGui.QLineEdit(self.widget)
        self.le_nombre.setObjectName("le_nombre")
        self.gridLayout.addWidget(self.le_nombre, 2, 1, 1, 1)
        self.le_descripcion = QtGui.QLineEdit(self.widget)
        self.le_descripcion.setObjectName("le_descripcion")
        self.gridLayout.addWidget(self.le_descripcion, 3, 1, 1, 1)
        self.le_marca = QtGui.QLineEdit(self.widget)
        self.le_marca.setObjectName("le_marca")
        self.gridLayout.addWidget(self.le_marca, 4, 1, 1, 1)
        self.le_color = QtGui.QLineEdit(self.widget)
        self.le_color.setObjectName("le_color")
        self.gridLayout.addWidget(self.le_color, 5, 1, 1, 1)
        self.btn_ingresar = QtGui.QPushButton(self.widget)
        self.btn_ingresar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.gridLayout.addWidget(self.btn_ingresar, 6, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Codigo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Nombre", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("MainWindow", "INGRESAR", None, QtGui.QApplication.UnicodeUTF8))

