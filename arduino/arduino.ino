#include <Servo.h>

Servo servo;
Servo servo2;
String mainString;
String xString;
String yString;
int x;
int y;
int pot1;
int pot2;
bool state = 0;
//calibration strings
float cA = 1;
float cB= 1;


String readString, data1, data2, data3;
void setup()
{
  pinMode(12, INPUT_PULLUP);
  servo.attach(9);
  servo2.attach(10);
  servo.write(90);
  servo2.write(90);
  pinMode(13, OUTPUT);
  Serial.begin(1000000);
  Serial.setTimeout(5);
}

void loop() {
    if(digitalRead(12) == LOW){
    state = !state;
    delay(1000);
    }
    
    if(state == 1){
      digitalWrite(13, HIGH);
      pot1 = analogRead(A4);
      pot2 = analogRead(A3);
      //Serial.println(cA);
      if(pot1 > 768){cA = cA + 0.0001;}
      if(pot1 < 256){cA = cA - 0.0001;}

      if(pot2 > 768){cB = cB + 0.0001;}
      if(pot2 < 256){cB = cB - 0.0001;}
      
      }
    else{digitalWrite(13, LOW);}
     
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

     
    x = map(data1.toInt(), 0, 640, (-90*cA)+90, (90*cA)+90); // 0, 180
    y = map(data2.toInt(), 0, 640, (90*cB)+90, (-90*cB)+90); // 180, 0
    servo.write(x);
    servo2.write(y);

    readString="";
    data1="";
    data2="";
  }
}
