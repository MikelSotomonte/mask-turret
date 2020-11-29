//split string: strok()
//character in string find: strchr()

#include <Servo.h>

Servo servo;
Servo servo2;
String mainString;
String xString;
String yString;
int x;
int y;
String readString, data1, data2, data3;
void setup()
{
  servo.attach(9);
  servo2.attach(10);
  servo.write(90);
  servo2.write(90);
  pinMode(13, OUTPUT);
  Serial.begin(345600);
  Serial.setTimeout(5);
}

void loop() {
  while (Serial.available()) {
    delay(2);
    if (Serial.available() >0) {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }

  if (readString.length() >0) {   
    data1 = readString.substring(0, 3); //get the first three characters
    data2 = readString.substring(3, 6); //get the next three characters
    //data3 = readString.substring(6, 9); //get the next three characters

     
    x = map(data1.toInt(), 0, 640, 0, 180);
    y = map(data2.toInt(), 0, 640, 180, 0);
    servo.write(x);
    servo2.write(y);

    readString="";
    data1="";
    data2="";
  }

}
