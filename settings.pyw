from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3
import time
import os


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
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label = QtWidgets.QLabel(self.Settings_2)
        self.label.setGeometry(QtCore.QRect(10, 130, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.Settings_2)
        self.pushButton.setGeometry(QtCore.QRect(400, 140, 60, 27))
        self.pushButton.clicked.connect(self.reset_game)
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
        self.label.raise_()
        self.pushButton.raise_()
        Settings.setCentralWidget(self.Settings_2)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Настройки"))
        self.text.setText(_translate("Settings", "Громкость"))
        self.label.setText(_translate("Settings",
                                      "Вы уверены? Все настройки и прогресс"
                                      " будут удалены!"))
        self.pushButton.setText(_translate("Settings", "Сброс"))

    def look(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        value = sql.execute(
            """SELECT volume FROM data""").fetchone()
        value = value[0]
        self.slider.setValue(value)
        self.slider.valueChanged.connect(self.changevalue)

    def changevalue(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        cvalue = self.slider.value()
        sql.execute(f"""UPDATE data SET volume = {cvalue}""")
        db.commit()

    def reset_game(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        sql.execute(f"""UPDATE data SET volume = 100""").fetchone()
        sql.execute(f"""UPDATE data SET lives = 5""").fetchone()
        sql.execute(f"""UPDATE data SET money = 200""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'Bad Guy'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'Dance Monkey'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'Blinding Lights'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'My Songs Know What You Did In The Dark'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'Seven Nation Army'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'Runaway Baby'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name =
             'Stressed Out'""").fetchone()
        sql.execute(
            f"""UPDATE songs SET open = 0 WHERE name = 'Thunder'""").fetchone()
        db.commit()
        db.close()
        sys.exit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QMainWindow()
    Settings.setWindowIcon(QIcon('data/sett.png'))
    ui = Ui_Settings()
    ui.setupUi(Settings)
    ui.look()
    Settings.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
