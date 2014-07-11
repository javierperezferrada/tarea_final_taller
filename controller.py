#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Ahora que tenemos un modelo el controlador cumple el rol de ser una capa
intermedia entre la Vista y el modelo.
Su finalidad es validar los datos de entrada que envía la vista y decidir
que información enviar a ésta.
"""

from model import Curso, Alumno


def cursos():
    return Curso.all()


def alumnos():
    return Alumno.all()


def crear_curso(nombre, codigo, semestre, area):
    """
    Método que crea un curso. Lo correcto sería validar
    que toda la información es correcta
    Ej:
        - Semestre puede ser 1 o 2
        - Los códigos podrían tener un formato predefinido
        - Etc
    """
    nuevo = Curso()
    nuevo.nombre = nombre
    # Aquí podrían haber validaciones para el codigo
    nuevo.codigo = codigo
    nuevo.semetre = semestre
    nuevo.area = area
    nuevo.save()

if __name__ == "__main__":
    pass
