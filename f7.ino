#include "f7.h"
void readlight();
void findmaxq();
void saomiao();
void sf();
void showlight();
void setup()
{
    // 初始化舵机和串口
    s0.attach(7);
    s1.attach(8);
    Serial.begin(9600);
}
void loop()
{
    if (Serial.available())
    {
        com=Serial.read();
        
        switch (com)
        {
            case 's':
                saomiao();
                break;
            case 'f':
                findmaxq();
                break;
            case 'q':
                sf();
                break;
            case 'l':
                showlight();
                break;
            default:
                Serial.println("bad com");
                break;
        }
    }
}
void readlight()
{
    // 光强获取函数。
    a0=analogRead(A0)-5;
    a1=analogRead(A1)+5;
    b0=analogRead(A2)-5;
    b1=analogRead(A3)+5;
}
void saomiao()
{
    // 光强扫描函数
    float l;
    int i,j;
    
    for( i = 0; i < 180; i++)
    {
        
        for( j = 0; j < 180; j++)
        {
            delay(10);
            s0.write(i);
            delay(10);
            s1.write(j);
            delay(5);
            readlight();
            l=(a0+a1+b0+b1);
            Serial.print(l,2);
            Serial.print(',');
        }
        Serial.print('\n');
        delay(10);
    }
    
    
}

void findmaxq()
{
    // 空间光强极值获取函数。
    int flog1=0;
    int flog2=0;
    int i=90;
    int j=90;
    s0.write(i);
    s1.write(j);
    for(int ip = 0; ip <= 4096; ip++)
    {
        readlight();
        delay(2);
        
        if (a0>(a1+3)) 
        {
            // i++;
            if (i<=179)
            {
                i++;
            } 
            else
            {
                flog1=1;
            }
        }
        if (a0<(a1-3))
        {
            // i--;
            if (i>=1)
            {
                i--;
                Serial.print("*");
            } 
            else
            {
                flog1=1;
            }
        }
        if ((a0<=(a1+3))&&(a0>=(a1-3)))
        {
            flog1=1;
        }
        Serial.print(i);
        Serial.print(',');
        Serial.print(flog1);
        Serial.print(',');
        s0.write(i);
        if (b0>(b1+3))
        {
            // j++;
            if (j<=179)
            {
                j++;
            } 
            else
            {
                flog2=1;
            } 
        }
        if (b0<=(b1-3))
        {
            // i--;
            if (j>=1)
            {
                j--;
            } 
            else
            {
                flog2=1;
            }
        }
        if (b0<=(b1+3)&&b0>=(b1-3))
        {
            flog2=1;
        }
        Serial.print(flog2);
        Serial.print(',');
        Serial.println(j);
        s1.write(j);
        if (flog1==1&&flog2==1)
        {
            Serial.println('p');
            Serial.print(i);
            Serial.print(',');
            Serial.print(j);
            break;
        }
    }
}
void sf()
{
    // 光强极大值扫描函数
    float l,ml;
    int i,j;
    int mx,my;
    ml=100000;
    mx=0;
    my=0;
    for( i = 0; i <= 180; i=i+10)
    {
        
        for( j = 0; j < 180; j=j+10)
        {
            delay(10);
            s0.write(i);
            delay(10);
            s1.write(j);
            delay(100);
            readlight();
            l=(a0+a1+b0+b1);
            // Serial.print(l,2);
            // Serial.print(',');
            if (ml>=l)
            {
                ml=l;
                mx=i;
                my=j;
            }
        }
        // Serial.print('\n');
        delay(10);
    }
    delay(1000);
    s0.write(mx);
    s1.write(my);
    delay(20);
    Serial.println('p');
    
    
}
void showlight()
{
    float l;
    readlight();
    delay(10);
    l=a0+a1+b0+b1;
    Serial.println(l);
    delay(2);
}
