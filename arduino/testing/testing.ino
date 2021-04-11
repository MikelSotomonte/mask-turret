
#include <Servo.h>

Servo servo;
Servo servo2;
int x;
int y;
String mainString, data1, data2;


void setup() {
  servo.attach(9);
  servo2.attach(10);
  servo.write(90);
  servo2.write(90);
  Serial.begin(2000000); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  while (Serial.available()) {
    delay(2);
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      mainString += c; //makes the string readString
    }
  }

  if (mainString.length() >0) {  

    data1 = mainString.substring(0, 3); //get the first three characters
    data2 = mainString.substring(3, 6); //get the next three characters
    //data3 = readString.substring(6, 9); //get the next three characters

     
    x = map(data1.toInt(), 0, 640, 0, 180); // 0, 180
    y = map(data2.toInt(), 0, 640, 0, 180); // 180, 0
    servo.write(x);
    servo2.write(y);
    //delay(400);
    mainString = "";
  }
}
 
