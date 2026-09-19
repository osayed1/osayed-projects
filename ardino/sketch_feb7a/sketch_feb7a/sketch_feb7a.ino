int led = 4;
int sensor = A0;
int sensor_idk = 1000;
int buzzer = 7;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}



void loop() {

  int gas_value = analogRead(A0);
  if (gas_value > sensor_idk) {
    digitalWrite (led, HIGH);
    
    tone(buzzer, 1800);
    delay(300);
    noTone(buzzer);
    delay(700);
  }
  else { 
    digitalWrite(led, LOW); 
    noTone(buzzer);
    }
  delay(100);
    Serial.println(gas_value);

}
