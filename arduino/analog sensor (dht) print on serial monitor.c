#include<DHT.h>
DHT dht(8,DHT11)
float t,h;
void setup(){
  Serial.begin(9600);
  dht.begin();
  Serial.println("Starting DHT Test");
  delay(2000);
}
void loop(){
  h=dht.readHumidity();
  t=dht.readTemperature();
  if(isnan(h)||isnan(t)){
    Serial.println("Failed to read");
  }
  else{
    Serial.println(h);
    Serial.println(t);
  }
}
