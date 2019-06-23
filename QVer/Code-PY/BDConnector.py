import pymysql

#CONECTA A LA BD
def conectar(usr='', passwod='', bd=''):
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user=usr,
                                 password=passwod,
                                 charset='utf8mb4',
                                 db=bd)
    return connection


conexion=conectar("root","42922075","qver")
usuarios_cursor=conexion.cursor()
usuarios_cursor.execute("select * from usuarios")
print(usuarios_cursor.fetchall())