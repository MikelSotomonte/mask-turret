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
  
void setup()
{
  
  servo.attach(9);
  servo2.attach(10);
  pinMode(13, OUTPUT);
  Serial.begin(250000);
}
String getValue(String data, char separator, int index)
{
    int found = 0;
    int strIndex[] = { 0, -1 };
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == separator || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i+1 : i;
        }
    }
    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
void loop()
{
  
  mainString = Serial.read();
  xString = getValue(mainString, ':', 0);
  yString = getValue(mainString, ':', 1);
  servo.write(map(x, 0, 640, 0, 180));
  servo2.write(map(y, 0, 640, 0, 180));


}
