#include <Servo.h>
Servo myservo;
void setup()
{
myservo.attach(3); 
}

void loop()
{

for (int i = 0; i < 180; ++i)
{
	myservo.write(i);
	delay(200);
}
for (int i = 0; i < 180; --i)
{
	myservo.write(180-i);
	delay(200);
}
}
