from PyQt5 import QtCore, QtGui, QtWidgets
from validarcorreo import validarcorreo, verexist
from Vista import *
import sys

class Controlador_Login(object):
    def __init__(self): 
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ventanalogin = Pantalla_Login()
        self.ventanalogin.setupUi(self.Dialog)
        self.function()
        self.Dialog.show()

    def function(self):
        self.ventanalogin.btn_sgte.clicked.connect(lambda:self.charge_confirm(self.ventanalogin.txt_pass, self.ventanalogin.txt_usr, self.ventanalogin.lbl_info))
        self.ventanalogin.btn_cc.clicked.connect(lambda:self.gotosign())

    def charge_confirm(self, password, user, info):
        database = open ("database.txt", "r")
        usrpass=[]
        flag=False
        for x in database:
            usrpass=usrpass+x.split(",")
        for x in usrpass:
            bk=x.replace("\n", "")
            usrpass[usrpass.index(x)]=bk
        for x in usrpass:
            try:
                if (x == user.text()) and (usrpass[usrpass.index(x)+1]==password.text()):
                    flag=True
            except Exception as e:
                pass
            try:
                if (x == user.text()) and (usrpass[usrpass.index(x)-1]==password.text()):
                    flag=True
            except Exception as e:
                pass


                
        if flag:
            info.setText("Valido")
            info.setStyleSheet("color: rgb(51, 204, 40);")
            info.show()
        else:
            user.clear()
            password.clear()
            info.setText("Usuario o contraseña incorrecto")
            info.setStyleSheet("color: rgb(255, 0, 4);")           
            info.show()
        database.close()
        #print (usrpass)

    def cerrar(self, ventana1):
        self.Dialog.show()
        ventana1.hide()

    def gotosign(self):
        self.crearcuenta = QtWidgets.QMainWindow()
        self.ui=Pantalla_Signup()
        self.ui.setupUi(self.crearcuenta)
        self.crearcuenta.setGeometry(293, 77,781,575)
        self.crearcuenta.show()
        self.ui.btn_log.clicked.connect(lambda:self.cerrar(self.crearcuenta))
        self.Dialog.hide()


class Controlador_Signup(object):
    def __init__(self): 
        self.app = QtWidgets.QApplication(sys.argv)
        self.Dialog = QtWidgets.QDialog()
        self.ventanasignup = Pantalla_Signup()
        self.ventanasignup.setupUi(self.Dialog)
        self.function()

    def function(self):
        self.ventanasignup.btn_sgte.clicked.connect(lambda:self.registrar(self.ventanasignup.txt_usr, self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con, self.ventanasignup.lbl_info, self.ventanasignup.txt_mail))
        self.ventanasignup.checkBox.toggled.connect(lambda:self.ver(self.ventanasignup.checkBox,self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con))


    def ver(self, ch, txt_pass, txt_pass_con):
        if ch.isChecked() == True:
            self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)

    def limpiar(self, *args):
        for x in args:
            x.clear()

    def registrar(self, usr, password, passconf, info, mail):
        #Casos Emptys
        if len(usr.text()) == 0:
            info.setText("Campo usuario vacío.")
            info.show()
        else:
            info.hide()
            if 0 == len(password.text()):
                info.setText("Campo contraseña vacío.")
                info.show() 
            else:
                #Casos Negativos
                info.hide()
                if 3 < len(usr.text()) < 16:
                    info.hide()
                    if 7 < len(password.text()):
                        if passconf.text() == password.text():
                            #Correo opcional
                            validar=verexist(usr.text())
                            if validar:
                                if len(mail.text())==0:
                                    database = open("database.txt", "a")
                                    newuser=usr.text()+","+password.text()+"\n"
                                    database.write(newuser)
                                    info.setStyleSheet("color: rgb(50, 200, 40);")
                                    info.setText("Usuario registrado con exito!(Sin mail).")
                                    database.close()
                                    info.show()
                                    self.limpiar(usr, password, passconf, mail)
                                else:
                            #Con correo registrado
                                    validar=validarcorreo(mail.text())
                                    info.hide()
                                    if validar:
                                        validar=verexist(mail.text())
                                        if validar:
                                            database = open("database.txt", "a")
                                            newuser=usr.text()+","+password.text()+","+mail.text()+"\n"
                                            database.write(newuser)
                                            info.setStyleSheet("color: rgb(50, 200, 40);")
                                            info.setText("Usuario registrado con exito!.")
                                            database.close()
                                            info.show()
                                            self.limpiar(usr, password, passconf, mail)
                                        else:
                                            info.setStyleSheet("color: rgb(255, 0, 4);")
                                            info.setText("Ya existe un usuario regisrado con su mail.")
                                            info.show()
                                    else:
                                        info.setStyleSheet("color: rgb(255, 0, 4);")
                                        info.setText("El E-mail es invalido.")
                                        info.show()
                            else:
                                info.setStyleSheet("color: rgb(255, 0, 4);")
                                info.setText("El usuario ya existe.")
                                info.show()
                        else:
                            info.setText("Las contraseñas no coinciden.")
                            info.show()    
                    else:
                        info.setText("Contraseña insegura, coloque más de 8 caracteres.")
                        info.show()    
                else:
                    info.setText("Ingrese solo nombre entre 4 y 15 caracteres.")
                    info.show()

        


''' ????  Llamada a sign creo
def logearse(self):
    from Login import Ui_Dialog
    self.ventana = QtWidgets.QMainWindow()
    self.ui=Ui_Dialog()
    self.ui.setupUi(self.ventana)
    self.ventana.setGeometry(280, 65,781,575)
    self.ventana.show()
'''


		

#INIT
if __name__ == "__main__":
    Login = Controlador_Login()
    sys.exit(Login.app.exec_())

		