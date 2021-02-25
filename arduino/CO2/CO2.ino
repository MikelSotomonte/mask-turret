
float analog;
float digital;


void setup(){
    Serial.begin(9600);
}

void loop(){

analog = analogRead(0);
Serial.println(analog);


delay(500);
}
