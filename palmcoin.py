# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui


class Main(object):
    def __init__(self):
        self.__app = QtGui.QApplication(sys.argv)
        self.__login_form = QtGui.QWidget()
        self.__mainWindow = QtGui.QMainWindow()

    def start(self):
        from ui import login
        ui = login.LoginForm(self.__login_form, self.__mainWindow)
        self.__login_form.show()
        sys.exit(self.__app.exec_())
        return ui

if __name__ == '__main__':
    main = Main()
    ui = main.start()
