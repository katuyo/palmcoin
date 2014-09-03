# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\palmtale@live.com\Weiyun\Workspace\eric\palmcoin\ui/order.ui'
#
# Created: Tue Jan  7 01:18:03 2014
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

class Ui_orderDialog(object):
    def setupUi(self, orderDialog):
        orderDialog.setObjectName(_fromUtf8("orderDialog"))
        orderDialog.resize(401, 263)
        self.buttonBox = QtGui.QDialogButtonBox(orderDialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 220, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(orderDialog)
        self.label.setGeometry(QtCore.QRect(30, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(orderDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(orderDialog)
        self.label_3.setGeometry(QtCore.QRect(50, 190, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.total_show = QtGui.QLineEdit(orderDialog)
        self.total_show.setEnabled(False)
        self.total_show.setGeometry(QtCore.QRect(120, 190, 113, 20))
        self.total_show.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.total_show.setReadOnly(True)
        self.total_show.setObjectName(_fromUtf8("total_show"))
        self.price_step_in = QtGui.QLineEdit(orderDialog)
        self.price_step_in.setGeometry(QtCore.QRect(310, 90, 61, 20))
        self.price_step_in.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.price_step_in.setCursorPosition(3)
        self.price_step_in.setObjectName(_fromUtf8("price_step_in"))
        self.amount_step_in = QtGui.QLineEdit(orderDialog)
        self.amount_step_in.setGeometry(QtCore.QRect(310, 140, 61, 20))
        self.amount_step_in.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.amount_step_in.setObjectName(_fromUtf8("amount_step_in"))
        self.label_4 = QtGui.QLabel(orderDialog)
        self.label_4.setGeometry(QtCore.QRect(250, 90, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(orderDialog)
        self.label_5.setGeometry(QtCore.QRect(250, 140, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.price_spinner = QtGui.QDoubleSpinBox(orderDialog)
        self.price_spinner.setGeometry(QtCore.QRect(120, 90, 121, 22))
        self.price_spinner.setDecimals(6)
        self.price_spinner.setMaximum(999999999.0)
        self.price_spinner.setSingleStep(0.1)
        self.price_spinner.setObjectName(_fromUtf8("price_spinner"))
        self.amount_spinner = QtGui.QDoubleSpinBox(orderDialog)
        self.amount_spinner.setGeometry(QtCore.QRect(120, 140, 121, 22))
        self.amount_spinner.setDecimals(6)
        self.amount_spinner.setMaximum(1000000000.0)
        self.amount_spinner.setSingleStep(0.1)
        self.amount_spinner.setObjectName(_fromUtf8("amount_spinner"))
        self.buyRadio = QtGui.QRadioButton(orderDialog)
        self.buyRadio.setGeometry(QtCore.QRect(70, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.buyRadio.setFont(font)
        self.buyRadio.setStyleSheet(_fromUtf8("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));"))
        self.buyRadio.setChecked(True)
        self.buyRadio.setObjectName(_fromUtf8("buyRadio"))
        self.sellRadio = QtGui.QRadioButton(orderDialog)
        self.sellRadio.setGeometry(QtCore.QRect(190, 40, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sellRadio.setFont(font)
        self.sellRadio.setStyleSheet(_fromUtf8("color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));"))
        self.sellRadio.setChecked(False)
        self.sellRadio.setObjectName(_fromUtf8("sellRadio"))
        self.call_back_prompt = QtGui.QLabel(orderDialog)
        self.call_back_prompt.setGeometry(QtCore.QRect(50, 10, 311, 31))
        self.call_back_prompt.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.call_back_prompt.setText(_fromUtf8(""))
        self.call_back_prompt.setObjectName(_fromUtf8("call_back_prompt"))

        self.retranslateUi(orderDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), orderDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), orderDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(orderDialog)

    def retranslateUi(self, orderDialog):
        orderDialog.setWindowTitle(_translate("orderDialog", "Order", None))
        self.label.setText(_translate("orderDialog", "Price:", None))
        self.label_2.setText(_translate("orderDialog", "Amount:", None))
        self.label_3.setText(_translate("orderDialog", "Total:", None))
        self.price_step_in.setText(_translate("orderDialog", "0.1", None))
        self.amount_step_in.setText(_translate("orderDialog", "0.1", None))
        self.label_4.setText(_translate("orderDialog", "Step:", None))
        self.label_5.setText(_translate("orderDialog", "Step:", None))
        self.buyRadio.setText(_translate("orderDialog", "BUY", None))
        self.sellRadio.setText(_translate("orderDialog", "SELL", None))

