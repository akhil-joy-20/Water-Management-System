#define SensorPin 0          // the pH meter Analog output is connected with the Arduino’s Analog
unsigned long int avgValue;  //Store the average value of the sensor feedback
float b;
int buf[10],temp;

#define TRIGGER_PIN 3
#define ECHO_PIN 2
#define USONIC_DIV 0.034

void setup() {
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(13,OUTPUT); 
  
  Serial.begin(9600);

//  Serial.println("Ready");   
}

void loop() {

  long duration;
  long distance;
  int percentage;
  
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(11);
  
  digitalWrite(TRIGGER_PIN, LOW);
  
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * USONIC_DIV / 2;

  percentage = map(distance, 14, 4, 0, 99);

  if(percentage < 0){
    percentage = 0;
  }else if(percentage >99){
    percentage = 99;
  }

//  Serial.print("Percentage: ");
  Serial.print(percentage);
  Serial.print(" ");
//  Serial.print("%  Distance: ");
  Serial.print(distance);
//  Serial.print(" cm");

//   delay(5000);


     for(int i=0;i<10;i++)       //Get 10 sample value from the sensor for smooth the value
  { 
    buf[i]=analogRead(SensorPin);
    delay(10);
  }
  for(int i=0;i<9;i++)        //sort the analog from small to large
  {
    for(int j=i+1;j<10;j++)
    {
      if(buf[i]>buf[j])
      {
        temp=buf[i];
        buf[i]=buf[j];
        buf[j]=temp;
      }
    }
  }
  avgValue=0;
  for(int i=2;i<8;i++)                      //take the average value of 6 center sample
    avgValue+=buf[i];
  float phValue=(float)avgValue*5.0/1024/6; //convert the analog into millivolt
  phValue=(3.5*phValue)-3.5;                      //convert the millivolt into pH value
  Serial.print(" ");  
  Serial.print(phValue,2);
  Serial.println(" ");
  digitalWrite(13, HIGH);       
  delay(5000);
  digitalWrite(13, LOW); 

 
 
}
