import sqlite3

conn = sqlite3.connect('compras.db')
c = conn.cursor()

query = """CREATE TABLE compra(id_compra INTEGER primary key AUTOINCREMENT,
								fecha DATE,
								proveedor TEXT,
								numero_factura INT,
								descripcion TEXT)"""

c.execute(query)





query="""CREATE TABLE producto(id_producto INTEGER primary key AUTOINCREMENT,
								codigo TEXT,
								nombre TEXT,
								descripcion TEXT,
								marca TEXT,
								color TEXT)"""
c.execute(query)

query = """CREATE TABLE compra_has_producto(fk_id_compra INTEGER,
											fk_id_producto Integer,
											cantidad INTEGER,
											precio_unitario INTEGER,
											total INTEGER,
											FOREIGN KEY (fk_id_compra) REFERENCES compras(id_compra),
											FOREIGN KEY (fk_id_producto) REFERENCES producto(id_producto))"""

c.execute(query)