# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\palmtale@live.com\Weiyun\Workspace\eric\palmcoin\ui/cancel.ui'
#
# Created: Tue Jan  7 01:17:17 2014
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

class Ui_cancel_dialog(object):
    def setupUi(self, cancel_dialog):
        cancel_dialog.setObjectName(_fromUtf8("cancel_dialog"))
        cancel_dialog.resize(400, 136)
        self.prompt_label = QtGui.QLabel(cancel_dialog)
        self.prompt_label.setGeometry(QtCore.QRect(30, 10, 341, 31))
        self.prompt_label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.prompt_label.setObjectName(_fromUtf8("prompt_label"))
        self.button_box = QtGui.QDialogButtonBox(cancel_dialog)
        self.button_box.setGeometry(QtCore.QRect(210, 90, 156, 23))
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.order_label = QtGui.QLabel(cancel_dialog)
        self.order_label.setGeometry(QtCore.QRect(50, 40, 331, 41))
        self.order_label.setStyleSheet(_fromUtf8("color: rgb(41, 78, 245);"))
        self.order_label.setText(_fromUtf8(""))
        self.order_label.setWordWrap(True)
        self.order_label.setObjectName(_fromUtf8("order_label"))

        self.retranslateUi(cancel_dialog)
        QtCore.QMetaObject.connectSlotsByName(cancel_dialog)

    def retranslateUi(self, cancel_dialog):
        cancel_dialog.setWindowTitle(_translate("cancel_dialog", "Cancel Confirmation", None))
        self.prompt_label.setText(_translate("cancel_dialog", "Are you sure to cancel this order?", None))

