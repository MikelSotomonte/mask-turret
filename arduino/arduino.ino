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
  Serial.begin(1000000);
  Serial.setTimeout(5);
}

void loop() {
  
    buttonState = digitalRead(12);
    if(buttonState == LOW){
      if(state < 3){state = state + 1;}
      else{state = 0;}
    delay(1000);
    if(buttonState == LOW){
      Serial.println("Calibration data: sA = " + String(sA) + " | sB = " + String(sB) + " | oA = " + String(oA) + " | oB = " + String(oB));
      
      }
    }
    
    if(state == 1){
      digitalWrite(13, HIGH);
      pot1 = analogRead(A4);
      pot2 = analogRead(A3);
      //Serial.println(cA);
      if(pot1 > 768){sA = sA + 0.0001;}
      if(pot1 < 256){sA = sA - 0.0001;}

      if(pot2 > 768){sB = sB + 0.0001;}
      if(pot2 < 256){sB = sB - 0.0001;}
      
      }
      if(state == 2){
        digitalWrite(13, HIGH);
        delay(100);
        pot1 = analogRead(A4);
        pot2 = analogRead(A3);
        digitalWrite(13, LOW);
        //Serial.println(oA);
        if(pot1 > 768){oA = oA + 5;}
        if(pot1 < 256){oA = oA - 5;}
  
        if(pot2 > 768){oB = oB + 5;}
        if(pot2 < 256){oB = oB - 5;}
        delay(100);
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
    digitalWrite(13, HIGH);
    data2 = readString.substring(3, 6); //get the next three characters
    //data3 = readString.substring(6, 9); //get the next three characters

     
    x = map(data1.toInt(), 0, 640, (-90*sA)+90, (90*sA)+90); // 0, 180
    y = map(data2.toInt(), 0, 640, (90*sB)+90, (-90*sB)+90); // 180, 0
    x = x + oA;
    y = y + oB;
    servo.write(x);
    servo2.write(y);

    readString="";
    data1="";
    data2="";
  }
  if (data1 == "s" && state == 0){
      digitalWrite(7, HIGH);
      delay(250);
      digitalWrite(7, LOW);
      }
}
