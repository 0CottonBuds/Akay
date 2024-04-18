#include <Servo.h>
#include <Arduino.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

void cutString(String inputString, String stringArray[], int& numStrings) {
  int stringLength = inputString.length();
  for (int i = 0; i < stringLength; i += 6) {
    // Get the next 6 characters or remaining characters
    String cutString = inputString.substring(i, min(i + 6, stringLength));
    
    // Check if there's space in the array and cut string is 6 characters
    if (numStrings < 6 && cutString.length() == 6) {
      stringArray[numStrings] = cutString;
      numStrings++;
    }
  }
}

void setup() {
  servo1.attach(2);
  servo2.attach(4);
  servo3.attach(7);
  servo4.attach(8);
  servo5.attach(12);
  servo6.attach(13);
  Serial.begin(9600);
}

void loop() {

  // Define string (replace with user input if needed)
  String userInput = "100000110000100100100110100010110100";
  
  // String array
  String stringArray[6];
  int numStrings = 0; // Keep track of filled elements

  // Cut and add to string array
  cutString(userInput, stringArray, numStrings);

  // Print strings (optional, modify as needed)
  Serial.println("Cut Strings:");
  for (int i = 0; i < numStrings; i++) {
    Serial.println(stringArray[i]);
  }

  int stringNum = sizeof(stringArray) / sizeof(stringArray[0]); // Get number of strings

  for (int i = 0; i < stringNum; i++) {
    String currentString = stringArray[i];
    int stringLength = currentString.length() + 1;
    char charArray[stringLength];

    // Convert string to character array
    currentString.toCharArray(charArray, stringLength);
    servo1.write(90);
    servo2.write(90);
    servo3.write(90);
    servo4.write(90);
    servo5.write(90);
    servo6.write(90);
    servo6.write(90);
    delay(100);

    for (int i = 0; i < stringLength; i++) {
      Serial.print(charArray[i]);
      if (charArray[0]=='1'){
        servo1.write(60);
      }
      if (charArray[1]=='1'){
        servo2.write(60);
      }
      if (charArray[2]=='1'){
        servo3.write(60);
      }
      if (charArray[3]=='1'){
        servo4.write(60);
      }
      if (charArray[4]=='1'){
        servo5.write(60);
      }
      if (charArray[5]=='1'){
        servo6.write(60);
      }
    }
    delay(500);
    Serial.println();
  }

}