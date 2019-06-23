from PyQt5 import QtCore, QtGui, QtWidgets

from validarcorreo import validarcorreo, verexist

from Vista import *
from Modelo import Usuario

from BDConnector import *
import pymysql
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


    def function(self):
        self.ventanalogin.btn_sgte.clicked.connect(lambda:self.charge_confirm(self.ventanalogin.txt_pass, self.ventanalogin.txt_usr, self.ventanalogin.lbl_info))
        self.ventanalogin.btn_cc.clicked.connect(lambda:Mostrar_Sign())


    def charge_confirm(*args):
        Datos=Usuario().logearse(args[1], args[2], args[3])
        if Datos != None:
            Sesion=Usuario(Datos[1], Datos[2], Datos[3])

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

    def ver(self, ch, txt_pass, txt_pass_con):
        if ch.isChecked() == True:
            self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.ventanasignup.txt_pass.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ventanasignup.txt_pass_con.setEchoMode(QtWidgets.QLineEdit.Password)

    def function(self):
        self.ventanasignup.btn_log.clicked.connect(lambda:Mostrar_Login())
        self.ventanasignup.btn_sgte.clicked.connect(lambda:self.registrar(self.ventanasignup.txt_usr, self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con, self.ventanasignup.lbl_info, self.ventanasignup.txt_mail))
        self.ventanasignup.checkBox.toggled.connect(lambda:self.ver(self.ventanasignup.checkBox,self.ventanasignup.txt_pass, self.ventanasignup.txt_pass_con))


    def registrar(*args):
        Usuario().validar_registro(args[1], args[2], args[3], args[4], args[5])

#INSTANCIA LAS PANTALLAS
LoginScreen=Controlador_Login()
SingupScreen=Controlador_Signup()


#LLAMA A LAS PANTALLAS
def Mostrar_Login():
    LoginScreen.Dialog.show()
    SingupScreen.Dialog.hide()
def Mostrar_Sign():
    LoginScreen.Dialog.hide()
    SingupScreen.Dialog.show()





#INIT DEL LOGIN
if __name__ == "__main__":
    Mostrar_Login()
    sys.exit(LoginScreen.app.exec_())
		