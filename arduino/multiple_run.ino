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
  Serial.println("initialized rotator");
  Serial.println("Enter 'r' to start, 's' to stop");

//  // Change these to suit your stepper if you want
//  stepper.setMaxSpeed(1200);
//  stepper.setAcceleration(5000);
//  stepper.moveTo(0);

//  stepper.moveTo(stepper.currentPosition());
  

}
int x = 0;
int y = 1;
int hault = 's'; // ascii for s

// this is an rotator multiple run code
// it will move rotator bug 180 degree back and forth
// returns the bug to the original position
void loop()
{
      while (Serial.available()) 
      {
        hault = Serial.read();
        if ('s' == hault ){
          Serial.println("Stopped rotator");
          stepper.setMaxSpeed(5000);
        }

        if ('r' == hault ){
          Serial.println("restarted rotator");
            // Change these to suit your stepper if you want
          stepper.setMaxSpeed(1200);
          stepper.setAcceleration(5000);
          stepper.moveTo(3200);
          y = 0;
          x = 0;
        }


      }
    // If at the end of travel go to the other end
    if (stepper.distanceToGo() == 0 && !y)
    {
      Serial.println("running rotator");
      stepper.moveTo(-stepper.currentPosition());
      
      // computing if we have completed the trip to original position
      x = (x+1) % 2;
      
      Serial.print("completed last rotation, trial number: ");
      Serial.println(x);
      delay(2500); // wait for a second
      if (0 == x && 's' == hault)
      {
        stepper.stop();
        y = 1; // flag for stop
        Serial.println("successfully stopped");
      }
      
    }
    
    stepper.run();



}
