  #include <SPI.h> //Call SPI library so you can communicate with the nRF24L01+
#include <nRF24L01.h> 
#include <RF24.h> 

#define node_id 3;
int act_sens = A0; 
int temp_sens = A1;
int temp_set = A2;
int ldr = A3;



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
}data;

data tr;



void setup()   
{
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
