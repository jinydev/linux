---
layout: home
---

# Nginx with yum 설치

### yum
래드햇 계열의 리눅스를 사용하는 경우에는 `yum`을 통하여 설치합니다.


1. nginx를 yum으로 설치할 수 있도록 외부 저장소(repository)를 추가합니다.

```
vi /etc/yum.repos.d/nginx.repo
```

다음과 같이 내용을 추가
```ini
```

2. install by using yum
```
yum install nginx -y
```

3. 시작과 정지

시작
```
nginx
```

정지
```
nginx -s stop
```

재시작
```
nginx -s reload
```

> reload vs restart
> reload는 프로세스 id가 변경되지 않습니다. 기존에 프로세스가 실행되고 있는 메모리에 다시 프로스세를 실행하기 때문에 id가 변경되지 않습니다. 반대로 restart는 프로세스를 죽이고, 새로 생성하여 실행하는 것이기 때문에 id가 변경됩니다.


4. process 확인
```
os -ef | grep nginx
```

5. 서비스에 등록하기
```
systemctl start nginx
systemctl enable nginx
systemctl stop nginx
```