from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
import sqlite3


def load_sound(name):
    pygame.mixer.init()
    if not pygame.mixer or not pygame.mixer.get_init():
        pass
    try:
        sound = pygame.mixer.Sound(name)
    except pygame.error:
        print(f'Файл со звуком "{sound}" не найден')
    return sound


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(888, 650)
        mainWindow.setMinimumSize(QtCore.QSize(888, 650))
        mainWindow.setMaximumSize(QtCore.QSize(888, 650))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 898, 650))
        self.label.setMinimumSize(QtCore.QSize(898, 641))
        self.label.setMaximumSize(QtCore.QSize(898, 650))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("data/background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 891, 651))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("data/background1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 901, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("data/shelf.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 310, 901, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("data/shelf.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 65);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 180, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(73, 0, 21);")
        self.label_6.setObjectName("label_6")
        self.heart1 = QtWidgets.QLabel(self.centralwidget)
        self.heart1.setGeometry(QtCore.QRect(290, 120, 41, 91))
        self.heart1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heart1.setText("")
        self.heart1.setPixmap(QtGui.QPixmap("data/price.png"))
        self.heart1.setScaledContents(True)
        self.heart1.setObjectName("heart1")
        self.heart_all = QtWidgets.QLabel(self.centralwidget)
        self.heart_all.setGeometry(QtCore.QRect(550, 120, 51, 91))
        self.heart_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heart_all.setText("")
        self.heart_all.setPixmap(QtGui.QPixmap("data/price.png"))
        self.heart_all.setScaledContents(True)
        self.heart_all.setObjectName("heart_all")
        self.heart1_price = QtWidgets.QLabel(self.centralwidget)
        self.heart1_price.setGeometry(QtCore.QRect(298, 160, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.heart1_price.setFont(font)
        self.heart1_price.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heart1_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.heart1_price.setObjectName("heart1_price")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(270, 60, 71, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("data/heart.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(536, 60, 71, 51))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("data/heart.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.heart_all_price = QtWidgets.QLabel(self.centralwidget)
        self.heart_all_price.setGeometry(QtCore.QRect(559, 160, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.heart_all_price.setFont(font)
        self.heart_all_price.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.heart_all_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.heart_all_price.setObjectName("heart_all_price")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(290, 40, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(550, 40, 81, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(670, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.money = QtWidgets.QLabel(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(790, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.money.setFont(font)
        self.money.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.money.setStyleSheet("color: rgb(100, 0, 71);")
        self.money.setText("")
        self.money.setObjectName("money")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(548, 260, 91, 71))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("data/Screenshot_4.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(70, 260, 91, 71))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("data/Screenshot_5.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(645, 260, 91, 71))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("data/Screenshot_6.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(453, 260, 91, 71))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("data/Screenshot_7.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(167, 260, 91, 71))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("data/Screenshot_8.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(358, 260, 91, 71))
        self.label_25.setText("")
        self.label_25.setPixmap(QtGui.QPixmap("data/Screenshot_10.png"))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(262, 260, 91, 71))
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap("data/Screenshot_11.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(740, 260, 91, 71))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("data/Screenshot_12.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(90, 330, 51, 91))
        self.BG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BG.setText("")
        self.BG.setPixmap(QtGui.QPixmap("data/price.png"))
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.SO = QtWidgets.QLabel(self.centralwidget)
        self.SO.setGeometry(QtCore.QRect(190, 330, 51, 91))
        self.SO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SO.setText("")
        self.SO.setPixmap(QtGui.QPixmap("data/price.png"))
        self.SO.setScaledContents(True)
        self.SO.setObjectName("SO")
        self.BL = QtWidgets.QLabel(self.centralwidget)
        self.BL.setGeometry(QtCore.QRect(280, 330, 51, 91))
        self.BL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BL.setText("")
        self.BL.setPixmap(QtGui.QPixmap("data/price.png"))
        self.BL.setScaledContents(True)
        self.BL.setObjectName("BL")
        self.RB = QtWidgets.QLabel(self.centralwidget)
        self.RB.setGeometry(QtCore.QRect(380, 330, 51, 91))
        self.RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RB.setText("")
        self.RB.setPixmap(QtGui.QPixmap("data/price.png"))
        self.RB.setScaledContents(True)
        self.RB.setObjectName("RB")
        self.SNA = QtWidgets.QLabel(self.centralwidget)
        self.SNA.setGeometry(QtCore.QRect(480, 330, 51, 91))
        self.SNA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SNA.setText("")
        self.SNA.setPixmap(QtGui.QPixmap("data/price.png"))
        self.SNA.setScaledContents(True)
        self.SNA.setObjectName("SNA")
        self.DM = QtWidgets.QLabel(self.centralwidget)
        self.DM.setGeometry(QtCore.QRect(570, 330, 51, 91))
        self.DM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DM.setText("")
        self.DM.setPixmap(QtGui.QPixmap("data/price.png"))
        self.DM.setScaledContents(True)
        self.DM.setObjectName("DM")
        self.LEU = QtWidgets.QLabel(self.centralwidget)
        self.LEU.setGeometry(QtCore.QRect(670, 330, 51, 91))
        self.LEU.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LEU.setText("")
        self.LEU.setPixmap(QtGui.QPixmap("data/price.png"))
        self.LEU.setScaledContents(True)
        self.LEU.setObjectName("LEU")
        self.T = QtWidgets.QLabel(self.centralwidget)
        self.T.setGeometry(QtCore.QRect(770, 330, 51, 91))
        self.T.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.T.setText("")
        self.T.setPixmap(QtGui.QPixmap("data/price.png"))
        self.T.setScaledContents(True)
        self.T.setObjectName("T")
        self.BG_price = QtWidgets.QLabel(self.centralwidget)
        self.BG_price.setGeometry(QtCore.QRect(98, 370, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BG_price.setFont(font)
        self.BG_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BG_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.BG_price.setObjectName("BG_price")
        self.SO_price = QtWidgets.QLabel(self.centralwidget)
        self.SO_price.setGeometry(QtCore.QRect(198, 370, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SO_price.setFont(font)
        self.SO_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SO_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.SO_price.setObjectName("SO_price")
        self.DM_price = QtWidgets.QLabel(self.centralwidget)
        self.DM_price.setGeometry(QtCore.QRect(578, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DM_price.setFont(font)
        self.DM_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DM_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.DM_price.setObjectName("DM_price")
        self.BL_price = QtWidgets.QLabel(self.centralwidget)
        self.BL_price.setGeometry(QtCore.QRect(288, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BL_price.setFont(font)
        self.BL_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BL_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.BL_price.setObjectName("BL_price")
        self.LEU_price = QtWidgets.QLabel(self.centralwidget)
        self.LEU_price.setGeometry(QtCore.QRect(678, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LEU_price.setFont(font)
        self.LEU_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LEU_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.LEU_price.setObjectName("LEU_price")
        self.RB_price = QtWidgets.QLabel(self.centralwidget)
        self.RB_price.setGeometry(QtCore.QRect(388, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RB_price.setFont(font)
        self.RB_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RB_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.RB_price.setObjectName("RB_price")
        self.T_price = QtWidgets.QLabel(self.centralwidget)
        self.T_price.setGeometry(QtCore.QRect(778, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.T_price.setFont(font)
        self.T_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.T_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.T_price.setObjectName("T_price")
        self.SNA_price = QtWidgets.QLabel(self.centralwidget)
        self.SNA_price.setGeometry(QtCore.QRect(488, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SNA_price.setFont(font)
        self.SNA_price.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SNA_price.setStyleSheet("color: rgb(255, 0, 0);")
        self.SNA_price.setObjectName("SNA_price")
        self.BUY_BG = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_BG.setGeometry(QtCore.QRect(100, 370, 31, 51))
        self.BUY_BG.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_BG.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                  "")
        self.BUY_BG.setText("")
        self.BUY_BG.setCheckable(False)
        self.BUY_BG.setFlat(True)
        self.BUY_BG.setObjectName("BUY_BG")
        self.BUY_SO = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_SO.setGeometry(QtCore.QRect(200, 370, 31, 51))
        self.BUY_SO.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_SO.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                  "")
        self.BUY_SO.setText("")
        self.BUY_SO.setFlat(True)
        self.BUY_SO.setObjectName("BUY_SO")
        self.BUY_BL = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_BL.setGeometry(QtCore.QRect(290, 370, 31, 51))
        self.BUY_BL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_BL.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                  "")
        self.BUY_BL.setText("")
        self.BUY_BL.setFlat(True)
        self.BUY_BL.setObjectName("BUY_BL")
        self.BUY_RB = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_RB.setGeometry(QtCore.QRect(390, 370, 31, 51))
        self.BUY_RB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_RB.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                  "")
        self.BUY_RB.setText("")
        self.BUY_RB.setFlat(True)
        self.BUY_RB.setObjectName("BUY_RB")
        self.BUY_SNA = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_SNA.setGeometry(QtCore.QRect(490, 370, 31, 51))
        self.BUY_SNA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_SNA.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "")
        self.BUY_SNA.setText("")
        self.BUY_SNA.setFlat(True)
        self.BUY_SNA.setObjectName("BUY_SNA")
        self.BUY_DM = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_DM.setGeometry(QtCore.QRect(580, 370, 31, 51))
        self.BUY_DM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_DM.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                  "")
        self.BUY_DM.setText("")
        self.BUY_DM.setFlat(True)
        self.BUY_DM.setObjectName("BUY_DM")
        self.BUY_LEU = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_LEU.setGeometry(QtCore.QRect(680, 370, 31, 51))
        self.BUY_LEU.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_LEU.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "")
        self.BUY_LEU.setText("")
        self.BUY_LEU.setFlat(True)
        self.BUY_LEU.setObjectName("BUY_LEU")
        self.BUY_T = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_T.setGeometry(QtCore.QRect(780, 370, 31, 51))
        self.BUY_T.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_T.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                 "")
        self.BUY_T.setText("")
        self.BUY_T.setFlat(True)
        self.BUY_T.setObjectName("BUY_T")
        self.BUY_HEART1 = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_HEART1.setGeometry(QtCore.QRect(295, 160, 31, 51))
        self.BUY_HEART1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_HEART1.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "")
        self.BUY_HEART1.setText("")
        self.BUY_HEART1.setFlat(True)
        self.BUY_HEART1.setObjectName("BUY_HEART1")
        self.BUY_HEARTALL = QtWidgets.QPushButton(self.centralwidget)
        self.BUY_HEARTALL.setGeometry(QtCore.QRect(560, 160, 31, 51))
        self.BUY_HEARTALL.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BUY_HEARTALL.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);\n"
            "")
        self.BUY_HEARTALL.setText("")
        self.BUY_HEARTALL.setFlat(True)
        self.BUY_HEARTALL.setObjectName("BUY_HEARTALL")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.heart1.raise_()
        self.heart_all.raise_()
        self.heart1_price.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.heart_all_price.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.money.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.BG.raise_()
        self.SO.raise_()
        self.BL.raise_()
        self.RB.raise_()
        self.SNA.raise_()
        self.DM.raise_()
        self.LEU.raise_()
        self.T.raise_()
        self.BG_price.raise_()
        self.SO_price.raise_()
        self.DM_price.raise_()
        self.BL_price.raise_()
        self.LEU_price.raise_()
        self.RB_price.raise_()
        self.T_price.raise_()
        self.SNA_price.raise_()
        self.BUY_BG.raise_()
        self.BUY_SO.raise_()
        self.BUY_BL.raise_()
        self.BUY_RB.raise_()
        self.BUY_SNA.raise_()
        self.BUY_DM.raise_()
        self.BUY_LEU.raise_()
        self.BUY_T.raise_()
        self.BUY_HEART1.raise_()
        self.BUY_HEARTALL.raise_()
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Магазин"))
        self.label_5.setText(_translate("mainWindow", "ЖИЗНИ "))
        self.label_6.setText(_translate("mainWindow", "ПЕСНИ"))
        self.heart1_price.setText(_translate("mainWindow", "50"))
        self.heart_all_price.setText(_translate("mainWindow", "200"))
        self.label_13.setText(_translate("mainWindow", "+1"))
        self.label_14.setText(_translate("mainWindow", "ВСЕ"))
        self.label_15.setText(_translate("mainWindow", "БАЛАНС:"))
        self.BG_price.setText(_translate("mainWindow", "200"))
        self.SO_price.setText(_translate("mainWindow", "100"))
        self.DM_price.setText(_translate("mainWindow", "500"))
        self.BL_price.setText(_translate("mainWindow", "400"))
        self.LEU_price.setText(_translate("mainWindow", "450"))
        self.RB_price.setText(_translate("mainWindow", "400"))
        self.T_price.setText(_translate("mainWindow", "250"))
        self.SNA_price.setText(_translate("mainWindow", "250"))

    def DM_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Dance Monkey'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 500:
                a = money[0]
                self.money.setText(str(a))
                a -= 500
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Dance Monkey' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def T_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Thunder'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 250:
                a = money[0]
                self.money.setText(str(a))
                a -= 250
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Thunder' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def SO_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Stressed Out'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 100:
                a = money[0]
                self.money.setText(str(a))
                a -= 100
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Stressed Out' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def BG_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Bad Guy'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 200:
                a = money[0]
                self.money.setText(str(a))
                a -= 200
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Bad Guy' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def BL_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Blinding Lights'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 400:
                a = money[0]
                self.money.setText(str(a))
                a -= 400
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Blinding Lights' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def RB_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Runaway Baby'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 400:
                a = money[0]
                self.money.setText(str(a))
                a -= 400
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Runaway Baby' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def SNA_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'Seven Nation Army'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 250:
                a = money[0]
                self.money.setText(str(a))
                a -= 250
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'Seven Nation Army' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def LEU_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()
        clock = sql.execute(
            """SELECT open FROM songs WHERE 
            name = 'My Songs Know What You Did In The Dark'""").fetchone()
        if clock[0] == 1 or clock[0] == '1':
            a = load_sound('data/песня_закрыта.mp3')
            a.play()
        else:
            money = sql.execute(
                """SELECT money FROM data""").fetchone()
            if money[0] >= 450:
                a = money[0]
                self.money.setText(str(a))
                a -= 450
                sql.execute(f'UPDATE data SET money = {a}')
                self.money.setText(str(a))
                a = load_sound('data/покупка.mp3')
                a.play()
                sql.execute(
                    """UPDATE songs SET open = 1
                     WHERE name = 'My Songs Know What You Did In The Dark' """)
                db.commit()
            else:
                a = load_sound('data/песня_закрыта.mp3')
                a.play()

    def lives_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()

        money = sql.execute(
            """SELECT money FROM data""").fetchone()
        lives = sql.execute(
            """SELECT lives FROM data""").fetchone()
        if money[0] >= 50 and lives[0] < 5:
            a = money[0]
            b = lives[0]
            self.money.setText(str(a))
            b += 1
            a -= 50
            sql.execute(f'UPDATE data SET money = {a}')
            sql.execute(f'UPDATE data SET lives = {b}')
            db.commit()
            self.money.setText(str(a))
            a = load_sound('data/покупка.mp3')
            a.play()
        else:
            a = load_sound('data/песня_закрыта.mp3')
            a.play()

    def alllives_buying(self):
        db = sqlite3.connect('data/base.db')
        sql = db.cursor()

        money = sql.execute(
            """SELECT money FROM data""").fetchone()
        lives = sql.execute(
            """SELECT lives FROM data""").fetchone()
        if money[0] >= 200 and lives[0] == 0:
            a = money[0]
            b = lives[0]
            self.money.setText(str(a))
            b += 5
            a -= 200
            sql.execute(f'UPDATE data SET money = {a}')
            sql.execute(f'UPDATE data SET lives = {b}')
            db.commit()
            self.money.setText(str(a))
            a = load_sound('data/покупка.mp3')
            a.play()
        else:
            a = load_sound('data/песня_закрыта.mp3')
            a.play()

    def buy_connect(self):
        self.BUY_DM.clicked.connect(self.DM_buying)
        self.BUY_T.clicked.connect(self.T_buying)
        self.BUY_BG.clicked.connect(self.BG_buying)
        self.BUY_SO.clicked.connect(self.SO_buying)
        self.BUY_BL.clicked.connect(self.BL_buying)
        self.BUY_RB.clicked.connect(self.RB_buying)
        self.BUY_SNA.clicked.connect(self.SNA_buying)
        self.BUY_LEU.clicked.connect(self.LEU_buying)
        self.BUY_HEART1.clicked.connect(self.lives_buying)
        self.BUY_HEARTALL.clicked.connect(self.alllives_buying)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    ui.buy_connect()
    mainWindow.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
