from main_window_ui import Ui_MainWindow
from auth_ui import Ui_Auth_dialog
from configure_ui import Ui_Configure_dialog
from redact_account_ui import Ui_Redact_account_dialog
import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from constants import server_address
from enum import Enum, auto


class Stages(Enum):
    Main = auto()
    Auth = auto()
    Configure = auto()
    Redact_account = auto()


def main_redact_account():
    if global_stages[0] == Stages.Main:
        ui_redact_account.Current_password_text.clear()
        ui_redact_account.Password_text.clear()
        ui_redact_account.Login_text.clear()
        ui_redact_account.Status_label.clear()
        window_redact_account.show()
        global_stages[0] = Stages.Redact_account


def auth_login():
    if global_stages[0] == Stages.Auth:
        global cookies
        try:
            response = requests.get(
                f'{server_address}/api/auth',
                json={'auth': [ui_auth.Login_text.text(), ui_auth.Password_text.text()]}
            )
        except requests.exceptions.ConnectionError:
            ui_auth.Status_label.setText('Нет соединения')
        else:
            if response.ok:
                cookies = response.cookies
                window_auth.hide()
                if response.text == 'not changed':
                    global_stages[0] = Stages.Configure
                    window_configure.show()
                    ui_configure.Login_text.setText(ui_auth.Login_text.text())
                else:
                    global_stages[0] = Stages.Main
                    window_main.show()
            else:
                ui_auth.Status_label.setText('Данные неверны')


def auth_text_changed():
    if global_stages[0] == Stages.Auth:
        if ui_auth.Password_text.text() and ui_auth.Login_text.text():
            ui_auth.Auth_button.setEnabled(True)
        else:
            ui_auth.Auth_button.setEnabled(False)


def configure_save():
    if global_stages[0] == Stages.Configure:
        global cookies
        response = requests.get(
            f'{server_address}/api/configure',
            json={'configure': [ui_configure.Login_text.text(), ui_configure.Password_text.text()]},
            cookies=cookies
        )
        if response.text == 'incorrect_login':
            ui_configure.Status_label.setText('Логин уже занят')
        else:
            global_stages[0] = Stages.Main
            window_configure.hide()
            window_main.show()


def configure_text_changed():
    if global_stages[0] == Stages.Configure:
        if ui_configure.Password_text.text() and ui_configure.Login_text.text():
            ui_configure.Save_button.setEnabled(True)
        else:
            ui_configure.Save_button.setEnabled(False)


def redact_account_text_changed():
     if global_stages[0] == Stages.Redact_account:
        if ui_redact_account.Password_text.text() and ui_redact_account.Login_text.text() and ui_redact_account.Current_password_text.text():
            ui_redact_account.Save_button.setEnabled(True)
        else:
            ui_redact_account.Save_button.setEnabled(False)


def redact_account_save():
    if global_stages[0] == Stages.Redact_account:
        global cookies
        response = requests.get(
            f'{server_address}/api/redact_account',
            json={
                'configure': [
                    ui_redact_account.Login_text.text(),
                    ui_redact_account.Password_text.text()
                ],
                'current_password': ui_redact_account.Current_password_text.text()
            },
            cookies=cookies
        )
        if response.text == 'incorrect_login':
            ui_redact_account.Status_label.setText('Логин уже занят')
        elif response.text == 'incorrect_auth':
            ui_redact_account.Status_label.setText('Неверный\nтекущий праоль')
        else:
            global_stages[0] = Stages.Main
            window_redact_account.hide()


global_stages = [Stages.Auth]
cookies = False


app = QtWidgets.QApplication(sys.argv)

# setuping


window_main = QtWidgets.QMainWindow()
ui_main_window = Ui_MainWindow()
ui_main_window.setupUi(window_main)

window_auth = QtWidgets.QDialog()
ui_auth = Ui_Auth_dialog()
ui_auth.setupUi(window_auth)

window_configure = QtWidgets.QDialog()
ui_configure = Ui_Configure_dialog()
ui_configure.setupUi(window_configure)

class WindowRedactAccount(QtWidgets.QWidget):
    def __init__(self):
        super(WindowRedactAccount, self).__init__(None)
    def closeEvent(self, event):
        global_stages[0] = Stages.Main
window_redact_account = WindowRedactAccount()    
ui_redact_account = Ui_Redact_account_dialog()
ui_redact_account.setupUi(window_redact_account)

# functional
ui_main_window.Redact_account_button.clicked.connect(main_redact_account)
# self.Variant_number_text.textChanged['QString'].connect(self.Variant_list.clearSelection) # type: ignore
# self.Variant_list.currentRowChanged['int'].connect(self.Variant_number_text.clear) # type: ignore
# self.Task_number_text.textChanged['QString'].connect(self.Task_list.clearSelection) # type: ignore
# self.Task_list.currentRowChanged['int'].connect(self.Task_number_text.clear) # type: ignore

ui_auth.Auth_button.clicked.connect(auth_login)
ui_auth.Login_text.textChanged.connect(auth_text_changed)
ui_auth.Password_text.textChanged.connect(auth_text_changed)

ui_configure.Login_text.textChanged.connect(configure_text_changed)
ui_configure.Password_text.textChanged.connect(configure_text_changed)
ui_configure.Save_button.clicked.connect(configure_save)

ui_redact_account.Login_text.textChanged.connect(redact_account_text_changed)
ui_redact_account.Password_text.textChanged.connect(redact_account_text_changed)
ui_redact_account.Current_password_text.textChanged.connect(redact_account_text_changed)
ui_redact_account.Save_button.clicked.connect(redact_account_save)

# starting
window_auth.show()
app.exec()

