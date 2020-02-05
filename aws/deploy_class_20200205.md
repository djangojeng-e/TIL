```bash
# 컨테이너 베쉬 실행 
docker exec -it instagram /bin/bash


# nginx 
nginx -g "daemon off;"

# gunicorn 
gunicorn -b unix:/run/instagram.sock config.wsgi. 


```

