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
import ui_forms.icons_rc_rc

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
        self.main_page.setStyleSheet(u"background-color:rgb(245, 205, 167)")
        self.verticalLayout_3 = QVBoxLayout(self.main_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_page_header = QWidget(self.main_page)
        self.main_page_header.setObjectName(u"main_page_header")
        self.main_page_header.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(self.main_page_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.main_page_header)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.settings_button_3 = QPushButton(self.widget)
        self.settings_button_3.setObjectName(u"settings_button_3")
        self.settings_button_3.setStyleSheet(u"border: 0;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button_3.setIcon(icon)
        self.settings_button_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.settings_button_3)

        self.widget_16 = QWidget(self.widget)
        self.widget_16.setObjectName(u"widget_16")

        self.horizontalLayout_11.addWidget(self.widget_16)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.main_page_header)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.header_name = QLabel(self.widget_2)
        self.header_name.setObjectName(u"header_name")
        font = QFont()
        font.setFamilies([u"Maiandra GD"])
        font.setPointSize(28)
        self.header_name.setFont(font)

        self.horizontalLayout_2.addWidget(self.header_name)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.main_page_header)
        self.widget_3.setObjectName(u"widget_3")

        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.main_page_header)

        self.main_page_main = QWidget(self.main_page)
        self.main_page_main.setObjectName(u"main_page_main")
        self.verticalLayout_5 = QVBoxLayout(self.main_page_main)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.plain_text_input = QTextEdit(self.main_page_main)
        self.plain_text_input.setObjectName(u"plain_text_input")
        self.plain_text_input.setMaximumSize(QSize(16777215, 100))
        self.plain_text_input.setStyleSheet(u"border-radius: 10px;\n"
"background-color:rgb(220, 219, 168)")

        self.verticalLayout_5.addWidget(self.plain_text_input)

        self.widget_4 = QWidget(self.main_page_main)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 0, 4, 4)
        self.translate_button = QPushButton(self.widget_4)
        self.translate_button.setObjectName(u"translate_button")
        self.translate_button.setMinimumSize(QSize(0, 64))
        self.translate_button.setStyleSheet(u"border-radius: 25px;\n"
"background-color:rgb(245, 205, 167);\n"
"border-color: rgb(0,0,0);\n"
"border-width : 1px;\n"
"border-style:solid")

        self.horizontalLayout_3.addWidget(self.translate_button)

        self.more_input_button = QPushButton(self.widget_4)
        self.more_input_button.setObjectName(u"more_input_button")
        self.more_input_button.setMaximumSize(QSize(52, 64))
        self.more_input_button.setStyleSheet(u"border-radius: 25px;\n"
"background-color: rgb(196, 219, 255)")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/photo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.more_input_button.setIcon(icon1)

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
        self.translation_page.setStyleSheet(u"background-color:rgb(245, 205, 167)")
        self.verticalLayout_4 = QVBoxLayout(self.translation_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.translation_page_header = QWidget(self.translation_page)
        self.translation_page_header.setObjectName(u"translation_page_header")
        self.translation_page_header.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_5 = QHBoxLayout(self.translation_page_header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_5 = QWidget(self.translation_page_header)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.translation_page_back_button = QPushButton(self.widget_5)
        self.translation_page_back_button.setObjectName(u"translation_page_back_button")
        self.translation_page_back_button.setMinimumSize(QSize(0, 2))
        self.translation_page_back_button.setMaximumSize(QSize(16777215, 40))
        self.translation_page_back_button.setStyleSheet(u"border: 0px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/3114883.png", QSize(), QIcon.Normal, QIcon.Off)
        self.translation_page_back_button.setIcon(icon2)
        self.translation_page_back_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.translation_page_back_button)

        self.widget_14 = QWidget(self.widget_5)
        self.widget_14.setObjectName(u"widget_14")

        self.horizontalLayout_9.addWidget(self.widget_14)


        self.horizontalLayout_5.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.translation_page_header)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.header_name_2 = QLabel(self.widget_6)
        self.header_name_2.setObjectName(u"header_name_2")
        self.header_name_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.header_name_2)


        self.horizontalLayout_5.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.translation_page_header)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.widget_15 = QWidget(self.widget_7)
        self.widget_15.setObjectName(u"widget_15")

        self.horizontalLayout_10.addWidget(self.widget_15)

        self.settings_button_2 = QPushButton(self.widget_7)
        self.settings_button_2.setObjectName(u"settings_button_2")
        self.settings_button_2.setStyleSheet(u"border: 0;")
        self.settings_button_2.setIcon(icon)
        self.settings_button_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.settings_button_2)


        self.horizontalLayout_5.addWidget(self.widget_7)


        self.verticalLayout_4.addWidget(self.translation_page_header)

        self.translation_page_main = QWidget(self.translation_page)
        self.translation_page_main.setObjectName(u"translation_page_main")
        self.verticalLayout_6 = QVBoxLayout(self.translation_page_main)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_8 = QWidget(self.translation_page_main)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.text_to_translate = QLabel(self.widget_8)
        self.text_to_translate.setObjectName(u"text_to_translate")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.text_to_translate.setFont(font2)
        self.text_to_translate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.text_to_translate)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.translation_page_main)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.braile_translation = QLabel(self.widget_9)
        self.braile_translation.setObjectName(u"braile_translation")
        self.braile_translation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.braile_translation)


        self.verticalLayout_6.addWidget(self.widget_9)


        self.verticalLayout_4.addWidget(self.translation_page_main)

        self.translation_page_main2 = QWidget(self.translation_page)
        self.translation_page_main2.setObjectName(u"translation_page_main2")
        self.translation_page_main2.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_8 = QVBoxLayout(self.translation_page_main2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_10 = QWidget(self.translation_page_main2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.prev_word_button = QPushButton(self.widget_12)
        self.prev_word_button.setObjectName(u"prev_word_button")
        self.prev_word_button.setMaximumSize(QSize(16777215, 52))
        self.prev_word_button.setStyleSheet(u"border-radius: 25px;\n"
"background-color:rgb(250, 190, 152);\n"
"border-color: rgb(0,0,0);\n"
"border-width : 1px;\n"
"border-style:solid")
        self.prev_word_button.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.prev_word_button)

        self.next_word_button = QPushButton(self.widget_12)
        self.next_word_button.setObjectName(u"next_word_button")
        self.next_word_button.setMaximumSize(QSize(16777215, 52))
        self.next_word_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.next_word_button.setStyleSheet(u"border-radius: 25px;\n"
"background-color:rgb(201, 219, 186);\n"
"border-color: rgb(0,0,0);\n"
"border-width : 1px;\n"
"border-style:solid")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_word_button.setIcon(icon3)

        self.horizontalLayout_8.addWidget(self.next_word_button)


        self.horizontalLayout_7.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_10)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.widget_13)


        self.verticalLayout_8.addWidget(self.widget_10)

        self.verticalSpacer_4 = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


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
        self.settings_button_3.setText("")
        self.header_name.setText(QCoreApplication.translate("MainWindow", u"AKAY", None))
        self.plain_text_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert Text here", None))
        self.translate_button.setText(QCoreApplication.translate("MainWindow", u"translate", None))
        self.more_input_button.setText(QCoreApplication.translate("MainWindow", u"Img", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Made by Ndstoc - Innolympics 2024", None))
        self.translation_page_back_button.setText("")
        self.header_name_2.setText(QCoreApplication.translate("MainWindow", u"AKAY", None))
        self.settings_button_2.setText("")
        self.text_to_translate.setText(QCoreApplication.translate("MainWindow", u"CurrentText", None))
        self.braile_translation.setText(QCoreApplication.translate("MainWindow", u"Braille substitution", None))
        self.prev_word_button.setText(QCoreApplication.translate("MainWindow", u"prev", None))
        self.next_word_button.setText(QCoreApplication.translate("MainWindow", u"next", None))
    # retranslateUi

