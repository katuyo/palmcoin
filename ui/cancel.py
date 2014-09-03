__author__ = 'Palm Tale'

from ui import Ui_cancel
from service import app_context
import time


class CancelDialog(Ui_cancel.Ui_cancel_dialog):

    def __init__(self, dialog):
        self.setupUi(dialog)
        self.__dialog = dialog
        self.__order = None

        self.button_box.accepted.connect(self.__cancel_order)
        self.button_box.rejected.connect(self.__dialog.reject)

    def show(self):
        self.__dialog.hide()
        self.__dialog.show()

    def set_order(self, order):
        self.__order = order
        order_info = time.strftime('%Y-%m-%d %H:%I:%S', time.localtime(order.date_time())) + " "
        order_info += order.type() + " "
        order_info += str(order.price()) + " CNY/BTC * "
        order_info += str(order.amount()) + " BTC = "
        order_info += str(order.price() * order.amount()) + " CNY"
        self.order_label.setText(order_info)

    def __cancel_order(self):
        platform_biz = app_context.get.platform_biz()
        result = platform_biz.cancel(self.__order)
        try:
            self.order_label.setText(result['message'])
        except TypeError:
            if result:
                self.order_label.setText("Cancelled successfully.")
            else:
                self.order_label.setText("Cancel failed.")
