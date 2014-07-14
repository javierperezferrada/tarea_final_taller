#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ahora que tenemos un modelo el controlador cumple el rol de ser una capa
intermedia entre la Vista y el modelo.
Su finalidad es validar los datos de entrada que envía la vista y decidir
que información enviar a ésta.
"""
from PySide import QtGui
from model import Producto, Compra, Compra_has_Producto



def productos():
    return Producto.all()


def compras():
    return Compra.all()

def get_last_compra():
    c = Compra()
    id_compra = c.last_id()
    return id_compra


def crear_compra_has_producto(id_compra, id_producto, precio, cantidad):
        nuevo = Compra_has_Producto()
        nuevo.fk_id_compra = id_compra
        nuevo.fk_id_producto = id_producto
        nuevo.cantidad = cantidad
        nuevo.precio_unitario = precio
        nuevo.total = int(precio) * int(cantidad)
        nuevo.save()
        return True

def crear_compra(fecha, proveedor, factura, descripcion):
    # Metodo que crea una compra.
    nuevo = Compra()
    if fecha == "" or factura == "" or proveedor == "":  # Valida los campos obligatorios.
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Debe ingresar los campos obligatorios.")
        msgBox.exec_()
        return False

    else:
        nuevo.fecha = fecha
        nuevo.proveedor = proveedor
        nuevo.numero_factura = factura
        nuevo.descripcion = descripcion
        nuevo.save()
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Compra ingresado satisfactoriamente.")
        msgBox.exec_()
        return True

def editar_compra(id_compra, fecha, proveedor, factura, descripcion):
    """
    Método que edita una compra
    """
    nuevo = Compra()
    if fecha == "" or proveedor == "" or factura == "":  # Valida los campos obligatorios.
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Debe ingresar los campos obligatorios.")
        msgBox.exec_()
        return False

    else:
        nuevo.id_compra = id_compra
        nuevo.fecha = fecha
        nuevo.proveedor = proveedor
        nuevo.numero_factura = factura
        nuevo.descripcion = descripcion
        nuevo.save()
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Compra editada satisfactoriamente.")
        msgBox.exec_()
        return True

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
