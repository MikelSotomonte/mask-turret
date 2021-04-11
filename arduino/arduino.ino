#include <Servo.h>
String substring;
Servo servo;
Servo servo2;
String mainString;
String xString;
String yString;
int x;
int y;
int pot1;
int pot2;
int state = 0;
//scale calibration
float sA = 1;
float sB= 1;
//offset calibration
int oA = 0;
int oB = 0;
bool buttonState = 0;

String readString, data1, data2, data3;
void setup()
{
  pinMode(7, OUTPUT);
  digitalWrite(7, LOW);
  pinMode(12, INPUT_PULLUP);
  servo.attach(9);
  servo2.attach(10);
  servo.write(90);
  servo2.write(90);
  pinMode(13, OUTPUT);
  pinMode(7, OUTPUT); //relay
  Serial.begin(2000000);
  //Serial.setTimeout(5);
}

void loop() {
  

     
    
    if (Serial.available() >0) {
      substring = Serial.read();
    }


 
    //if (Serial.readString() == "s" && state == 0){
     // digitalWrite(7, HIGH);
     // delay(250);
     // digitalWrite(7, LOW);
     // } 
     //else{
      data1 = readString.substring(0, 3); //get the first three characters
      data2 = readString.substring(3, 6); //get the next three characters
      //data3 = readString.substring(6, 9); //get the next three characters
      Serial.println(data1);
       
      x = map(data1.toInt(), 0, 640, (-90*sA)+90, (90*sA)+90); // 0, 180
      y = map(data2.toInt(), 0, 640, (90*sB)+90, (-90*sB)+90); // 180, 0
      x = x + oA;
      y = y + oB;
      servo.write(x);
      servo2.write(y);
  
      readString="";
      data1="";
      data2="";
    // }
  
}
