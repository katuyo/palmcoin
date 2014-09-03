# -*- coding: utf-8 -*-
import threading
import time

from PyQt4 import QtGui
from ui import Ui_main, order, cancel
from service import app_context


class MainWindow(Ui_main.Ui_MainWindow):

    def __init__(self, main_window):
        Ui_main.Ui_MainWindow.setupUi(self, main_window)
        self.__window = main_window
        self.__prepare_ui()
        self.__prepare_info()

        self.__dialog = order.OrderDialog(QtGui.QDialog())
        self.__window.keyPressEvent = self.__call_order_dialog

        self.__cancel_dialog = cancel.CancelDialog(QtGui.QDialog())
        # For auto refresh market depth and order records
        self.__market_timer = None
        self.__order_timer = None
        self.__runTimer = True
        self.__timer_up()
        self.__window.closeEvent = self.__timer_down

    def __prepare_ui(self):
        self.freshButton.clicked.connect(self.render_market_depth)
        self.freshButtono.clicked.connect(self.render_orders)
        self.autoRadio.clicked.connect(self.__toggle_fresh_change)
        self.manualRadio.clicked.connect(self.__toggle_fresh_change)
        self.autoRadioo.clicked.connect(self.__toggle_fresh_change)
        self.manualRadioo.clicked.connect(self.__toggle_fresh_change)
        self.asksDepth.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.bidsDepth.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.sellList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.buyList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.buyList.itemClicked.connect(self.__cancel_order)
        self.sellList.itemClicked.connect(self.__cancel_order)
        self.asksDepth.itemDoubleClicked.connect(self.__order_selected)
        self.bidsDepth.itemDoubleClicked.connect(self.__order_selected)

    def __prepare_info(self):
        platform_name = app_context.get.platform_biz().platform_name()
        self.platformInfo.setText(platform_name)
        account = app_context.get.current_account()
        self.userNameInfo.setText(account.username())
        coins_info = ''
        for coin in account.balance():
            coins_info += (coin.currency_code() + ': ' + coin.symbol() + str(coin.amount()) + ' ')
        self.balanceInfo.setText(coins_info)
        coins_info = ''
        for coin in account.frozen():
            coins_info += (coin.currency_code() + ': ' + coin.symbol() + str(coin.amount()) + ' ')
        self.frozenInfo.setText(coins_info)
        self.render_market_depth()
        self.render_orders()

    def render_market_depth(self):
        platform_biz = app_context.get.platform_biz()
        market_depth = platform_biz.get_market_depth(self.deep_spinner.value())
        if market_depth is not None:
            self.asksDepth.setRowCount(len(market_depth.asks()))
            self.bidsDepth.setRowCount(len(market_depth.bids()))
            i = 0
            for ask in market_depth.asks():
                _change_table_item(self.asksDepth, i, 0, str(ask.price()))
                _change_table_item(self.asksDepth, i, 1, str(ask.volume()))
                i += 1
            self.asksDepth.scrollToBottom()
            i = 0
            for bid in market_depth.bids():
                _change_table_item(self.bidsDepth, i, 0, str(bid.price()))
                _change_table_item(self.bidsDepth, i, 1, str(bid.volume()))
                i += 1

    def render_orders(self):
        platform_biz = app_context.get.platform_biz()
        orders = platform_biz.get_orders()
        if orders is not None:
            self.buyList.setRowCount(len(orders.buy_orders()))
            self.sellList.setRowCount(len(orders.sell_orders()))
            i = 0
            for buy_order in orders.buy_orders():
                _change_table_item(self.buyList, i, 0, str(buy_order.price()))
                _change_table_item(self.buyList, i, 1, str(buy_order.amount()))
                _change_table_item(self.buyList, i, 2, str(buy_order.price() * buy_order.amount()))
                _change_table_item(self.buyList, i, 3, str(buy_order.status()))
                self.buyList.item(i, 3).setData(9, buy_order)
                time_string = time.strftime('%Y-%m-%d %H:%I:%S', time.localtime(buy_order.date_time()))
                _change_table_item(self.buyList, i, 4, time_string)
                i += 1
            i = 0
            for sell_order in orders.sell_orders():
                _change_table_item(self.sellList, i, 0, str(sell_order.price()))
                _change_table_item(self.sellList, i, 1, str(sell_order.amount()))
                _change_table_item(self.sellList, i, 2, str(sell_order.price() * sell_order.amount()))
                _change_table_item(self.sellList, i, 3, str(sell_order.status()))
                self.sellList.item(i, 3).setData(9, sell_order)
                time_string = time.strftime('%Y-%m-%d %H:%I:%S', time.localtime(sell_order.date_time()))
                _change_table_item(self.sellList, i, 4, time_string)
                i += 1

    # Events slots
    def __call_order_dialog(self, key_event=[], kwargs=[]):
        if 16777269 == key_event.key():
            self.__dialog.show()

    def __order_selected(self, event):
        selected_items = self.asksDepth.selectedItems()
        if len(selected_items) >= 2 and (event == selected_items[0] or event == selected_items[1]):
            self.__dialog.set_price_amount(selected_items[0].text(), selected_items[1].text())
            self.__dialog.buyRadio.setChecked(True)
            self.__dialog.show()
            return
        selected_items = self.bidsDepth.selectedItems()
        if len(selected_items) >= 2 and (event == selected_items[0] or event == selected_items[1]):
            self.__dialog.set_price_amount(selected_items[0].text(), selected_items[1].text())
            self.__dialog.sellRadio.setChecked(True)
            self.__dialog.show()

    def __cancel_order(self, item):
        if item.text() != 'Cancel':
            return
        self.__cancel_dialog.set_order(item.data(9))
        self.__cancel_dialog.show()

    def __toggle_fresh_change(self):
        if self.autoRadio.isChecked():
            self.periodSpin.setEnabled(True)
            self.freshButton.setEnabled(False)
        else:
            if self.manualRadio.isChecked():
                self.periodSpin.setEnabled(False)
                self.freshButton.setEnabled(True)
        if self.autoRadioo.isChecked():
            self.periodSpino.setEnabled(True)
            self.freshButtono.setEnabled(False)
        else:
            if self.manualRadioo.isChecked():
                self.periodSpino.setEnabled(False)
                self.freshButtono.setEnabled(True)

    def __timer_up(self):
        self.__market_timer = threading.Thread()
        self.__market_timer.run = self.__run_market_rendering
        self.__order_timer = threading.Thread()
        self.__order_timer.run = self.__run_orders_rendering
        self.__market_timer.start()
        self.__order_timer.start()

    def __run_market_rendering(self):
        while self.__runTimer:
            if self.autoRadio.isChecked():
                self.render_market_depth()
            time.sleep(self.periodSpin.value())

    def __run_orders_rendering(self):
        while self.__runTimer:
            if self.autoRadioo.isChecked():
                self.render_orders()
            time.sleep(self.periodSpino.value())

    def __timer_down(self, args=[], kwargs=[]):
        self.__runTimer = False


def _change_table_item(table, row, column, new_string=''):
    item = table.item(row, column)
    if item is None:
        item = QtGui.QTableWidgetItem(new_string)
        table.setItem(row, column, item)
    else:
        item.setText(new_string)
    if new_string == 'Open':
        item.setText('Cancel')
        font = QtGui.QFont()
        font.setUnderline(True)
        item.setFont(font)
    else:
        item.setFont(QtGui.QFont())