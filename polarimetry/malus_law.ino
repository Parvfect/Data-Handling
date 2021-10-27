
// Right we are assuming Servo rotates one degree and takes a light measurement and appends to the array
#include <Servo.h>

int light_sensor_pin = A0;
int green_light_pin = A0;
int blue_light_pin = A0;
int red_light_pin = A0;
int servo_pin = 9;

Servo servo;

float light_values[180]{0}; 

void setup(){
    Serial.begin(9600);
    servo.attach(servo_pin);
    pinMode(red_light_pin, OUTPUT);
    pinMode(green_light_pin, OUTPUT);
    pinMode(blue_light_pin, OUTPUT);
}

void loop(){
    
    // Starting the LED
    led_init() 
    
    // Starting taking measurements
    take_measurements()

    // Print all the light values taken
    for(int i = 0; i < 180; i++){
        Serial.println(light_values[i]);
    }
}

void take_measurements(){
    /*
    Rotates the Servo by one degree until 180 and takes a light sensor measurement at each and appends it 
    to the array
    */

   for(int i = 1; i < 180; i++){
        servo.write(i);
        light_values[i] = read_light_value();
        delay(1);
    }
}

float read_light_value(){
    /*
    Reads the light sensor and returns the value
    */
    return analogRead(light_sensor_pin);
}

void led_init(){
    RGB_color(255, 255, 255); // White
}



