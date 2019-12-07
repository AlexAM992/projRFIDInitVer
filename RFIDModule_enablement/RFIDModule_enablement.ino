//taken from https://naylampmechatronics.com/blog/22_Tutorial-Lector-RFID-RC522.html

#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.
 
void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  pinMode(2,OUTPUT);
  pinMode(4,OUTPUT);
  digitalWrite(2,LOW);
  digitalWrite(4,LOW);
}
void loop() 
{
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  //Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {     
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();
  Serial.println(content);
  if(content.equals("A9A23D59"))
  {
    digitalWrite(2,HIGH);
    digitalWrite(4,LOW);
    }else
    {
      digitalWrite(4,HIGH);
      digitalWrite(2,LOW);
      }
    
}
