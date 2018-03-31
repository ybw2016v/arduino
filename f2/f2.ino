#include <dht11.h>
dht11 dog11;
#define dog11PIN 7
void setup(/* arguments */)
{
    Serial.begin(9600);
    pinMode(13,OUTPUT);
    pinMode(2,OUTPUT);
    Serial.println("start dog11");
}
void loop(/* arguments */)
{
    int chk = dog11.read(dog11PIN);
    Serial.print("Read sensor: ");
    switch (chk)
    {
    case DHTLIB_OK:
                Serial.println("OK");
                break;
    case DHTLIB_ERROR_CHECKSUM:
                Serial.println("Checksum error");
                break;
    case DHTLIB_ERROR_TIMEOUT:
                Serial.println("Time out error");
                break;
    default:
                Serial.println("Unknown error");
                break;
    }
    digitalWrite(2,HIGH);
    Serial.print("Humidity (%): ");
    Serial.println((float)dog11.humidity, 2);
    digitalWrite(13,LOW);
    Serial.print("Temperature (oC): ");
    Serial.println((float)dog11.temperature, 2);
    delay(3000);
    digitalWrite(2,LOW);
    digitalWrite(13,HIGH);
    delay(100);
}
