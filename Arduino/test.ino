#include <Servo.h>
#include <Arduino.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

bool butt_5_is_pressed = false; 
bool butt_6_is_pressed = false; 

String currentWord;

void setup() {
  servo1.attach(2);
  servo2.attach(4);
  servo3.attach(7);
  servo4.attach(8);
  servo5.attach(12);
  servo6.attach(13);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  Serial.begin(9600);

  currentWord = " ";
}

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

void display_braille(String currentWord){
  
  // Define string (replace with user input if needed)
  String userInput = currentWord; 
  
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
  } 
}

void loop() {
  // if there is bytes in the serial
  if(Serial.available() > 0){
    String data = Serial.readStringUntil("\n");

    if(data == "end\n"){
      Serial.print("end connection\n");
    }
    else{
      if (digitalRead(5) == 0 || digitalRead(6) == 0){
          Serial.println("Button Pressed");
          if (digitalRead(5) == 0){
            butt_5_is_pressed = true;
              if (butt_5_is_pressed == true){
                Serial.println("next\n");
              }
            }

          //previous button change the condition here for button input
          if (digitalRead(6) == 0){
            butt_6_is_pressed = true;
            if (butt_6_is_pressed == true){
              Serial.println("prev\n");
            }
            
          }
          servo1.write(90);
          servo2.write(90);
          servo3.write(90);
          servo4.write(90);
          servo5.write(90);
          servo6.write(90);
          servo6.write(90);
          delay(100);
          return;
        }
      else{
        currentWord = data;
        display_braille(currentString);
        Serial.print("Data: " + currentWord + "\n")
      }
      
    }
    delay(500);
  }
}