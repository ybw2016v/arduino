void setup(/* arguments */)
{
    pinMode(13,OUTPUT);
}
void loop(/* arguments */)
{
    int i=0;
    int count=10;
    for ( i = 1; i < count; i++)
    {
        digitalWrite(13,HIGH);
        delay(100+i);
        digitalWrite(13,LOW);
        delay(100+i);
    }
}
