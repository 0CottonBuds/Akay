from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow 
from PySide6.QtCore import QObject
from ui_forms.app_ui import Ui_MainWindow
from brailly_translator import grade1_braille_translation, grade2_braille_translate

class App(): 
    Q_app: QApplication
    ui : Ui_MainWindow

    def __init__(self) -> None:

        self.Q_app = QApplication()
        main_window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(main_window)

        self.ui.translate_button.clicked.connect(self.translate)
        self.ui.translation_page_back_button.clicked.connect(self.move_to_main_page)
        
        main_window.show()

        self.Q_app.exec()

    def translate(self):
        self.move_to_translation_page()
        current_text = self.ui.plain_text_input.toPlainText()
        self.ui.text_to_translate.setText(current_text)
        self.ui.braile_translation.setText(grade2_braille_translate(current_text))

    def move_to_translation_page(self):
        self.ui.app_router.setCurrentWidget(self.ui.translation_page)
    def move_to_main_page(self):
        self.ui.app_router.setCurrentWidget(self.ui.main_page)



if __name__ == "__main__":
    app = App()
    pass