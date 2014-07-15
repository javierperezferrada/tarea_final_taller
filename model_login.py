#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys #importacion necesaria para acceder a la librerias de Qt
from PySide import QtGui, QtCore
import sqlite3

def conectar():
    #crea la conexion a la base de datos
    con = sqlite3.connect('compras.db')
    con.row_factory = sqlite3.Row
    return con

def logines(usuario,contrasenia):
    #verifica la existencia del usuario
    con = conectar()
    c = con.cursor()
    query = "SELECT count(user) FROM usuarios WHERE user = ?"
    #con un contador verifico si existe el usuario
    try:
        resultado = c.execute(query, [usuario])
        cont = resultado.fetchall()
        print cont
    except sqlite3.Error as e:
        print "Error:", e.args[0]
    a = int(cont[0][0])
    if a > 0:
        query1 = "SELECT id_usuario FROM usuarios WHERE user = ?"
        try:
            resultad = c.execute(query1, [usuario])
            identi = resultad.fetchall()
            identi=int(identi[0][0])
            result = verifica(identi,contrasenia)
            print result
        except sqlite3.Error as e:
            print "Error:", e.args[0]
    else:
        # Error al ingresar usuario
        msgBox = QtGui.QMessageBox()
        msgBox.setText("No existe usuario")
        msgBox.exec_()
        result = False
    con.close()
    return result

def verifica(identi,contrasenia):
    #verifica contraseña
    con = conectar()
    c = con.cursor()
    #si existe usuario, verificamos contraseña
    query = "SELECT password FROM usuarios WHERE id_usuario = ?"
    try:
        resultado = c.execute(query, [identi])
        contras= resultado.fetchall()
    except sqlite3.Error as e:
        print "Error:", e.args[0]
    con.close()
    contra = contras[0][0]
    if contra == contrasenia:
        res = True
    else:
        #Error al ingresar contrasenia 
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Contrasenia Erronea")
        msgBox.exec_()
        res = False
    return res
