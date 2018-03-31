#include <dht11.h>
dht11 dog11;
#define dog11PIN 7
void setup()
{
    Serial.begin(9600);
    pinMode(13, OUTPUT);
}
void loop()
{
    if (Serial.available())
    {
        if ('r'==Serial.read())
        {
            int chk = dog11.read(dog11PIN);
            //Serial.print("Humidity (%): ");
            Serial.println((float)dog11.humidity, 2);
            digitalWrite(13,LOW);
            //Serial.print("Temperature (oC): ");
            Serial.println((float)dog11.temperature, 2);
            Serial.println(chk);
            delay(1000);
            digitalWrite(13,HIGH);
        }
    }
}
