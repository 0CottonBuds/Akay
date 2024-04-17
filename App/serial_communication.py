from serial import Serial
from PySide6.QtCore import QObject, Slot, Signal, QRunnable

class ArduinoSerialCommunication(QObject):
    arduino: Serial
    start_translating = Signal(list[str])
    next_pressed = Signal()
    prev_pressed = Signal()
    words: list[str]
    index = 0

    def __init__(self, parent: QObject | None = ...) -> None:
        super().__init__(parent)
        self.arduino = Serial('COM10', 9600, timeout=2)
    
    def next_word(self):
        self.index += 1

    def prev_word(self):
        self.index -= 1
        
    @Slot() 
    def set_words(self, words):
        self.words = words

    @Slot()
    def run(self):
        try:
            self.index = 0
            while self.index < len(self.words) -1:
                self.arduino.write(bytes(self.words[self.index], "utf-8")+ b'\n') 
                response = self.arduino.read_until("\n")

                if response == b'':
                    print("empty")
                    continue
                elif response == b'next\n':
                    self.index += 1
                    # overflow protection
                    if self.index > len(self.words):
                        break
                    print(f"self.arduino requested next word current word {self.words[self.index]}")
                    self.next_pressed.emit()
                    continue
                elif response == b'prev\n':
                    self.index -= 1
                    # underflow protection
                    if self.index < 0:
                        self.index += 1
                    print(f"self.arduino requested previous word current word {self.words[self.index]}")
                    self.prev_pressed.emit()
                    continue
                elif response == b'end connection\n':
                    print("ending connection to arduino")
                    break

                print(response.strip())

        except KeyboardInterrupt:
            print("Program interrupted")
        
        except Exception:
            print("Something went wrong")

        self.arduino.write(b"end\n")
        response = self.arduino.read_until("\n")
        print(response.strip())

        # Close the serial connection
        self.arduino.close()
    
if __name__ == "__main__":
    com = ArduinoSerialCommunication(None)
    com.run(["hello"])