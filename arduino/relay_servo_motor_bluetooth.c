#include <SoftwareSerial.h>
#include<Servo.h>
SoftwareSerial EEBLUE(10,11);
Servo s1;
int angle;
void setup()
{
  Serial.begin(9600);
  EEBLUE.begin(9600);
  Serial.println("BLUETOOTH IS READY");
  s1.attach(8);
}
void loop()
{
if(EEBLUE.available()){
  angle=EEBLUE.parseInt();
    for(int i=0;i<=angle;i+=20){
      s1.write(i);
      delay(500);
    }
  }
}
