#include <SoftwareSerial.h>
#include <Wire.h>
#include <MechaQMC5883.h>

MechaQMC5883 qmc; //방위각 센서
SoftwareSerial gpsSerial(6,5); //GPS 모듈
// RX = 6
// TX = 5

char c = ""; // \n 인지 구분 및 str에 저장
String str = ""; // \n 전까지 c 값을 저장
String targetStr = "GPGGA"; // str의 값이 NMEA의 GPGGA 값인지 지정

void setup() {
  Wire.begin();
  Serial.begin(9600);
  gpsSerial.begin(9600);
  qmc.init(); //qmc.setMode(Mode_Continuous,ODR_200Hz,RNG_2G,OSR_256);
  Serial.println("Start System... ");
}


void loop() {
  int x, y, z;
  int azimuth;

  // 방위각 센서 값 디버깅 용
  //Serial.print("x: ");
  //Serial.print(x);
  //Serial.print(" y: ");
  //Serial.print(y);
  //Serial.print(" z: ");
  //Serial.print(z);
  
  

  if(gpsSerial.available()) // gps 센서 통신 가능 여부 확인
    {
      c = gpsSerial.read(); //gps 센서 값 읽기
      qmc.read(&x, &y, &z,&azimuth); //방위각 센서 값 읽어오기
      
      if(c == '\n')// \n 일시. 지금까지 저장된 str 값이 targetStr과 맞는지 구분
        { 
        
        if(targetStr.equals(str.substring(1, 6))) // NMEA 의 GPGGA 값일시
          { 
          // Serial.println(str); //디버깅용, 파싱 전 값 출력
          
          // , 기준 파싱
          int first = str.indexOf(",");
          int two = str.indexOf(",", first+1);
          int three = str.indexOf(",", two+1);
          int four = str.indexOf(",", three+1);
          int five = str.indexOf(",", four+1);

          // index 추출
          String Lat = str.substring(two+1, three);
          String Long = str.substring(four+1, five);

          // 앞값과 뒷값을 구분
          String Lat1 = Lat.substring(0, 2);
          String Lat2 = Lat.substring(2);

          // 앞값과 뒷값을 구분
          String Long1 = Long.substring(0, 3);
          String Long2 = Long.substring(3);

          // 좌표 계산
          double LatF = Lat1.toDouble() + Lat2.toDouble()/60;
          float LongF = Long1.toFloat() + Long2.toFloat()/60;

          // 좌표 출력
          Serial.print("latitude: ");
          Serial.println(LatF, 15);
          Serial.print("longitude: ");
          Serial.println(LongF, 15);
          Serial.print("heading: "); //Heading 값 (방위각)
          Serial.println(azimuth);
        }

        // str 값 초기화 
        str = "";
        
      } else // \n 아닐시, str에 문자를 계속 더하기
        { 
        str += c;
      }
    }
}
