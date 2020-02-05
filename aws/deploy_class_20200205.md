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

