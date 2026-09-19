const int echo_us = 2;
const int trig_us = 7;

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

 int LED1 = 11;
 int LED2 = 12;
 int LED3 = 13;

 int buzzer = 8;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

 void setup() { 

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("SSD1306 not found!");
    while(true); 
  }

  pinMode(buzzer, OUTPUT);

  pinMode(echo_us, INPUT);
  pinMode(trig_us, OUTPUT);

  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  digitalWrite(trig_us, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_us, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_us, LOW);

  long time = pulseIn(echo_us, HIGH);
  float distance = time * 0.034 / 2;

  Serial.print("cm:");
  Serial.println(distance);

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("cm: ");
  display.println(distance);
  display.display();
  delay(20);

if (distance < 30) digitalWrite(LED3, HIGH);
else digitalWrite(LED3, LOW);

if (distance < 20) digitalWrite(LED2, HIGH);
else digitalWrite(LED2, LOW);

if (distance < 10) digitalWrite(LED1, HIGH);
else digitalWrite(LED1, LOW);

if ( distance <= 20 && distance > 11 ){
  digitalWrite(buzzer, HIGH);
  delay(500);
  digitalWrite(buzzer, LOW);
  delay(500);
  }
else digitalWrite(buzzer, LOW);

if (distance <= 10){
  digitalWrite(buzzer, HIGH);
  delay(50);
  }
else digitalWrite(buzzer, LOW);
}

