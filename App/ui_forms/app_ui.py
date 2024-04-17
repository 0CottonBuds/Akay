# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.app_router = QStackedWidget(self.centralwidget)
        self.app_router.setObjectName(u"app_router")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.main_page.setStyleSheet(u"background-color:rgb(255, 255, 127)")
        self.verticalLayout_3 = QVBoxLayout(self.main_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_page_header = QWidget(self.main_page)
        self.main_page_header.setObjectName(u"main_page_header")
        self.header_name = QLabel(self.main_page_header)
        self.header_name.setObjectName(u"header_name")
        self.header_name.setGeometry(QRect(130, 10, 111, 71))
        font = QFont()
        font.setPointSize(28)
        self.header_name.setFont(font)
        self.settings_button = QPushButton(self.main_page_header)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(290, 40, 75, 24))

        self.verticalLayout_3.addWidget(self.main_page_header)

        self.main_page_main = QWidget(self.main_page)
        self.main_page_main.setObjectName(u"main_page_main")
        self.plain_text_input = QTextEdit(self.main_page_main)
        self.plain_text_input.setObjectName(u"plain_text_input")
        self.plain_text_input.setGeometry(QRect(0, 0, 381, 131))
        self.translate_button = QPushButton(self.main_page_main)
        self.translate_button.setObjectName(u"translate_button")
        self.translate_button.setGeometry(QRect(30, 150, 75, 24))
        self.pushButton_2 = QPushButton(self.main_page_main)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 150, 75, 24))

        self.verticalLayout_3.addWidget(self.main_page_main)

        self.main_page_main2 = QWidget(self.main_page)
        self.main_page_main2.setObjectName(u"main_page_main2")

        self.verticalLayout_3.addWidget(self.main_page_main2)

        self.app_router.addWidget(self.main_page)
        self.translation_page = QWidget()
        self.translation_page.setObjectName(u"translation_page")
        self.verticalLayout_4 = QVBoxLayout(self.translation_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.translation_page_header = QWidget(self.translation_page)
        self.translation_page_header.setObjectName(u"translation_page_header")
        self.settings_button_2 = QPushButton(self.translation_page_header)
        self.settings_button_2.setObjectName(u"settings_button_2")
        self.settings_button_2.setGeometry(QRect(270, 50, 75, 24))
        self.header_name_2 = QLabel(self.translation_page_header)
        self.header_name_2.setObjectName(u"header_name_2")
        self.header_name_2.setGeometry(QRect(120, 20, 111, 71))
        self.header_name_2.setFont(font)
        self.translation_page_back_button = QPushButton(self.translation_page_header)
        self.translation_page_back_button.setObjectName(u"translation_page_back_button")
        self.translation_page_back_button.setGeometry(QRect(20, 50, 75, 24))

        self.verticalLayout_4.addWidget(self.translation_page_header)

        self.translation_page_main = QWidget(self.translation_page)
        self.translation_page_main.setObjectName(u"translation_page_main")
        self.text_to_translate = QLabel(self.translation_page_main)
        self.text_to_translate.setObjectName(u"text_to_translate")
        self.text_to_translate.setGeometry(QRect(140, 40, 81, 16))
        self.braile_translation = QLabel(self.translation_page_main)
        self.braile_translation.setObjectName(u"braile_translation")
        self.braile_translation.setGeometry(QRect(120, 90, 111, 20))

        self.verticalLayout_4.addWidget(self.translation_page_main)

        self.translation_page_main2 = QWidget(self.translation_page)
        self.translation_page_main2.setObjectName(u"translation_page_main2")
        self.pushButton_3 = QPushButton(self.translation_page_main2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(140, 70, 75, 24))

        self.verticalLayout_4.addWidget(self.translation_page_main2)

        self.app_router.addWidget(self.translation_page)

        self.verticalLayout_2.addWidget(self.app_router)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.app_router.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.header_name.setText(QCoreApplication.translate("MainWindow", u"AKAY", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.translate_button.setText(QCoreApplication.translate("MainWindow", u"translate", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"more input", None))
        self.settings_button_2.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.header_name_2.setText(QCoreApplication.translate("MainWindow", u"AKAY", None))
        self.translation_page_back_button.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.text_to_translate.setText(QCoreApplication.translate("MainWindow", u"CurrentText", None))
        self.braile_translation.setText(QCoreApplication.translate("MainWindow", u"Braille substitution", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"next", None))
    # retranslateUi

