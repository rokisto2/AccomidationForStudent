# Form implementation generated from reading ui file 'App/Design/untitled.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 614)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.mail = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.mail.setGeometry(QtCore.QRect(30, 100, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        self.mail.setFont(font)
        self.mail.setInputMask("")
        self.mail.setText("")
        self.mail.setObjectName("mail")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 150, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(17)
        self.password.setFont(font)
        self.password.setInputMask("")
        self.password.setText("")
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(30, 460, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        self.loginButton.setFont(font)
        self.loginButton.setCheckable(False)
        self.loginButton.setChecked(False)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setObjectName("loginButton")
        self.loginButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.loginButton_2.setGeometry(QtCore.QRect(30, 510, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        self.loginButton_2.setFont(font)
        self.loginButton_2.setCheckable(False)
        self.loginButton_2.setChecked(False)
        self.loginButton_2.setAutoDefault(False)
        self.loginButton_2.setObjectName("loginButton_2")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 210, 208, 101))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioStudent = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.radioStudent.setFont(font)
        self.radioStudent.setObjectName("radioStudent")
        self.verticalLayout.addWidget(self.radioStudent)
        self.radioAdministration = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.radioAdministration.setFont(font)
        self.radioAdministration.setObjectName("radioAdministration")
        self.verticalLayout.addWidget(self.radioAdministration)
        self.radioDeaneryStaff = QtWidgets.QRadioButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.radioDeaneryStaff.setFont(font)
        self.radioDeaneryStaff.setObjectName("radioDeaneryStaff")
        self.verticalLayout.addWidget(self.radioDeaneryStaff)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вход в систему"))
        self.mail.setPlaceholderText(_translate("MainWindow", "Введите почту"))
        self.password.setPlaceholderText(_translate("MainWindow", "Введите пароль"))
        self.loginButton.setText(_translate("MainWindow", "Войти"))
        self.loginButton_2.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.radioStudent.setText(_translate("MainWindow", "Студент"))
        self.radioAdministration.setText(_translate("MainWindow", "Админестратор"))
        self.radioDeaneryStaff.setText(_translate("MainWindow", "Работник деканата"))