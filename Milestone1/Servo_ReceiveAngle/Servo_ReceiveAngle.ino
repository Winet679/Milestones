#include <ESP32Servo.h>

Servo servo;
int pin = 13;

void setup() {
  Serial.begin(115200);
  servo.attach(pin);
}

void loop() {
  if (Serial.available() > 0) {
    int degree = Serial.parseInt();

    while(Serial.available() > 0) {
      Serial.read();
    }
  }
}