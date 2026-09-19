
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

int x = 0;
int dir = 1;

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  Serial.begin(9600);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("SSD1306 not found!");
    while(true); 
  }
}

void loop() {

  display.clearDisplay();
  display.drawCircle(x, 32, 8, WHITE);
  display.display();

  x = x + dir;

  if (x >= 120) dir = -1;   
  if (x <= 0)   dir = 1;    
}
