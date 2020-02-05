```bash
# 컨테이너 베쉬 실행 
docker exec -it instagram /bin/bash


# nginx 
nginx -g "daemon off;"

# gunicorn 
gunicorn -b unix:/run/instagram.sock config.wsgi. 


```





Supervisord 모듈 활용. gunicorn 과  nginx 동시 실행 



```bash
supervisord -c ../.config/supervisord.conf -n

```





instagram/.config/supervisord.conf 



```python
[supervisord]
logfile=/var/log/supervisor.log
user=root

[program:nginx]
command=nginx -g "daemon off;"

[program:gunicorn]
command=gunicorn -b unix:/run/instagram.sock config.wsgi

```





**로컬에서 docker run** 



1. build 
   - poetry export 
   - docker build 
2. copy secrets 
   - docker run (bash)
   - docker cp secrets.json 
3. run 
   - collectstatic 
   - docker run (supervisor)



**배포해서 run까지 하려면?** 



1. (Local) build, push 
2. (서버) pull, run (bash)
3. (local) secrets를 서버로 copy 
4. (서버) secrets를 container로 copy 
5. (서버) run 
   - collectstatic 
   - docker run (supervisor)





