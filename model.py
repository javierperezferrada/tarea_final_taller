# -*- coding: utf-8 -*-
"""
Ejemplo simple de aplicación de un diagrama de clases.
Las clases representan a las entidades, las cuales a su vez
son tablas en la base de datos.
La ventaja de las clases es que además de los atributos poseen
métodos que facilitan las consultas y ĺas centralizan.
Con esto ya se puede tener una patrón de diseño MVC.
**ADVERTENCIA:**
Este ejemplo carece de varias consideraciones que habría que tomar
al realizar una aplicación real, especialmente una APP de escritorio
que admita varios hilos de ejecución.

TODO:
    - Mantener consistencia de objetos con la BD.
    - En este esquema todavía no se pueden hacer consultas complejas (Join).
    - Clase Base que represente a una tabla genérica con los métodos Insert,
    Update, delete y load.
    - Manejar restricciones de BD a nivel de clases.
    - Cualquier cambio estructural (atributos/columnas) en las clases hay que
    replicarlo (con sentencias SQL) en la base de datos.
    - Etc.
"""
import sqlite3


def connect():
    """Retorna una conexión con la base de datos"""
    conn = sqlite3.connect('compras.db')
    conn.row_factory = sqlite3.Row
    return conn


def last_id(conn):
    """Retorna la última primary key generada en la base de datos"""
    result = conn.execute("SELECT last_insert_rowid()")
    return result.fetchone()


class Producto(object):
    """
    Clase que representa a la tabla productos
    Una instancia de esta clase representa a una fila.
    La instancia (objeto) puede estar en BD o no.
    El método save de la clase inserta o actualiza el registro según
    Corresponda
    Los atributos de la clase deben tener correspondencia con la BD
    (Nombres y tipos de datos)
    """
    __tablename__ = "producto"
    id_producto = None  # Primary Key
    codigo = ""
    nombre = ""
    descripcion = ""
    marca = ""
    color = ""

    def __init__(
            self,
            id_producto=None,
            codigo="",
            nombre="",
            descripcion="",
            marca="",
            color=""):

        self.id_producto = id_producto
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.marca = marca
        self.color = color

        # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
        if id_producto is not None:
            self.load()
        elif nombre is not None:
            self.load(nombre=nombre)

    def load(self, nombre=None):
        """
        Carga un producto de la base de datos por id_producto o nombre
        """
        conn = connect()
        query = "SELECT * FROM producto "
        if nombre is not None:
            query += " WHERE nombre = ?"
            condition = nombre
        else:
            if self.id_producto is None:
                return
            query += " WHERE id_producto = ?"
            condition = self.id_producto

        result = conn.execute(
            query, [condition])
        row = result.fetchone()
        conn.close()
        if row is not None:
            self.id_producto = row[0]
            self.codigo = row[1]
            self.nombre = row[2]
            self.descripcion = row[3]
            self.marca = row[4]
            self.color = row[5]
        else:
            self.id_producto = None
            #print "El registro no existe"

    def save(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if self.id_producto is None:
            self.id_producto = self.__insert()
        else:
            self.__update()

    def __insert(self):
        query = "INSERT INTO {0} ".format(self.__tablename__)
        # La pk está definida como auto increment en el modelo
        query += "(codigo, nombre, descripcion, marca, color) "
        query += "VALUES (?, ?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.codigo,
                    self.nombre,
                    self.descripcion,
                    self.marca,
                    self.color])
            conn.commit()
            id_producto = last_id(conn)
            conn.close()
            return id_producto
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self):
        query = "UPDATE {} ".format(self.__tablename__)
        query += "SET codigo = ?, "
        query += "nombre = ?, "
        query += "descripcion = ?, "
        query += "marca = ?, "
        query += "color = ? "
        query += "WHERE id_producto = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.codigo,
                    self.nombre,
                    self.descripcion,
                    self.marca,
                    self.color,
                    self.id_producto])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def delete(self):
        query = "DELETE FROM {} ".format(self.__tablename__)
        query += "WHERE id_producto = ?"
        try:
            conn = connect()
            conn.execute(query, [self.id_producto])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla productos.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase
        """
        query = "SELECT * FROM {}".format(cls.__tablename__)
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()
            return data

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    @classmethod
    def productos(cls, id_compra=None):
        query = "SELECT p.* FROM producto p, compra_has_producto c WHERE p.id_producto = c.fk_id_producto and c.fk_id_compra = ?"
        try:
            conn = connect()
            result = conn.execute(query, [id_compra])
            data = result.fetchall()
            return data
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None



class Compra(object):
    """
    Clase que representa a la tabla compra
    Una instancia de esta clase representa a una fila.
    La instancia (objeto) puede estar en BD o no.
    El método save de la clase inserta o actualiza el registro según
    Corresponda
    Los atributos de la clase deben tener correspondencia con la BD
    (Nombres y tipos de datos)
    """
    __tablename__ = "compra"
    id_compra = None  # Primary Key
    fecha = ""
    proveedor = ""
    numero_factura = 0
    descripcion = ""

    def __init__(
            self,
            id_compra=None,
            fecha="",
            proveedor="",
            numero_factura= 0,
            descripcion=""):

        self.fecha = fecha
        self.proveedor = proveedor
        self.numero_factura = numero_factura
        self.descripcion = descripcion

        # Si la pk tiene valor hay que traer el objeto (Fila) de la DB
        if id_compra is not None:
            self.id_compra = id_compra
            self.__load()

    def __load(self):
        if self.id_compra is not None:
            conn = connect()
            query = "SELECT * FROM compra WHERE id_compra = ?"
            result = conn.execute(
                query, [self.id_compra])
            row = result.fetchone()
            conn.close()
            if row is not None:
                self.fecha = row[1]
                self.proveedor = row[2]
                self.numero_factura = row[3]
                self.descripcion = row[4]
            else:
                self.id_compra = None
                print "El registro no existe"

    def save(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        if self.id_compra is None:
            self.id_compra = self.__insert()
        else:
            self.__update()

    def __insert(self):
        query = "INSERT INTO compra "
        # La pk está definida como auto increment en el modelo
        query += "(fecha, proveedor, numero_factura, descripcion) "
        query += "VALUES (?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.fecha,
                    self.proveedor,
                    self.numero_factura,
                    self.descripcion])
            conn.commit()
            id_compra = last_id(conn)
            conn.close()
            return id_compra
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self):
        query = "UPDATE compra "
        query += "SET fecha = ?, "
        query += "proveedor = ?, "
        query += "numero_factura = ?, "
        query += "descripcion = ? "
        query += "WHERE id_compra = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.fecha,
                    self.proveedor,
                    self.numero_factura,
                    self.descripcion,
                    self.id_compra])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def delete(self):
        query = "DELETE FROM compra "
        query += "WHERE id_compra = ?"
        try:
            conn = connect()
            conn.execute(query, [self.id_compra])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla compra.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase.
        """
        query = "SELECT * FROM compra"
        compras = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()
            return data

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def last_id(self):
        #funcion que retorna el ultimo id_compra ingresado
        query = "SELECT MAX(id_compra) FROM compra"
        try:
            conn = connect()
            result = conn.execute(query)
            return result.fetchone()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return -1



