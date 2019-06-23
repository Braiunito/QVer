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
cursor=conexion.cursor()
cursor.execute("select * from usuario")
usuarios=cursor.fetchall()
print(cursor.fetchall())


#Sentencia para XAMPP MySQL
#INSERT INTO `usuario` ( `nombre`, `contraseña`, `correo`) VALUES ("Braiunito", "42922075", "braiantablet@gmail.com")