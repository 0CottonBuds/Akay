from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow 
from PySide6.QtCore import QObject
from ui_forms.app_ui import Ui_MainWindow
from brailly_translator import grade1_braille_translation, grade2_braille_translate

class App(): 
    Q_app: QApplication
    ui : Ui_MainWindow
    current_text: str
    current_translated_text: str
    current_word_index: int

    def __init__(self) -> None:
        self.Q_app = QApplication()
        main_window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(main_window)
        # connect to com serial port 

        self.current_text = ""
        self.current_word_index = 0 

        self.ui.translate_button.clicked.connect(self.translate)
        self.ui.translation_page_back_button.clicked.connect(self.move_to_main_page)
        self.ui.next_word_button.clicked.connect(self.translate_next_word)
        
        main_window.show()

        self.Q_app.exec()

    def translate(self):
        self.move_to_translation_page()
        self.current_text = self.ui.plain_text_input.toPlainText()
        self.current_translated_text = grade2_braille_translate(self.current_text)
        self.current_text = self.ui.plain_text_input.toPlainText().split()
        self.current_word_index = 0 
        self.ui.text_to_translate.setText(self.current_text[self.current_word_index])
        self.ui.braile_translation.setText(self.current_translated_text[self.current_word_index])
        print(self.current_text)
        print(self.current_translated_text)
        #serial send word here
    
    def translate_next_word(self):
        if self.current_word_index + 2 > len(self.current_text):
            self.move_to_main_page()
            return
        self.current_word_index += 1 
        self.ui.text_to_translate.setText(self.current_text[self.current_word_index])
        self.ui.braile_translation.setText(self.current_translated_text[self.current_word_index])
        #serial send word here

    def move_to_translation_page(self):
        self.ui.app_router.setCurrentWidget(self.ui.translation_page)
    def move_to_main_page(self):
        self.ui.app_router.setCurrentWidget(self.ui.main_page)

if __name__ == "__main__":
    app = App()
    pass