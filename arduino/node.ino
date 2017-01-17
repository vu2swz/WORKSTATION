#include <SPI.h> //Call SPI library so you can communicate with the nRF24L01+
#include <nRF24L01.h> 
#include <RF24.h> 

#define node_id 3;
int act_sens = A0; 
int temp_sens = A1;
int temp_set = A2;
int ldr = A3;
int powerLED=3;
int IDled =4;
int state =0;
int i=0;
int S=0;



const int pinCE = 9; //This pin is used to set the nRF24 to standby (0) or active mode (1)
const int pinCSN = 10; 
RF24 radio(pinCE, pinCSN); // Declare object from nRF24 library (Create your wireless SPI) 
const uint64_t rAddress[] = {0xE8E8F0F0E1LL, 0xE8E8F0F0E1LL, 0xE8E8F0F0E1LL, 0xE8E8F0F0E1LL, 0xE8E8F0F0E1LL, 0xE8E8F0F0E1LL};  

typedef struct{
  int node ;
  int diff;
  int activity;
  float temp;
  int light;
  int ID;
}data;

data tr;



void setup()   
{
   pinMode(7,INPUT_PULLUP);
   pinMode(6,INPUT_PULLUP);
   pinMode(5,INPUT_PULLUP);
   //pinMode(act_sens,INPUT);
  pinMode(temp_set,INPUT);
  tr.node = node_id;
  Serial.begin(9600);  //start serial to communication
  Serial.print("Initialised Node ");
  Serial.println(tr.node);
  radio.begin();  //Start the nRF24 module
  radio.openWritingPipe(rAddress[tr.node]);    // setup pipe to transmit over
  radio.stopListening(); 
  
}

void loop()
{
  //Serial.println(state);
  //*********************************
  if(state==0)
  {
    digitalWrite(4,HIGH);
    digitalWrite(3,LOW);
  }
  if(state==1)
  {
    digitalWrite(3,HIGH);
    digitalWrite(4,LOW);
    Serial.println("try reset");
     if(digitalRead(5)==LOW)
    {
      digitalWrite(4,HIGH);
       delay(500);
       state=0;
       S=0;
       tr.ID=0;
       digitalWrite(4,LOW);
    }
  }
  while(state==0)
   {
    Serial.println("noID");
    if(digitalRead(6)==LOW)
     {
      Serial.println("1");
      digitalWrite(3,HIGH);
      S=S*10+1;
      delay(500);
      digitalWrite(3,LOW);
     }
    if(digitalRead(7)==LOW)
     {
      Serial.println("2");
      digitalWrite(3,HIGH);
      S=S*10+2; 
      delay(500);
      digitalWrite(3,LOW);
     }
     if(digitalRead(5)==LOW)
     {
      state=1;
      delay(500);
      tr.ID=S;
     }
   }
  //Serial.println(S);
 
  //**************************************
  if(analogRead(act_sens)<50)
  tr.activity = 1;
  else
  tr.activity = 0;
  
  tr.temp = -(analogRead(temp_sens))*500/1024;
  tr.light = analogRead(ldr);
  //tr.light=analogRead(ldr);
  tr.diff = tr.temp-(analogRead(temp_set))*42/1024;
    Serial.print("Transmitter: "); 
     Serial.print(tr.node); //print which pipe or transmitter this is from
     Serial.print("\t Activity: ");
     Serial.print(tr.activity);
     //print payload or the number the transmitter guessed
    Serial.print("\t Set Temp: ");
     Serial.print((analogRead(temp_set))*42/1024);
     Serial.print("\t Temp: ");
     Serial.print(tr.temp); //print payload or the number the transmitter guessed
     Serial.print("\t Temp Diff: ");
     Serial.print(tr.diff); //print payload or the number the transmitter guessed
     Serial.print("\t Light: ");
     Serial.print(tr.light); //print payload or the number the transmitter guessed
     Serial.print("\t ID: ");
     Serial.print(tr.ID); //print payload or the number the transmitter guessed
     
     Serial.println();
     
  if (!radio.write( &tr, sizeof(tr) ))
  {  
      Serial.println("Data sending failed");      
  }
  else 
  {
      Serial.println("Data sent to server ");
  }
 radio.powerDown();
  delay(1000);
  radio.powerUp();
}
