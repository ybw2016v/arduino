#include <Servo.h>
struct pw
{
    int x;
    int y;
    float l;
    struct pw * next;
};

struct pw * h = NULL;
int a0;
int a1;
int b0;
int b1;
Servo s0;
Servo s1;
char com;