#include <Servo.h>

Servo servoA;
int speed;

void setup() {

  position = 0;    // variable to store the servo position
  servoA.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  for (speed = 90; speed <= 180; speed+= 10 ) { //no speed: 90, max: 180
    // in steps of 1 degree
    
    servoA.write(speed);              // tell servo to go to speed 
    delay(5000);                       // waits 5secs for the servo to reach next speed
  }
  
  for (speed = 180; speed >= 0; speed -= 10) { 
    servoA.write(speed);           
    delay(5000);                       
  }
}
