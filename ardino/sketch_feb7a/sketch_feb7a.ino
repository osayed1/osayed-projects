#include <DHT.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>
#include <SPI.h>
#include <wifi.h>
#include <HTTPClient.h>

const char* ssid = "NawazDeco";
const char* password = "nd0125204791";
const char* serverName = "https://192.168.68.50:5000/update";

DHT mysensor(4, DHT11);
Adafruit_SSD1306 display(128, 64, &Wire, -1);

int red_led = 5 ;
int blue_led = 18;

void setup() {
serial.begin(115200);

wifi.begin(ssid, password);
serial.print("connecting to the wifi");

while (wifi.status() != WL_CONNECTED) {
  delay(500);
  serail.print("."); 
  }
serail.println("\nwifi connected");

display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
display.setTextColor(WHITE);
display.setTextSize(2);

mysensor.begin();

pinMode(red_led, OUTPUT);
pinMode(blue_led, OUTPUT);
}

void loop() {
double t = mysensor.readTemperature();

if (wifi.status() == WL_connect) {
  WifiClient client;
  HTTPClient http;

  http.begin(client, servername);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded")
  String httpRequestData = "temperature=" + String(t);
  int httpResponseCode = http.POST(httpRequestData)

  http.end();
}

display.clearDisplay();
display.setCursor(0, 0);
display.print(t);

display.display();

delay(500);

if (t < 27) { 
    digitalWrite(red_led, LOW);
    digitalWrite(blue_led, HIGH);
  }
  else if (t > 28) { 
    digitalWrite(blue_led, LOW);
    digitalWrite(red_led, HIGH);
  }
  else { 
    digitalWrite(blue_led, LOW);
    digitalWrite(red_led, LOW);
  }
}