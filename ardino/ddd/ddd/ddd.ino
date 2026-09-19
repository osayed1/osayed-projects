#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define SDA_PIN 18
#define SCL_PIN 19

int LED = 13;
int button = 12;
int buzzer = 14;

void setup(){
    
  pinMode(LED,OUTPUT);
  pinMode(button,INPUT);
  pinMode(buzzer,OUTPUT);
}
void loop(){
  if(digitalRead(button) == HIGH) {
    digitalWrite(LED,HIGH);
    tone(buzzer, 1000);
  }
  else{
    digitalWrite(LED,LOW);
    noTone(buzzer);
  }
}