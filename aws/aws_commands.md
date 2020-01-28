# AWS EC2 



CML 에서 EC2로 접속하기 



```bash
ssh -i ~/.ssh/wp.pem ubuntu@{myipaddress}
```





CML 에서 EC2에 파일 올리기 



```bash
scp -i ~/.ssh/wp.pem ~{EC2에 경로 지정} ubuntu@{myipaddress}
```

 

Class example



```bash
# 파일 업로드  
scp -i ~/.ssh/wp.pem -r ~/projects/wps12th/instagram/ubuntu@{my ip address}:home/ubuntu/projects/ 

# 스크린 사용 

screen -S runserver # 런서버라는 세션명 생성 
# ctrl + a d (Screen 끄기)
screen -R runserver # 런서버 스크린 복원 
exit # screen 종료 

```

