#include <Servo.h>

Servo servo;

void setup()
{
  servo.attach(9);
  pinMode(13, OUTPUT);
  Serial.begin(250000);
}
void loop() {
servo.write(map(Serial.parseInt(), 0, 640, 0, 180));


}
