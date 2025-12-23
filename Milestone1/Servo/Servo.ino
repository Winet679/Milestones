#include "ESP32Servo.h"

Servo servo;

int pin = 13;

void setup() {
  servo.attach(pin);
}

void loop()
{
  for (int i=0; i<180; i++) {
    servo.write(i);
    delay(10);
  }
}