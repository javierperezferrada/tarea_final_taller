# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vent_ingreso.ui'
#
<<<<<<< HEAD
# Created: Fri Jul 11 15:58:49 2014
=======
# Created: Fri Jul 11 17:02:08 2014
>>>>>>> javier
#      by: pyside-uic 0.2.13 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 327)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 401, 281))
        self.widget.setMaximumSize(QtCore.QSize(401, 16777215))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
<<<<<<< HEAD
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
=======
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.le_codigo = QtGui.QLineEdit(self.widget)
        self.le_codigo.setObjectName("le_codigo")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.le_codigo)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.le_nombre = QtGui.QLineEdit(self.widget)
        self.le_nombre.setObjectName("le_nombre")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.le_nombre)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.le_descripcion = QtGui.QLineEdit(self.widget)
        self.le_descripcion.setObjectName("le_descripcion")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.le_descripcion)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.le_marca = QtGui.QLineEdit(self.widget)
        self.le_marca.setObjectName("le_marca")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.le_marca)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.le_color = QtGui.QLineEdit(self.widget)
        self.le_color.setObjectName("le_color")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.le_color)
        self.btn_ingresar = QtGui.QPushButton(self.widget)
        self.btn_ingresar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btn_ingresar.setObjectName("btn_ingresar")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.btn_ingresar)
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label)
>>>>>>> javier
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Codigo     *", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Nombre  *", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Descripción", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ingresar.setText(QtGui.QApplication.translate("MainWindow", "INGRESAR", None, QtGui.QApplication.UnicodeUTF8))
<<<<<<< HEAD
=======
        self.label.setText(QtGui.QApplication.translate("MainWindow", "*Campos Obligatorios", None, QtGui.QApplication.UnicodeUTF8))
>>>>>>> javier

