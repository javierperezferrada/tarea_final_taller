#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ahora que tenemos un modelo el controlador cumple el rol de ser una capa
intermedia entre la Vista y el modelo.
Su finalidad es validar los datos de entrada que envía la vista y decidir
que información enviar a ésta.
"""
from PySide import QtGui
from model import Producto, Compra



def productos():
    return Producto.all()


def compras():
    return Compra.all()


def crear_producto(codigo, nombre, descripcion, marca, color):
    """
    Método que crea un producto.
    """
    nuevo = Producto()
    if codigo == "" or nombre == "":  # Valida los campos obligatorios.
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Debe ingresar los campos obligatorios.")
        msgBox.exec_()
        return False

    else:
        nuevo.codigo = codigo
        nuevo.nombre = nombre
        nuevo.descripcion = descripcion
        nuevo.marca = marca
        nuevo.color = color
        nuevo.save()
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Producto ingresado satisfactoriamente.")
        msgBox.exec_()
        return True


def editar_producto(id_producto, codigo, nombre, descripcion, marca, color):
    """
    Método que edita un producto.
    """
    nuevo = Producto()
    if codigo == "" or nombre == "":  # Valida los campos obligatorios.
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Debe ingresar los campos obligatorios.")
        msgBox.exec_()
        return False

    else:
        nuevo.id_producto = id_producto
        nuevo.codigo = codigo
        nuevo.nombre = nombre
        nuevo.descripcion = descripcion
        nuevo.marca = marca
        nuevo.color = color
        nuevo.save()
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Producto editado satisfactoriamente.")
        msgBox.exec_()
        return True



if __name__ == "__main__":
    pass
