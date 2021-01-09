from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(514, 181)
        Settings.setMinimumSize(QtCore.QSize(514, 181))
        Settings.setMaximumSize(QtCore.QSize(514, 181))
        self.Settings_2 = QtWidgets.QWidget(Settings)
        self.Settings_2.setObjectName("Settings_2")
        self.slider = QtWidgets.QSlider(self.Settings_2)
        self.slider.setGeometry(QtCore.QRect(170, 46, 331, 22))
        self.slider.setMaximum(100)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.text = QtWidgets.QLabel(self.Settings_2)
        self.text.setGeometry(QtCore.QRect(10, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.text.setFont(font)
        self.text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.text.setObjectName("text")
        self.reset = QtWidgets.QPushButton(self.Settings_2)
        self.reset.setGeometry(QtCore.QRect(220, 80, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.label = QtWidgets.QLabel(self.Settings_2)
        self.label.setGeometry(QtCore.QRect(10, 130, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.Settings_2)
        self.pushButton.setGeometry(QtCore.QRect(420, 140, 31, 27))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.Settings_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 521, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/background1.png"))
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.slider.raise_()
        self.text.raise_()
        self.reset.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        Settings.setCentralWidget(self.Settings_2)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.text.setText(_translate("Settings", "Громкость"))
        self.reset.setText(_translate("Settings", "Сброс"))
        self.label.setText(_translate("Settings",
                                      "Вы уверены? Все настройки и прогресс будут удалены!"))
        self.pushButton.setText(_translate("Settings", "Да"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QMainWindow()
    Settings.setWindowIcon(QIcon('data/sett.png'))
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
