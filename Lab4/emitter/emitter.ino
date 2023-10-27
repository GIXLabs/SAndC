/*
 "The Emitter"   TECHIN 512 555 Lab test unit

Based on:
  http://www.arduino.cc/en/Tutorial/Blink
*/

#define  LED_OUTPUT  2
#define  PULSE 6
#define  SCOPETRIG 13
#define  GLITCH_DELAY_MIN 1500 // one glitch every GLITCH_DELAY ms
#define  GLITCH_DELAY_MAX 3000

int glitch_delay = GLITCH_DELAY_MIN;
int delays[10] = {1000};

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(LED_OUTPUT, OUTPUT);
  pinMode(PULSE, OUTPUT);
  pinMode(SCOPETRIG, OUTPUT);
  for (int i=0;i<10;i++) {  
      delays[i] = int(random(GLITCH_DELAY_MIN, GLITCH_DELAY_MAX)) ; 
  glitch_delay = delays[9];
  }
}

int a=0, k=0;
int j = 0;
int led_del = 0;
// the loop function runs over and over again forever
void loop() {
 // digitalWrite(LED_BUILTIN, HIGH);
 //// delay(500);
 // digitalWrite(LED_BUILTIN, LOW);
 // delay(500);
 //
 //   emit the first pulse of the cycle
 //
  digitalWrite(PULSE, HIGH);   // set regular pulse
  delayMicroseconds(9);
  digitalWrite(PULSE, LOW);    // set regular pulse
 //
 // check for error condition and emit glitch pulse if so
 //
  if (j++ > glitch_delay){
    j = 0;         
    delayMicroseconds(250);
     
    digitalWrite(PULSE, HIGH);   // start of glitch pulse
    digitalWrite(SCOPETRIG, HIGH);   // start of glitch pulse
    delay(0);
    digitalWrite(PULSE, LOW);    // end of glitch pulse
    digitalWrite(SCOPETRIG, LOW);    // end of glitch pulse
    glitch_delay=delays[k++];
    if (k>9) { k=0;}
    led_del = 400;   //  green LED to indicate glitch for 800ms
    } // end of glitch
    
  delay(1);   // 1Khz cycle
  if (led_del-- < 0) {
      digitalWrite(LED_OUTPUT, LOW);
      led_del = -1;
      }
  else   digitalWrite(LED_OUTPUT, HIGH);
}
