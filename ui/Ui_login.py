# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\palmtale@live.com\Weiyun\Workspace\eric\palmcoin\ui/login.ui'
#
# Created: Tue Jan  7 01:17:23 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginForm(object):
    def setupUi(self, loginForm):
        loginForm.setObjectName(_fromUtf8("loginForm"))
        loginForm.resize(412, 301)
        self.platformSelector = QtGui.QComboBox(loginForm)
        self.platformSelector.setGeometry(QtCore.QRect(300, 20, 81, 22))
        self.platformSelector.setObjectName(_fromUtf8("platformSelector"))
        self.platformLab = QtGui.QLabel(loginForm)
        self.platformLab.setGeometry(QtCore.QRect(220, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.platformLab.setFont(font)
        self.platformLab.setObjectName(_fromUtf8("platformLab"))
        self.accessLab = QtGui.QLabel(loginForm)
        self.accessLab.setGeometry(QtCore.QRect(50, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accessLab.setFont(font)
        self.accessLab.setObjectName(_fromUtf8("accessLab"))
        self.secretLab = QtGui.QLabel(loginForm)
        self.secretLab.setGeometry(QtCore.QRect(50, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.secretLab.setFont(font)
        self.secretLab.setObjectName(_fromUtf8("secretLab"))
        self.accessInput = QtGui.QLineEdit(loginForm)
        self.accessInput.setGeometry(QtCore.QRect(150, 120, 211, 20))
        self.accessInput.setEchoMode(QtGui.QLineEdit.Normal)
        self.accessInput.setObjectName(_fromUtf8("accessInput"))
        self.secretInput = QtGui.QLineEdit(loginForm)
        self.secretInput.setGeometry(QtCore.QRect(150, 170, 211, 20))
        self.secretInput.setEchoMode(QtGui.QLineEdit.Password)
        self.secretInput.setObjectName(_fromUtf8("secretInput"))
        self.checkBtn = QtGui.QPushButton(loginForm)
        self.checkBtn.setGeometry(QtCore.QRect(270, 220, 75, 23))
        self.checkBtn.setObjectName(_fromUtf8("checkBtn"))

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        loginForm.setWindowTitle(_translate("loginForm", "Palm Coin", None))
        self.platformLab.setText(_translate("loginForm", "Platform:", None))
        self.accessLab.setText(_translate("loginForm", "Access Key:", None))
        self.secretLab.setText(_translate("loginForm", "Secret Key:", None))
        self.checkBtn.setText(_translate("loginForm", "OK", None))