class Compra_has_Producto(object):
    """
    Clase que representa a la tabla compra_has_producto
    Una instancia de esta clase representa a una fila.
    La instancia (objeto) puede estar en BD o no.
    El método save de la clase inserta o actualiza el registro según
    Corresponda
    Los atributos de la clase deben tener correspondencia con la BD
    (Nombres y tipos de datos)
    """
    __tablename__ = "compra_has_producto"
    fk_id_compra = 0
    fk_id_producto = 0
    cantidad = 0
    precio_unitario = 0
    total = 0


    def __init__(
            self,
            fk_id_compra=0,
            fk_id_producto=0,
            cantidad=0,
            precio_unitario=0,
            total=0):
        self.fk_id_compra = fk_id_compra
        self.fk_id_producto = fk_id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.total = total



    def save(self):
        """
        Guarda el objeto en la base de datos.
        Utiliza un insert o update según Corresponda
        """
        self.__insert()


    def __insert(self):
        query = "INSERT INTO compra_has_producto "
        # La pk está definida como auto increment en el modelo
        query += "(fk_id_compra, fk_id_producto, cantidad, precio_unitario, total) "
        query += "VALUES (?, ?, ?, ?, ?)"
        try:
            conn = connect()
            result = conn.execute(
                query, [
                    self.fk_id_compra,
                    self.fk_id_producto,
                    self.cantidad,
                    self.precio_unitario,
                    self.total])
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None

    def __update(self):
        query = "UPDATE compra "
        query += "SET fecha = ?, "
        query += "proveedor = ?, "
        query += "numero_factura = ?, "
        query += "descripcion = ? "
        query += "WHERE id_compra = ?"
        try:
            conn = connect()
            conn.execute(
                query, [
                    self.fecha,
                    self.proveedor,
                    self.numero_factura,
                    self.descripcion,
                    self.id_compra])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    def delete(self):
        query = "DELETE FROM compra "
        query += "WHERE id_compra = ?"
        try:
            conn = connect()
            conn.execute(query, [self.id_compra])
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return False

    @classmethod
    def all(cls):
        """
        Método utlizado para obtener la colección completa de filas
        en la tabla compra.
        Este método al ser de clase no necesita una instancia (objeto)
        Sólo basta con invocarlo desde la clase.
        """
        query = "SELECT * FROM compra"
        compras = list()
        try:
            conn = connect()
            result = conn.execute(query)
            data = result.fetchall()
            return data

        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
            return None