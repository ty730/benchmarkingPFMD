#include "Arduino.h"
#include <AccelStepper.h>


#define STEPPER_DIR_PIN 12
#define STEPPER_STEP_PIN 13

// Define a stepper and the pins it will use
//AccelStepper stepper; // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepper(AccelStepper::DRIVER, STEPPER_STEP_PIN, STEPPER_DIR_PIN);
void setup()
{  
  Serial.begin(115200);

  // Change these to suit your stepper if you want
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(1000);
  stepper.moveTo(10000/2);

}
int x = 0;
int y = 0;
int d = 10000/2;
int c = 0;

void loop()
{
    // If at the end of travel go to the other end
    //if (stepper.distanceToGo() == 0)
      //stepper.moveTo(-stepper.currentPosition());

    
    stepper.run();

    while (Serial.available()) 
      {
        c = Serial.read();
        if ('s' == c ){
          x = Serial.parseInt();
          Serial.print("speed: ");
          Serial.println(x);
          stepper.setMaxSpeed(x);
        }
        if ('d' == c ){
          d = Serial.parseInt();
          Serial.print("steps: ");
          Serial.println(d);
          stepper.moveTo(d/2);
        }
        if ('p' == c){
          Serial.println("pausing stepper");
          Serial.print("Currently at: ");
          Serial.println(stepper.currentPosition());
          while (true) {
            stepper.stop();
            c = Serial.read();
            if ('r' == c) {
              Serial.println("resuming stepper");
              break;
            }
          }
         // stepper.moveTo(d/2)
        }
  }

}
