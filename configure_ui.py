# Form implementation generated from reading ui file 'Forms/Configure.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Configure_dialog(object):
    def setupUi(self, Configure_dialog):
        Configure_dialog.setObjectName("Configure_dialog")
        Configure_dialog.resize(312, 146)
        self.gridLayout = QtWidgets.QGridLayout(Configure_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Login_text = QtWidgets.QLineEdit(parent=Configure_dialog)
        self.Login_text.setObjectName("Login_text")
        self.gridLayout.addWidget(self.Login_text, 0, 1, 1, 1)
        self.login_lable = QtWidgets.QLabel(parent=Configure_dialog)
        self.login_lable.setObjectName("login_lable")
        self.gridLayout.addWidget(self.login_lable, 0, 0, 1, 1)
        self.password_lable = QtWidgets.QLabel(parent=Configure_dialog)
        self.password_lable.setObjectName("password_lable")
        self.gridLayout.addWidget(self.password_lable, 1, 0, 1, 1)
        self.Password_text = QtWidgets.QLineEdit(parent=Configure_dialog)
        self.Password_text.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Password_text.setObjectName("Password_text")
        self.gridLayout.addWidget(self.Password_text, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Status_label = QtWidgets.QLabel(parent=Configure_dialog)
        self.Status_label.setStyleSheet("color: red")
        self.Status_label.setText("")
        self.Status_label.setObjectName("Status_label")
        self.horizontalLayout.addWidget(self.Status_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Save_button = QtWidgets.QPushButton(parent=Configure_dialog)
        self.Save_button.setEnabled(False)
        self.Save_button.setMinimumSize(QtCore.QSize(100, 0))
        self.Save_button.setObjectName("Save_button")
        self.horizontalLayout.addWidget(self.Save_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.retranslateUi(Configure_dialog)
        QtCore.QMetaObject.connectSlotsByName(Configure_dialog)

    def retranslateUi(self, Configure_dialog):
        _translate = QtCore.QCoreApplication.translate
        Configure_dialog.setWindowTitle(_translate("Configure_dialog", "Настройка пользователя"))
        self.login_lable.setText(_translate("Configure_dialog", "Логин"))
        self.password_lable.setText(_translate("Configure_dialog", "Пароль"))
        self.Save_button.setText(_translate("Configure_dialog", "Сохранить"))