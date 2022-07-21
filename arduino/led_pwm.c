int i;
void setup() {
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
}
void loop()
{
  for(int i=0;i<=255;i++)
  {
    RGB(0,i,0);
    delay(100);
  }
  for(int i=0;i<=255;i++)
  {
    RGB(i,0,0);
    delay(100);
  }
  for(int i=0;i<=255;i++)
  {
    RGB(0,0,i);
    delay(100);
  }
}
void RGB(int R,int G,int B)
{
  analogWrite(9,R);
  analogWrite(10,G);
  analogWrite(11,B);
}
