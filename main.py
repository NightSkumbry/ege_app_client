# from main_window import Ui_MainWindow as main_window
from auth_ui import Ui_Auth_dialog
from configure_ui import Ui_Configure_dialog
import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from constants import server_address


def auth_login():
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
                global_stages[0] = 'configure'
                window_configure.show()
                ui_configure.Login_text.setText(ui_auth.Login_text.text())
            else:
                global_stages[0] = 'main'
                window_main.show()
        else:
            ui_auth.Status_label.setText('Данные неверны')


def auth_text_changed():
    if ui_auth.Password_text.text() and ui_auth.Login_text.text():
        ui_auth.Auth_button.setEnabled(True)
    else:
        ui_auth.Auth_button.setEnabled(False)


def configure_save():
    global cookies
    response = requests.get(
        f'{server_address}/api/configure',
        json={'configure': [ui_configure.Login_text.text(), ui_configure.Password_text.text()]},
        cookies=cookies
    )
    if response.text == 'incorrect_login':
        ui_configure.Status_label.setText('Логин уже занят')
    else:
        global_stages[0] = 'main'
        window_configure.hide()
        window_main.show()


def configure_text_changed():
    if ui_configure.Password_text.text() and ui_configure.Login_text.text():
        ui_configure.Save_button.setEnabled(True)
    else:
        ui_configure.Save_button.setEnabled(False)


global_stages = ['auth']
cookies = False


app = QtWidgets.QApplication(sys.argv)

# setuping
window_main = QtWidgets.QMainWindow()
# ui_main_window = main_window()
# ui_main_window.setupUi(window)
window_auth = QtWidgets.QDialog()
ui_auth = Ui_Auth_dialog()
ui_auth.setupUi(window_auth)
window_configure = QtWidgets.QDialog()
ui_configure = Ui_Configure_dialog()
ui_configure.setupUi(window_configure)

# functional
ui_auth.Auth_button.clicked.connect(auth_login)
ui_auth.Login_text.textChanged.connect(auth_text_changed)
ui_auth.Password_text.textChanged.connect(auth_text_changed)
ui_configure.Login_text.textChanged.connect(configure_text_changed)
ui_configure.Password_text.textChanged.connect(configure_text_changed)
ui_configure.Save_button.clicked.connect(configure_save)

# starting
window_auth.show()
app.exec()

