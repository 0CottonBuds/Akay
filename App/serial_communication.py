from serial import Serial
import time

ser = Serial('COM10', 9600, timeout=2)
dummy_data = ['110010100010111000111000101010', '011110100010001100', '110010100010111000111000101010']
try:
    while True:
        i = 0
        ser.write(dummy_data[i].encode())
        while i >= len(dummy_data):
            ser.write(dummy_data[i].encode())
            response = ser.readline().decode('utf-8').strip()
            print("arduino n or p", response)

            if response == "next":
                i += 1
            else:
                i -= 1
        ser.write(b"end")
            
        # Wait for a moment before sending the next command
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Program interrupted")

# Close the serial connection
ser.close()