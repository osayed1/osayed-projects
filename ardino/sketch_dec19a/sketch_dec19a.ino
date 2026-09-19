
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

int buzzer = 8;

const int echo = 2;
const int trig = 7;

int LED1 = 11;
int LED2 = 12;
int LED3 = 13;

// sda (sercile data (A4))
// scl (sercile clock (A5))

void setup() {

  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);

  pinMode(buzzer, OUTPUT);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("SSD1306 not found!");
    while(true);
  }
  Serial.begin(9600);

}

void loop() {

  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  long time = pulseIn(echo, HIGH, 30000);
  float distance = time * 0.034 / 2;

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("cm: ");
  display.println(distance);
  delay(20);

  if (distance >= 30) {
  display.println("SAFE");
  }
  else if (distance >= 10) {
    display.println("WARNING");
  }
  else {
    display.println("STOP");
  }
  display.display();

  if (distance < 30)digitalWrite(LED1, HIGH);
  else digitalWrite(LED1, LOW);

  if (distance < 20)digitalWrite(LED2, HIGH);
  else digitalWrite(LED2, LOW);

  if (distance < 10)digitalWrite(LED3, HIGH);
  else digitalWrite(LED3, LOW);

if (distance <= 5) {
  tone(buzzer, 700);   
}
else if (distance <= 10) {
  tone(buzzer, 1000);    
}
else {
  noTone(buzzer);      
}

}
