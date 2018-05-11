#include <Servo.h>

Servo myservo1;  // create servo object to control a servo
// twelve servo objects can be created on most boards
Servo myservo2; 
int pos;
int pos2;
void setup() {
  myservo1.attach(8);
  myservo2.attach(7);
  Serial.begin(9600);
  
}

void loop() {
  float a0,a1,b0,b1;

   for (pos = 0; pos <= 180; pos += 10) { 
    myservo2.write(pos);// goes from 0 degrees to 180 degrees
     for (pos2 = 180; pos2 >= 0; pos2 -= 4) 
  { // goes from 180 degrees to 0 degrees
    myservo1.write(pos2);
    // tell servo to go to position in variable 'pos'
        a0=analogRead(A0)+5;
     a1=analogRead(A1)-5;
      b0=analogRead(A2)-5;
       b1=analogRead(A3)+5;
       Serial.print(a0);
       Serial.print(',');
          Serial.print(a1);
       Serial.print(',');
          Serial.print(b0);
       Serial.print(',');
          Serial.println(b1);
    delay(100);     
    
    // in steps of 1 degree
//    myservo1.write(pos);
//      myservo2.write(pos);
//      // tell servo to go to position in variable 'pos'
//     
//    a0=analogRead(A0);
//     a1=analogRead(A1);
//      b0=analogRead(A2);
//       b1=analogRead(A3);
//       Serial.print(a0);
//       Serial.print(',');
//          Serial.print(a1);
//       Serial.print(',');
//          Serial.print(b0);
//       Serial.print(',');
//          Serial.println(b1);
//
//    delay(60);                       // waits 15ms for the servo to reach the position
  }
pos2=180;

}
pos=0;
}
