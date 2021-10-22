// Complimentary file that goes with the python script for the Malus Law Experiment

#include <Servo.h>
Servo myservo;
String inByte;
int pos;

void setup() {

myservo.attach(9);
Serial.begin(9600);
}

void loop()
{
if(Serial.available()) // if data available in serial port
{
inByte = Serial.read(); // read data until newline
pos = inByte.toInt(); // change datatype from string to integer
myservo.write(pos); // move servo
Serial.print("Servo in position: ");
Serial.println(inByte);
}
}