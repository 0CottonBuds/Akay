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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

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
        self.main_page_header.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.main_page_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.main_page_header)
        self.widget.setObjectName(u"widget")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 75, 24))

        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.main_page_header)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.header_name = QLabel(self.widget_2)
        self.header_name.setObjectName(u"header_name")
        font = QFont()
        font.setPointSize(28)
        self.header_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.header_name)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.main_page_header)
        self.widget_3.setObjectName(u"widget_3")
        self.settings_button = QPushButton(self.widget_3)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(20, 20, 75, 24))

        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.main_page_header)

        self.main_page_main = QWidget(self.main_page)
        self.main_page_main.setObjectName(u"main_page_main")
        self.verticalLayout_5 = QVBoxLayout(self.main_page_main)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.plain_text_input = QTextEdit(self.main_page_main)
        self.plain_text_input.setObjectName(u"plain_text_input")
        self.plain_text_input.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_5.addWidget(self.plain_text_input)

        self.widget_4 = QWidget(self.main_page_main)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.translate_button = QPushButton(self.widget_4)
        self.translate_button.setObjectName(u"translate_button")
        self.translate_button.setMinimumSize(QSize(0, 64))
        self.translate_button.setStyleSheet(u"border-radius: 20px")

        self.horizontalLayout_3.addWidget(self.translate_button)

        self.more_input_button = QPushButton(self.widget_4)
        self.more_input_button.setObjectName(u"more_input_button")
        self.more_input_button.setMaximumSize(QSize(16777215, 64))

        self.horizontalLayout_3.addWidget(self.more_input_button)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.verticalSpacer_2 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.main_page_main)

        self.main_page_main2 = QWidget(self.main_page)
        self.main_page_main2.setObjectName(u"main_page_main2")
        self.main_page_main2.setMinimumSize(QSize(0, 75))
        self.main_page_main2.setMaximumSize(QSize(16777215, 75))
        self.label = QLabel(self.main_page_main2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 60, 211, 16))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(7)
        font1.setItalic(True)
        self.label.setFont(font1)

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
        self.next_word_button = QPushButton(self.translation_page_main2)
        self.next_word_button.setObjectName(u"next_word_button")
        self.next_word_button.setGeometry(QRect(140, 70, 75, 24))

        self.verticalLayout_4.addWidget(self.translation_page_main2)

        self.app_router.addWidget(self.translation_page)
        self.more_input_page = QWidget()
        self.more_input_page.setObjectName(u"more_input_page")
        self.verticalLayout = QVBoxLayout(self.more_input_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.more_input_header = QWidget(self.more_input_page)
        self.more_input_header.setObjectName(u"more_input_header")

        self.verticalLayout.addWidget(self.more_input_header)

        self.more_input_main = QWidget(self.more_input_page)
        self.more_input_main.setObjectName(u"more_input_main")

        self.verticalLayout.addWidget(self.more_input_main)

        self.more_input_main2 = QWidget(self.more_input_page)
        self.more_input_main2.setObjectName(u"more_input_main2")

        self.verticalLayout.addWidget(self.more_input_main2)

        self.app_router.addWidget(self.more_input_page)

        self.verticalLayout_2.addWidget(self.app_router)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.app_router.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.header_name.setText(QCoreApplication.translate("MainWindow", u"AKAY", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.plain_text_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert Text here", None))
        self.translate_button.setText(QCoreApplication.translate("MainWindow", u"translate", None))
        self.more_input_button.setText(QCoreApplication.translate("MainWindow", u"more input", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Made by Ndstoc - Innolympics 2024", None))
        self.settings_button_2.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.header_name_2.setText(QCoreApplication.translate("MainWindow", u"AKAY", None))
        self.translation_page_back_button.setText(QCoreApplication.translate("MainWindow", u"back", None))
        self.text_to_translate.setText(QCoreApplication.translate("MainWindow", u"CurrentText", None))
        self.braile_translation.setText(QCoreApplication.translate("MainWindow", u"Braille substitution", None))
        self.next_word_button.setText(QCoreApplication.translate("MainWindow", u"next", None))
    # retranslateUi

