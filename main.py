# from main_window import Ui_MainWindow as main_window
from auth_ui import Ui_Auth_dialog
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
            if response.text:
                ...
            if response.text == 'not changed':
                global_stages[0] = 'configure'
            else:
                global_stages[0] = 'main'
        else:
            ui_auth.Status_label.setText('Данные неверны')


def auth_text_changed():
    if ui_auth.Password_text.text and ui_auth.Login_text.text:
        ui_auth.Auth_button.setEnabled(True)
    else:
        ui_auth.Auth_button.setEnabled(False)


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

# functional
ui_auth.Auth_button.clicked.connect(auth_login)
ui_auth.Login_text.textChanged.connect(auth_text_changed)
ui_auth.Password_text.textChanged.connect(auth_text_changed)

# starting
window_main.show()
window_auth.show()
app.exec()

