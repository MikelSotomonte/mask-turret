
float analog;
float digital;


void setup(){
    Serial.begin(9600);
}

void loop(){

analog = analogRead(0);
digital = digitalRead(2);

Serial.println(analog);
Serial.println(digital);

delay(500);
}
