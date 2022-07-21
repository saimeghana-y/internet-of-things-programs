#include<Servo.h>
Servo s1;
int c,i;
int servopin=8;
void setup(){
Serial.begin(9600);
s1.attach(servopin);
}
void loop(){
c = Serial.parseInt();
for(i=0;i<=c;i++){
s1.write(i);
delay(500);
}
delay(500);
for(i=c;i>=0;i--){
s1.write(i);
delay(500);
}
}
