# Setting Up Database on AWS 



# 

**In order to use MySQL instead of using SQLite, we can use RDS service provided by AMAZON WEB SERVICES**



AWS maintains server centres across different regions in the world. The closer to the server centres from our area gives faster response speed. Therefore, the region has to be set as the closest region from the area we live in. 



Regions you could use your AWS services will be as below. 



US East - 1

US East - 2

US West - 1 

US West - 2 



ASIA PACIFIC (HONG KONG) 

ASIA PACIFIC (MUMBAI)

ASIA PACIFIC (SEOUL)

ASIA PACIFIC (SINGAPORE)

ASIA PACIFIC (SYDNEY)

ASIA PACIFIC(TOKYO) 



CA - CENTRAL (CANADA)



EUROPE (FRANKFRUIT)

EUROPE (IRELAND)

EUROPE(LONDON)

EUROPE(PARIS)

EUROPE(STOCKHOLM)



MIDDLE EAST (BAHRAIN)



SOUTH AMERICA (BRAZIL )





# 데이터베이스 서버를 중앙화 하는 이유 



- 여러 웹 서버 인스턴스들간에 데이터를 공유해야 하기 때문 
- 공유해야 하는 파일들이 있기 때문에 별도의 파일 서버를 사용 
- 미디어 파일들을 공유해 사용할수 있도록 아마존 S3를 사용 

- 미디어 파일들 뿐만 아니라, 정적 파일들도 S3를 설정해 사용 



