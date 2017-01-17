#include <SPI.h> //Call SPI library so you can communicate with the nRF24L01+
#include <nRF24L01.h> 
#include <RF24.h> 

const int pinCE = 9; //This pin is used to set the nRF24 to standby (0) or active mode (1)
const int pinCSN = 10; 
RF24 radio(pinCE, pinCSN); // Declare object from nRF24 library (Create your wireless SPI) 
const uint64_t rAddress[] = {0xE8E8F0F0E1LL, 0xE8E8F0F0E2LL, 0xE8E8F0F0E3LL, 0xE8E8F0F0E4LL, 0xE8E8F0F0E5LL, 0xE8E8F0F0E6LL};  

typedef struct{
  int node;
  int diff;
  int activity;
  float temp;
  int light;
  int ID;
}data;

data tr;

int act[]={0,0,0,0};
int fan[]={0,0,0,0};
void setup()   
{
  Serial.begin(57600);  //start serial to communication
 // Serial.println("Server On. Listening for transmissions "); 
  radio.begin();  //Start the nRF24 module
  radio.openReadingPipe(1,rAddress[0]);      
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(A0,OUTPUT);
  pinMode(A1,OUTPUT);
  pinMode(A2,OUTPUT);
  pinMode(A3,OUTPUT);
  radio.startListening();                 // Start listening for messages
}

void loop()  
{   
    byte pipeNum = 0; //variable to hold which reading pipe sent data
    byte gotByte = 0; //used to store payload from transmit module
    
    while(radio.available(&pipeNum)){ //Check if recieved data
     radio.read( &tr, sizeof(tr) ); //read one byte of data and store it in gotByte variable
     if(tr.node>0&&tr.node<5)
     {
       tr.temp=abs(tr.temp);
       Serial.print(" "); 
     Serial.print(tr.node); //print which pipe or transmitter this is from
     Serial.print(" ");
     Serial.print(tr.activity); //print payload or the number the transmitter guessed
     Serial.print(" ");
     Serial.print(tr.temp); //print payload or the number the transmitter guessed
     //Serial.print("\t Light: ");
     //Serial.print(tr.light); //print p+ayload or the number the transmitter guessed
     Serial.print(" ");
     Serial.print(tr.ID); //print p+ayload or the number the transmitter guessed
     Serial.println();  
   }
     act[tr.node-1]=tr.activity;
     if(tr.diff>1)
     fan[tr.node]=1;
     if(tr.diff<-1)
     fan[tr.node]=0;
     
     int i;
     for(i=3;i<7;i++)
     digitalWrite(i,fan[i-3]);
     for(i=A0;i<A4;i++)
     digitalWrite(i,fan[i-A0]);
     
   
 }

  delay(100);    
}
