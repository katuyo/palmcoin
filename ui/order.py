# -*- coding: utf-8 -*-
from ui import Ui_order
from PyQt4 import QtGui

class OrderDialog(Ui_order.Ui_orderDialog):

    def __init__(self, dialog):
        Ui_order.Ui_orderDialog.setupUi(self, dialog)
        self.__dialog = dialog
        ui = self
        self.buttonBox.accepted.connect(self.__do_accept)
        self.price_spinner.valueChanged.connect(self.__calc_total)
        self.amount_spinner.valueChanged.connect(self.__calc_total)
        self.price_step_in.textChanged.connect(self.__step_price)
        self.amount_step_in.textChanged.connect(self.__step_amount)

    def __calc_total(self, key_event):
        self.total_show.setText(str(self.price_spinner.value() * self.amount_spinner.value()))

    def __step_price(self):
        self.price_spinner.setSingleStep(float(self.price_step_in.text()))

    def __step_amount(self):
        self.amount_spinner.setSingleStep(float(self.amount_step_in.text()))

    def __do_accept(self):
        from service import app_context
        platform_biz = app_context.get.platform_biz()
        buy_or_sell = 1 if self.buyRadio.isChecked() else 0 if self.sellRadio.isChecked() else -1
        order_result = platform_biz.order(float(self.price_spinner.value()), float(self.amount_spinner.value()), buy_or_sell)
        try:
            self.call_back_prompt.setText(order_result['message'])
        except TypeError:
            if order_result:
                self.call_back_prompt.setText("Order Successfully!")
            else:
                self.call_back_prompt.setText("Order Failed!")

    def show(self):
        self.__dialog.hide()
        self.call_back_prompt.setText('')
        self.__dialog.show()

    def set_price_amount(self, price, amount):
        self.price_spinner.setValue(float(price))
        self.amount_spinner.setValue(float(amount))
