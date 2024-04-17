String currentWord;

void setup() {
	Serial.begin(9600);
  currentWord = ' ';
}

void loop() {

  // if there is bytes in the serial
  if(Serial.available() > 0){
    String data = Serial.readStringUntil("\n");

    if(data == "end\n"){
      Serial.print("end connection\n");
    }
    //next button change the condition here for button input
    else if(true){
      Serial.print("next\n");
    }
    //prev button change the condition here for button input
    else if(false){
      Serial.print("prev\n");
    }
    else{
      currentWord = data;
      Serial.print("Data: " + data);
    }

    // do your braille thing here or better do it asynchronously
  }
}