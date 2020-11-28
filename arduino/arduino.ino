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
bool a;
void setup()
{
  servo.attach(9);
  servo2.attach(10);
  servo.write(90);
  servo2.write(90);
  pinMode(13, OUTPUT);
  Serial.begin(345600);
  Serial.setTimeout(200);
}

void loop()
{
  if (Serial.available() > 0) {
    xString = Serial.readStringUntil(':');
    //Serial.println("x: " + xString);
    //Serial.read();
    yString = Serial.readStringUntil('\0');
    Serial.read();
    //Serial.println("y: " + yString);
  
    x = xString.toInt();
    y = yString.toInt();
    Serial.println(y);
    Serial.println(x);
    x = map(x, 0, 640, 0, 180);
    y = map(y, 0, 640, 180, 0);
    
    servo.write(x);
    servo2.write(y); 
  }
}
