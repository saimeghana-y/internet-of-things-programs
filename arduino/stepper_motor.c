#include<Stepper.h>
int steps_per_rev=32;
int gear_reduction=64;
int steps_req=gear_reduction*steps_per_rev;
int c;
Stepper motor(steps_per_rev,2,4,3,5);
void setup(){
  Serial.begin(9600);
}
void loop(){
  c=Serial.parseInt();
  Serial.println(c);
  motor.setSpeed(900);
  motor.step(c);
  delay(1000);
  Serial.println(c);
  motor.setSpeed(900);
  motor.step(-c);
  delay(1000);
}
