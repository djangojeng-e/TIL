# Http: 80 



**암호화 방법** 



- 대칭키 암호화 

  원문 -> 키 -> 암호문 

  암호문 -> 키 -> 원문 

  

- 공개키 /개인키 기법 

  원문 -> 공개키 (암호화) -> 개운키 (복호화) -> 원문 

  원문 -> 개인키(암호화) -> 공개키 (복호화) -> 원문 

  개인키 (private key) <- 절대로 노출되면 안됨 

  공개키 (public key) <- 외부에 노출되어도 상관 없음 

  

  A가 B와 통신하고 싶을때 

  1. A가 자신의 공개키를 HTTP 를 사용해서 B에게 보냄. 
  2. B는 A 에게 HTTP를 사용해서 자신의 공개키를 보냄.
  3. A는 B 에게 보낼 메시지를 B 의 공개키를 사용해서 암호화하여 보냄. 
  4. B 는 받은 메세지를 자신의 "개인키"로 복화해서 읽는다. 

  

  

- Hashing

  raw_password -> 서버로직 -> hash value stored in database  





# HTTP에 공개키/개인키 추가 -> HTTPS 



중간에서 데이터가 탈취되는 위험을 줄일수 있음. 





Let's Encrypt 

- 인증서 발급 
- 인증서와 공개키, 개인키를 Ngnix가 사용하도록 설정 
- 인증서 자동 갱신 





**<u>certbot프로그램을 이용해서 Let's Encrypt기관의 인증서를 받는다.**</u>





- 직접 설치 방법과 
- docker를 사용해서 실행  --> 인증서, 개인키, 공개키 가 나오게됨. 이 저장될 영역을 --volume옵션에 추가 



- docker run --volume 

  Host의 특정 영역 - Container의 특정 영역과 공유 





```bash
sudo docker run --rm -it --name certbot -v '/etc/letsencrypt:/etc/letsencrypt' -v '/var/lib/letsencrypt:/var/lib/letsencrypt' certbot/certbot certonly
```

