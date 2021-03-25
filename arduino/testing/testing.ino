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
    Serial.println(buttonState);}
