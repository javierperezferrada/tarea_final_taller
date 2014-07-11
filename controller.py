#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ahora que tenemos un modelo el controlador cumple el rol de ser una capa
intermedia entre la Vista y el modelo.
Su finalidad es validar los datos de entrada que envía la vista y decidir
que información enviar a ésta.
"""

from model import Producto, Compra


def productos():
    return Producto.all()


def compras():
    return Compra.all()


def crear_producto(codigo, nombre, descripcion, marca, color):
    """
    Método que crea un producto. Falta validar
    que toda la información es correcta
    """
    nuevo = Producto()
    nuevo.codigo = codigo
    # Aquí podrían haber validaciones para el codigo
    nuevo.nombre = nombre
    nuevo.descripcion = descripcion
    nuevo.marca = marca
    nuevo.color = color
    nuevo.save()

if __name__ == "__main__":
    pass
