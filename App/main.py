from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow 
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QObject, QThread, Signal
from ui_forms.app_ui import Ui_MainWindow
from brailly_translator import grade1_braille_translation, grade2_braille_translate
from text_extraction import image_to_text
from serial_communication import ArduinoSerialCommunication

class App(): 
    Q_app: QApplication
    ui : Ui_MainWindow
    arduino_communication_worker: ArduinoSerialCommunication
    communication_thread = QThread
    current_text: str
    current_translated_text: str
    current_word_index: int


    def __init__(self) -> None:
        self.Q_app = QApplication()
        main_window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(main_window)

        self.communication_thread = QThread()
        self.arduino_communication_worker = ArduinoSerialCommunication(None)
        self.arduino_communication_worker.moveToThread(self.communication_thread)
        self.communication_thread.finished.connect(self.communication_thread.deleteLater)
        self.communication_thread.start()

        self.arduino_communication_worker.start_translating.connect(self.arduino_communication_worker.run)

        self.arduino_communication_worker.next_pressed.connect(self.translate_next_word)
        self.arduino_communication_worker.prev_pressed.connect(self.translate_previous_word)

    
        #QFile dialog
        file_dialog = QFileDialog(self.ui.main_page_main2)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg)")


        # connect to com serial port 

        self.current_text = ""
        self.current_word_index = 0 

        self.ui.translate_button.clicked.connect(self.translate_plain_text)
        self.ui.translation_page_back_button.clicked.connect(self.move_to_main_page)
        self.ui.next_word_button.clicked.connect(self.next_button)
        self.ui.more_input_button.clicked.connect(self.select_other_input)
        
        main_window.show()

        self.Q_app.exec()
    


    def translate(self):
        self.move_to_translation_page()
        self.current_translated_text = grade2_braille_translate(self.current_text)
        self.current_text = self.ui.plain_text_input.toPlainText().split()
        self.current_word_index = 0 

        self.arduino_communication_worker.set_words(self.current_translated_text)
        self.arduino_communication_worker.start_translating.emit()

        self.ui.text_to_translate.setText(self.current_text[self.current_word_index])
        self.ui.braile_translation.setText(self.current_translated_text[self.current_word_index])
        print(self.current_text)
        print(self.current_translated_text)

    def translate_plain_text(self):
        self.current_text = self.ui.plain_text_input.toPlainText()

        if self.current_text.strip() == "":
            return

        self.translate()
        #serial send word here
    
    def translate_image(self, image_path):
        self.current_text = image_to_text(image_path) 
        self.current_translated_text = grade2_braille_translate(self.current_text)

        self.translate()

   
    def translate_next_word(self):
        if self.current_word_index + 2 > len(self.current_text):
            self.move_to_main_page()
            self.ui.plain_text_input.setText("")
            return
        self.current_word_index += 1 
        self.ui.text_to_translate.setText(self.current_text[self.current_word_index])
        self.ui.braile_translation.setText(self.current_translated_text[self.current_word_index])
        #serial send word here

    def translate_previous_word(self):
        if self.current_word_index -1 < 0:
            self.move_to_main_page()
            self.ui.plain_text_input.setText("")
            return
        self.current_word_index -= 1 
        self.ui.text_to_translate.setText(self.current_text[self.current_word_index])
        self.ui.braile_translation.setText(self.current_translated_text[self.current_word_index])
        #serial send word here

    def next_button(self):
        self.arduino_communication_worker.index += 1
        self.translate_next_word()

    def select_other_input(self):
        image_path, filter_ = QFileDialog.getOpenFileName(None, "Open file", "./", "Images (*.png *.xpm *.jpg)")
        self.translate_image(image_path)

    def move_to_translation_page(self):
        self.ui.app_router.setCurrentWidget(self.ui.translation_page)
    def move_to_main_page(self):
        self.ui.app_router.setCurrentWidget(self.ui.main_page)

if __name__ == "__main__":
    app = App()
    pass