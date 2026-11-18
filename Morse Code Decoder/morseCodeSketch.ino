#include <LiquidCrystal_I2C.h>    // Libreria que controla el I2C
#include <Wire.h>  

LiquidCrystal_I2C lcd(0x27,16,2);

const int buttonPin = 2;
const int ledPin = 13;

int buttonState = 0;
int lastState = LOW;

unsigned long pressStartTime = 0;
unsigned long buttonDuration = 0;
unsigned long lastPressTime = 0;

const unsigned long timeStop = 800;
bool readingMorse = false;

char encodedMessage[50] = "\0";

const char* alphaNumeric[] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4",
"5", "6", "7", "8", "9"};

const char* morseCode[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",
"-----",".----","..---","...--","....-",".....","-....","--...","---..","----."};

void setup() {
  // put your setup code here, to run once:
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print(" PROTOCOLO  I2C ");
}

void loop() {
  // put your main code here, to run repeatedly:
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  //Detects that the program was just taking in a morse code and prints if 800ms have passed since the last press.
  if(readingMorse && buttonState == LOW && (millis()-lastPressTime >= timeStop)){
    printMorse(encodedMessage);
    readingMorse = false;
    memset(encodedMessage, 0, sizeof(encodedMessage));
  }

  // Detects that the button has just been pushed; old state was LOW but current state is HIGH
  if (lastState == LOW && buttonState == HIGH) {
    pressStartTime = millis();
    digitalWrite(ledPin, HIGH);
  }

  //Detects that the button was just released; old state was HIGH but current state is LOW
  if(lastState == HIGH && buttonState == LOW){
    buttonDuration = millis() - pressStartTime;
    if(buttonDuration < 135){
      Serial.println("dot");
      strcat(encodedMessage, ".");
    }
    else {
      Serial.println("dash");
      strcat(encodedMessage, "-");
    }
    lastPressTime = millis();
    readingMorse = true;
    digitalWrite(ledPin, LOW);
  }

  //Sets the last button state at the end of the loop
  lastState = buttonState;
  delay(5);
}

void printMorse(char* message) {
  lcd.clear();
  Serial.println(message);
  if(message[0] != '\0'){
    for(int i = 0; i < 36; i++){
      if(strcmp(message, morseCode[i]) == 0){
        Serial.println(alphaNumeric[i]);
        lcd.print(alphaNumeric[i]);
        return;
      }
  }
  Serial.println("ERROR");
  lcd.print("ERROR");
  }
  return;
}
