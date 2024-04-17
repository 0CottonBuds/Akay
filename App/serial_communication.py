from serial import Serial
import time

class ArduinoSerialCommunication():
    arduino: Serial

    def __init__(self) -> None:
        self.arduino = Serial('COM10', 9600, timeout=2)

    def run(self, words):
        try:
            i = 0
            while i < len(words):
                self.arduino.write(bytes(words[i], "utf-8")+ b'\n') 
                response = self.arduino.read_until("\n")

                if response == b'':
                    print("empty")
                    continue
                elif response == b'next\n':
                    i += 1
                    # overflow protection
                    if i >= len(words):
                        i -= 1
                    print(f"self.arduino requested next word current word {words[i]}")
                    continue
                elif response == b'prev\n':
                    i -= 1
                    # underflow protection
                    if i < 0:
                        i += 1
                    print(f"self.arduino requested previous word current word {words[i]}")
                    continue
                elif response == b'end connection\n':
                    print("ending connection to arduino")
                    break

                print(response.strip())

        except KeyboardInterrupt:
            print("Program interrupted")

        self.arduino.write(b"end\n")
        response = self.arduino.read_until("\n")
        print(response.strip())

        # Close the serial connection
        self.arduino.close()

    
if __name__ == "__main__":
    com = ArduinoSerialCommunication()
    com.run(["hello"])