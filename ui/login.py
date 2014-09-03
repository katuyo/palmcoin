# -*- coding: utf-8 -*-

from ui import Ui_login
from ui import main
from config import util
from PyQt4 import QtCore

class LoginForm(Ui_login.Ui_loginForm):
   
    def __init__(self, login_form, main_window):
        Ui_login.Ui_loginForm.setupUi(self, login_form)
        self.__loginForm = login_form
        self.__mainWindow = main_window
        self.checkBtn.clicked.connect(self.__click_ok)
        self.platformSelector.currentIndexChanged.connect(self.__set_keys_input)
        self.__platform_keys = util.read_config_keys()
        for index in range(len(self.__platform_keys)):
            self.platformSelector.addItem("")
            self.platformSelector.setItemText(index, QtCore.QCoreApplication.translate("loginForm", self.__platform_keys[index]['platform'], None))

    def __set_keys_input(self, index):
        self.accessInput.setText(self.__platform_keys[index]['accessKey'])
        self.secretInput.setText(self.__platform_keys[index]['secretKey'])
    
    def __click_ok(self):
        selected_text = self.platformSelector.currentText()
        access_key = self.accessInput.text()
        secret_key = self.secretInput.text()
        from service import app_context
        if app_context.get.validate_account(selected_text, access_key, secret_key):
            # Login success,  1.Save config, 
            self.__platform_keys[self.platformSelector.currentIndex()]['accessKey'] = access_key
            self.__platform_keys[self.platformSelector.currentIndex()]['secretKey'] = secret_key
            from config import util
            util.save_platform_keys(self.__platform_keys)
            # 2. Pop-up main window, 
            main.MainWindow(self.__mainWindow)
            self.__mainWindow.show()
            # 3. Self dispose
            self.__loginForm.close()
